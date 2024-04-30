from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path
import pandas as pd
from ..DataBase import SqlHandler


app = FastAPI()
dbname = 'temp'


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/get_data")
async def get_records():
    return {'data': 'data'}

@app.get("/get_image1")
async def get_visualization1():
    image_path = Path('visualization1.png')
    return FileResponse(image_path)

@app.get("/get_image2")
async def get_visualization2():
    image_path = Path('visualization2.png')
    return FileResponse(image_path)

@app.get("/get_image3")
async def get_visualization3():
    image_path = Path('visualization3.png')
    return FileResponse(image_path)

@app.get("/get_data/avg_frequency")
async def average_visit_frequency():
    '''
    Calculate visits per day for each customer.
    '''
    orders = sqlint.SqlHandler(dbname, 'orders')
    cursor = orders.cursor
    cursor.execute('''SELECT DATEDIFF(day, MAX(date_of_order), MIN(date_of_order)), customer_id FROM orders
                        GROUP BY  customer_id
                        ORDER BY customer_id;''')
    differences = cursor.fetchall()
    cursor.execute('''SELECT COUNT(customer_id), customer_id FROM orders
                        GROUP BY customer_id
                        ORDER BY customer_id;''')
    counts = cursor.fetchall()
    frequencies = []
    for count, difference in (counts, differences):
        avg = round(count[0]/difference[0], 1)
        frequencies.append((avg, count[1]))
    return dict(frequencies)

@app.get("/get_data/no_visit")
async def no_visit30():
    '''
    Select all customers that have not visited us in last 30 or more days.
    '''
    orders = sqlint.SqlHandler(dbname, 'orders')
    cursor = orders.cursor
    cursor.execute('''SELECT DISTINCT c.customer_id, c.first_name, c.last_name FROM customers c
                        INNER JOIN orders o ON c.customer_id = o.customer_id
                        WHERE o.date_of_order <= DATE_SUB(NOW(), INTERVAL 30 DAY);
                        ''')
    customers = cursor.fetchall()
    result = []
    for row in customers:
        name = row[1] + ' ' + row[2]
        result.append((row[0], name))

    return dict(result)

@app.get("/get_data/top_customers/{n}")
async def top_visits(n):
    '''
    Return top n of customers with the highest visit frequency.
    '''
    orders = sqlint.SqlHandler(dbname, 'orders')
    cursor = orders.cursor
    cursor.execute('''SELECT COUNT(o.customer_id) AS vsits, c.customer_id, c.first_name, c.last_name FROM orders o 
                        INNER JOIN customers c ON c.customer_id = o.customer_id
                        GROUP BY o.customer_id
                        ORDER BY visits;''')
    visits = cursor.fetchall()
    top = visits[:n]
    result = {}
    for row in top:
        name = row[2] + ' ' + row[3]
        result[row[1]] = (name, row[0])

    return result

@app.get("/get_data/bestseller")
async def bestseller():
    '''
    Get the customers' most beloved product.
    '''
    orders = sqlint.SqlHandler(dbname, 'orders')
    cursor = orders.cursor
    cursor.execute('''SELECT m.menu_id, m.name, m.size, SUM(o.quantity_ordered) AS quantity FROM Menu m
                        INNER JOIN orders o ON m.menu_id = o.menu_id
                        GROUP BY o.menu_id
                        ORDER BY quantity''')
    top = cursor.fetchall()[0]
    bestseller = {top[0]: [top[1], top[2]]}
    return bestseller

@app.post("/create_data")
async def create_item(item):
    return {'item': 'inserted'}

@app.post("/create_data/coffee_purchase")
async def coffee_transaction(transaction_id, date_of_payment, amount, type, customer_id, employee_id):
    '''
    Add each order transaction to the database.
    '''
    transactions = sqlint.SqlHandler(dbname, 'transaction1')
    data = {'transaction_id': transaction_id, 'date_of_payment': date_of_payment,
            'amount': amount, 'type': type, 'customer_id': customer_id, 'employee_id': employee_id}
    transactions.insert_many(pd.DataFrame(data))
    return {'message': 'Data inserted successfully'}

@app.put("/update_data/{item_id}")
async def update_item(item_id, item):
    return {"message": "Item updated successfully"}

@app.delete("/delete_data/{record_id}")
async def delete_record(record_id: int):
    return {"message": "Record deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
