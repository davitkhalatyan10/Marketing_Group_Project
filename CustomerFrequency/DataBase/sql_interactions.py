import sqlite3
import logging 
import pandas as pd
import numpy as np
import os
from CustomerFrequency.Logger import CustomFormatter

logger = logging.getLogger(os.path.basename(__file__))
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logger.addHandler(ch)

class SqlHandler:

    def __init__(self, dbname:str,table_name:str) -> None:
        self.cnxn=sqlite3.connect(f'{dbname}.db')
        self.cursor=self.cnxn.cursor()
        self.dbname=dbname
        self.table_name=table_name

    def close_cnxn(self)->None:

        logger.info('commiting the changes')
        self.cursor.close()
        self.cnxn.close()
        logger.info('the connection has been closed')

    def insert_one()->None:
        pass

    def get_table_columns(self) -> list:
        """
        Retrieves column names of the specified table.

        Returns:
            list: List of column names.
        """
        self.cursor.execute(f"PRAGMA table_info({self.table_name});")
        columns = self.cursor.fetchall()

        column_names = [col[1] for col in columns]
        logger.info(f'the list of columns: {column_names}')
        # self.cursor.close()

        return column_names
    
    def truncate_table(self)->None:
        
        query=f"DROP TABLE IF EXISTS {self.table_name};"
        self.cursor.execute(query)
        logging.info(f'the {self.table_name} is truncated')
        # self.cursor.close()

    def drop_table(self):
        
        query = f"DROP TABLE IF EXISTS {self.table_name};"
        logging.info(query)

        self.cursor.execute(query)

        self.cnxn.commit()

        logging.info(f"table '{self.table_name}' deleted.")
        logger.debug('using drop table function')

    def insert_many(self, df: pd.DataFrame) -> str:
        """
        Inserts multiple rows into the specified table
        based on the given Pandas DataFrame.

        Args:
            df (pd.DataFrame): Pandas DataFrame
            containing the data to be inserted.

        Raises:
            Exception: If an error occurs
            while inserting the data into the table.
        """
        df = df.replace(np.nan, None)  # for handling NULLS
        df.rename(columns=lambda x: x.lower(), inplace=True)
        columns = list(df.columns)
        logger.info(f'BEFORE the column intersection: {columns}')
        sql_column_names = [i.lower() for i in self.get_table_columns()]
        columns = list(set(columns) & set(sql_column_names))
        logger.info(f'AFTER the column intersection: {columns}')
        ncolumns = list(len(columns)*'?')
        data_to_insert = df.loc[:, columns]

        values = [tuple(i) for i in data_to_insert.values]
        logger.info(f'''the shape of the table
                    which is going to be imported {data_to_insert.shape}''')

        if len(columns) > 1:
            cols, params = ', '.join(columns), ', '.join(ncolumns)
        else:
            cols, params = columns[0], ncolumns[0]

        logger.info(f'insert structure: colnames: {cols} params: {params}')
        logger.info(values[0])
        query = f"""INSERT INTO  {self.table_name}
        ({cols}) VALUES ({params});"""

        logger.info(f'QUERY: {query}')

        self.cursor.executemany(query, values)
        try:
            for i in self.cursor.messages:
                logger.info(i)
        except:
            pass

        self.cnxn.commit()

        logger.warning('the data is loaded')


    def from_sql_to_pandas(self, chunksize:int, id_value:str) -> pd.DataFrame:
        """
        Retrieves data from the specified table in chunks
        and converts it into a Pandas DataFrame.

        Args:
            chunksize (int): Number of rows to fetch in each chunk.
            id_value (str): Column name to be used for
            ordering and fetching data in chunks.

        Returns:
            pd.DataFrame: Concatenated Pandas DataFrame
            containing the selected data.

        """
        
        offset=0
        dfs=[]
       
        
        while True:
            query=f"""
            SELECT * FROM {self.table_name}
                ORDER BY {id_value}
                OFFSET  {offset}  ROWS
                FETCH NEXT {chunksize} ROWS ONLY  
            """
            data = pd.read_sql_query(query,self.cnxn) 
            logger.info(f'the shape of the chunk: {data.shape}')
            dfs.append(data)
            offset += chunksize
            if len(dfs[-1]) < chunksize:
                logger.warning('loading the data from SQL is finished')
                logger.debug('connection is closed')
                break
        df = pd.concat(dfs)

        return df


    def update_table(self,condition, new_values):
        set_clause = ', '.join([f"{key} = ?" for key in new_values.keys()])
        values = tuple(new_values.values())
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE {condition}"
        self.cursor.execute(query, values)
        self.cnxn.commit()
        logger.info('Table updated successfully.')



    def top_visits(self):
        self.cursor.execute('''SELECT COUNT(o.customer_id) AS vsits, c.customer_id, c.first_name, c.last_name FROM orders o 
                                INNER JOIN customers c ON c.customer_id = o.customer_id
                                GROUP BY o.customer_id
                                ORDER BY visits;''')
        visits = self.cursor.fetchall()
        return visits
    
    def bestseller(self):
        self.cursor.execute('''SELECT m.menu_id, m.name, m.size, SUM(o.quantity_ordered) AS quantity FROM Menu m
                        INNER JOIN orders o ON m.menu_id = o.menu_id
                        GROUP BY o.menu_id
                        ORDER BY quantity''')
        top = self.cursor.fetchall()[0]
        return top
    
    def no_visits_n_days(self):
        self.cursor.execute('''SELECT DISTINCT c.customer_id, c.first_name, c.last_name FROM customers c
                        INNER JOIN orders o ON c.customer_id = o.customer_id
                        WHERE o.date_of_order <= DATE_SUB(NOW(), INTERVAL {n} DAY);
                        ''')
        customers = self.cursor.fetchall()
        return customers
    
    def average_visit_frequency(self):
        self.cursor.execute('''SELECT COUNT(o.customer_id), o.customer_id, c.phone_number
                            FROM orders o
                            JOIN customers c ON o.customer_id = c.customer_id
                            GROUP BY o.customer_id, c.phone_number
                            ORDER BY o.customer_id;''')
        counts = self.cursor.fetchall()

        self.cursor.execute('''
                            SELECT julianday(MAX(o.date_of_order)) - julianday(MIN(o.date_of_order)), o.customer_id
                            FROM orders o
                            GROUP BY o.customer_id
                            ORDER BY o.customer_id;
                            ''')

        differences = self.cursor.fetchall()

        return counts, differences
    
    def phone_numbers(self):
        self.cursor.execute('''SELECT c.customer_id, c.phone_number FROM customers c
                    INNER JOIN orders o ON c.customer_id = o.customer_id
                    WHERE o.date_of_order <= DATE_SUB(NOW(), INTERVAL {n} DAY);
                    ''')
        phone_nums = self.cursor.fetchall()
        return phone_nums

   
        



