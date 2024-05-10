import pandas as pd

# Load your transactional data from the database or CSV file
transaction_data = pd.read_csv(transaction_file_path)

def calculate_rfm_scores(transaction_data, output_file_path):
    """
    Calculate RFM scores for each customer based on transactional data.

    Args:
        transaction_data (DataFrame): DataFrame containing transactional data.

    Returns:
        DataFrame: DataFrame containing RFM scores for each customer.
    """
    # Calculate Recency, Frequency, and Monetary metrics
    rfm_table = transaction_data.groupby('customer_id').agg({
        'date_of_payment': lambda x: (pd.Timestamp.now() - pd.to_datetime(x).max()).days,  # Recency
        'transaction_id': 'count',  # Frequency
        'amount': 'sum'  # Monetary
    }).rename(columns={
        'date_of_payment': 'Recency',
        'transaction_id': 'Frequency',
        'amount': 'Monetary'
    })

    # Calculate RFM scores
    rfm_table['R_score'] = pd.qcut(rfm_table['Recency'], q=4, labels=False, duplicates='drop') + 1
    rfm_table['F_score'] = pd.qcut(rfm_table['Frequency'], q=4, labels=False, duplicates='drop') + 1
    rfm_table['M_score'] = pd.qcut(rfm_table['Monetary'], q=4, labels=False, duplicates='drop') + 1

    # Calculate RFM score
    rfm_table['RFM_score'] = rfm_table['R_score'] * 100 + rfm_table['F_score'] * 10 + rfm_table['M_score']

    # Sort the table based on RFM score
    rfm_table = rfm_table.sort_values(by='RFM_score', ascending=False)

    # Save the RFM table to a CSV file
    rfm_table.to_csv(output_file_path)

    return rfm_table
