import pandas as pd

def calculate_rfm_scores(transactions_df):
    """
    Calculate RFM scores for each customer based on transactional data.

    Args:
        transactions_df (DataFrame): DataFrame containing transactional data.

    Returns:
        DataFrame: DataFrame containing RFM scores for each customer.
    """
    now = pd.to_datetime('2024-05-11')  # Assuming you want the date in the same format

    # Calculate Recency
    recency_df = transactions_df.groupby('customer_id')['date_of_payment'].max().reset_index()
    recency_df.columns = ['CustomerID', 'LastPurchaseDate']
    recency_df['Recency'] = (now - recency_df['LastPurchaseDate']).dt.days
    recency_df.drop('LastPurchaseDate', axis=1, inplace=True)

    # Calculate Frequency
    transactions_df.drop_duplicates(subset=['transaction_id', 'customer_id'], keep="first", inplace=True)
    frequency_df = transactions_df.groupby('customer_id')['transaction_id'].count().reset_index()
    frequency_df.columns = ['CustomerID', 'Frequency']

    # Calculate Monetary
    transactions_df['TotalCost'] = transactions_df['amount']
    monetary_df = transactions_df.groupby('customer_id')['TotalCost'].sum().reset_index()
    monetary_df.columns = ['CustomerID', 'Monetary']

    # Merge Recency, Frequency, and Monetary DataFrames
    temp_df = recency_df.merge(frequency_df, on='CustomerID')
    rfm_df = temp_df.merge(monetary_df, on='CustomerID')

    # Set CustomerID as index
    rfm_df.set_index('CustomerID', inplace=True)

    return rfm_df

def assign_score(x, p, d):
    """
    Assign score based on quartiles.

    Args:
        x (int): Value.
        p (str): Column name.
        d (dict): Quartiles dict.

    Returns:
        int: Score.
    """
    if x <= d[p][0.25]:
        return 4
    elif x <= d[p][0.50]:
        return 3
    elif x <= d[p][0.75]: 
        return 2
    else:
        return 1

def assign_rfm_score(rfm_segmentation, quantiles):
    """
    Assign RFM score based on quartiles.

    Args:
        rfm_segmentation (DataFrame): DataFrame containing RFM data.
        quantiles (dict): Quartiles dict.
    """
    rfm_segmentation['R_Quartile'] = rfm_segmentation['Recency'].apply(assign_score, args=('Recency', quantiles))
    rfm_segmentation['F_Quartile'] = rfm_segmentation['Frequency'].apply(assign_score, args=('Frequency', quantiles))
    rfm_segmentation['M_Quartile'] = rfm_segmentation['Monetary'].apply(assign_score, args=('Monetary', quantiles))
    rfm_segmentation['RFMScore'] = rfm_segmentation['R_Quartile'].map(str) + rfm_segmentation['F_Quartile'].map(str) + rfm_segmentation['M_Quartile'].map(str)

    for column in rfm_segmentation.columns:
        if rfm_segmentation[column].dtype == 'int64':
            rfm_segmentation[column] = rfm_segmentation[column].astype('float64')

    return rfm_segmentation

# Load your transactional data from the CSV file
transactions_df = pd.read_csv('Data/transactions_data.csv')
transactions_df['date_of_payment'] = pd.to_datetime(transactions_df['date_of_payment'])

# Calculate RFM scores
rfm_segmentation = calculate_rfm_scores(transactions_df)

# Get quartiles
quantiles = rfm_segmentation.quantile(q=[0.25,0.5,0.75]).to_dict()

# Assign RFM scores
rfm_segmentation = assign_rfm_score(rfm_segmentation, quantiles)

# Save RFM scores to a CSV file
rfm_segmentation.to_csv('Data/rfm_data.csv')
