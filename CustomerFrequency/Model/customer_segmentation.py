
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def load_data(customer_file_path, transaction_file_path):

    customer_data = pd.read_csv(customer_file_path)
    transaction_data = pd.read_csv(transaction_file_path)
    return customer_data, transaction_data


def display_data_head(customer_data, transaction_data):
    
    customer_data_head = customer_data.head()
    transaction_data_head = transaction_data.head()
    print("Customer Data Head:\n", customer_data_head)
    print("\nTransaction Data Head:\n", transaction_data_head)


""" Customer Data
customer_id: Unique identifier for each customer.\
first_name: Customer's first name.\
last_name: Customer's last name.\
phone_number: Customer's phone number.\

Transaction Data\
transaction_id: Unique identifier for each transaction.\
date_of_payment: Date and time when the transaction occurred.\
customer_id: Identifier linking the transaction to a specific customer.\
employee_id: Identifier for the employee who handled the transaction.\
amount: The amount of money involved in the transaction.\
type: The payment type (e.g., Apple Pay, MasterCard, cash).\

As we know that the data is without N/A, we can move on data cleaning process
"""

"""Next Steps:
Convert the date format: Change the date_of_payment column to datetime format.
Analysis: Calculate the number of transactions per customer to begin the segmentation process."""


def convert_date_format(transaction_data):
    """
    Converts the date format of the 'date_of_payment' column in the transaction data to datetime.

    Args:
        transaction_data (DataFrame): Transaction data DataFrame.
    """
    transaction_data['date_of_payment'] = pd.to_datetime(transaction_data['date_of_payment'])
    return transaction_data

def calculate_transactions_per_customer(transaction_data, customer_data):
    """
    Calculates the number of transactions per customer and merges it with the customer data.

    Args:
        transaction_data (DataFrame): Transaction data DataFrame.

    Returns:
        DataFrame: Merged DataFrame containing customer data with transaction counts.
    """
    transactions_per_customer = transaction_data['customer_id'].value_counts().reset_index()
    transactions_per_customer.columns = ['customer_id', 'transaction_count']
    customer_transaction_data = pd.merge(customer_data, transactions_per_customer, on='customer_id', how='left').fillna(0)
    return customer_transaction_data




"""Data Overview:
customer_id: Unique customer identifier.\
first_name, last_name: Customer's name.\
phone_number: Customer's phone number.\
transaction_count: Number of transactions completed by each customer.\

Next Steps: Define Customer Segments\
We will now define customer segments based on the transaction_count. A simple way to segment might be:\

Frequent Buyers: More than 5 transactions.\
Occasional Buyers: Between 2 and 5 transactions.\
One-Time Buyers: 1 transaction.\
Inactive: No transactions."""

def categorize_customer(x):
    """
    Categorizes customers into segments based on transaction count.

    Args:
     x (int): Transaction count for a customer.

    Returns:
    str: Customer segment.
    """
    if x > 5:
        return 'Frequent Buyer'
    elif x >= 2 and x <= 5:
        return 'Occasional Buyer'
    elif x == 1:
        return 'One-Time Buyer'
    else:
        return 'Inactive'


def define_customer_segments(customer_transaction_data):
    """
    Defines customer segments based on transaction count.

    Args:
        customer_transaction_data (DataFrame): DataFrame containing customer data with transaction counts.

    Returns:
        DataFrame: DataFrame with customer segments added.
    """
    customer_transaction_data['customer_segment'] = customer_transaction_data['transaction_count'].apply(categorize_customer)
    customer_segment_distribution = customer_transaction_data['customer_segment'].value_counts()
    return customer_segment_distribution, customer_transaction_data

    

"""We have successfully categorized the customers into segments based on their transaction frequency. Here is the distribution of the customer segments:

Occasional Buyer: 1330 customers\
One-Time Buyer: 416 customers\
Inactive: 161 customers\
Frequent Buyer: 93 customers\

# Summary and Insights:
Occasional Buyers are the largest group, suggesting that a significant number of customers return for purchases a few times. Marketing strategies that encourage repeated interactions might be effective here.
One-Time Buyers and Inactive categories represent potential for increasing engagement through promotional campaigns or loyalty programs.
Frequent Buyers, while the smallest group, are likely your most loyal customers and could be targeted with premium offers or membership benefits."""


def visualize_customer_segments(customer_segment_distribution):
    """
    Visualizes the distribution of customer segments using a pie chart.

    Args:
        customer_segment_distribution (Series): Distribution of customer segments.
    """
    labels = customer_segment_distribution.index
    sizes = customer_segment_distribution.values
    colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']
    explode = (0.1, 0.1, 0.1, 0.1)

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, colors=colors)
    ax1.axis('equal')

    plt.title('Customer Segmentation Based on Transaction Frequency')
    plt.show()



"""Insights and Strategic Directions:
1. Occasional Buyers (63.3%): This is the largest segment. Strategies to consider include:
    * Loyalty Programs: Introduce or enhance loyalty programs to increase the frequency of visits.
    * Targeted Promotions: Offer promotions on popular items or during specific times to encourage more frequent purchases.
2. One-Time Buyers (19.8%): To reduce churn and convert them into more frequent visitors, consider:
    * Follow-Up Marketing: Implement follow-up marketing strategies, such as feedback requests or second-purchase discounts.
    * Personalized Offers: Use purchase history data to send personalized offers and recommendations.
3. Inactive (7.7%): To re-engage these customers:
    * Reactivation Campaigns: Send reactivation emails or texts with special offers to entice them back.
    * Survey for Feedback: Understand why they have not returned and address these concerns in your services.
4. Frequent Buyers (4.4%): Since this group likely drives a significant portion of revenue:
    * VIP Programs: Create exclusive VIP programs with special perks.
    * Engage with Exclusivity: Offer them exclusive products or early access to new items.
"""
def generate_satisfaction_scores(customer_transaction_data):
    """
    Generates synthetic satisfaction scores for customer transaction data.

    Args:
        customer_transaction_data (DataFrame): DataFrame containing customer data with transaction counts.

    Returns:
         DataFrame: DataFrame with satisfaction scores added.
    """
    np.random.seed(42)
    satisfaction_scores = np.random.normal(loc=7, scale=1.5, size=len(customer_transaction_data))
    satisfaction_scores_clamped = np.clip(satisfaction_scores, 1, 10)
    customer_transaction_data['satisfaction_score'] = np.round(satisfaction_scores_clamped).astype(int)
    return customer_transaction_data

def save_data_with_satisfaction_scores(customer_transaction_data, output_file_path):
    
    customer_transaction_data.to_csv(output_file_path, index=False)


"""Interpretation of Data Information and Descriptive Statistics:
1. Data.info() output:
    * There are 2000 entries, which means the dataset contains information about 2000 customer transactions.
    * There are 7 columns with no missing values.
    * customer_id, transaction_count, and satisfaction_score are numeric, while the rest are objects (likely strings).
2. Data.describe() output:
    * The average transaction_count is approximately 2.5, suggesting that on average, a customer makes about 2-3 transactions.
    * The mean satisfaction_score is around 7, which is a good sign as it indicates a generally satisfied customer base. However, this is a synthetic dataset, so this interpretation is more about understanding the method rather than deriving actual insights.
    * The range for transaction_count is 0 to 9, and for satisfaction_score, it's 2 to 10. There are no outliers in the satisfaction scores, as all values fall within the expected range.
3. Correlation coefficient output:
    * The correlation coefficient of approximately 0.0026 suggests there is virtually no linear relationship between transaction_count and satisfaction_score.
    """


    
    

def analyze_data(file_path):

    df = pd.read_csv(file_path)
    """
    Analyzes customer transaction data.

    Args:
     df (DataFrame): DataFrame containing customer transaction data with satisfaction scores.

    Returns:
    dict: Dictionary containing analysis results.
    """
    analysis_results = {}

    analysis_results['data_overview'] = {
        'info': df.info(),
        'description': df.describe()
    }

    correlation = df['transaction_count'].corr(df['satisfaction_score'])
    analysis_results['correlation'] = correlation

    return analysis_results

def visualize_data(df):
    
    # Boxplot
    plt.figure(figsize=(10, 6))
    boxplot = sns.boxplot(x='customer_segment', y='satisfaction_score', data=df)
    boxplot.set_title('Satisfaction Scores by Customer Segment')

    medians = df.groupby(['customer_segment'])['satisfaction_score'].median().values
    median_labels = [str(np.round(s, 2)) for s in medians]

    pos = range(len(medians))
    for tick, label in zip(pos, boxplot.get_xticklabels()):
        boxplot.text(pos[tick], medians[tick] + 0.1, median_labels[tick], 
                     horizontalalignment='center', size='medium', color='w', weight='semibold')

    plt.show()

    # Scatter Plot
    plt.figure(figsize=(12, 8))
    scatterplot = sns.scatterplot(x='transaction_count', y='satisfaction_score', data=df)
    sns.regplot(x='transaction_count', y='satisfaction_score', data=df, scatter=False, ax=scatterplot)

    scatterplot.set_title('Transaction Count vs Satisfaction Score')
    scatterplot.set_xlabel('Transaction Count')
    scatterplot.set_ylabel('Satisfaction Score')
    plt.show()

# def main():
#     """
#     Main function to execute the analysis workflow.
#     """
#     customer_file_path = './Data/customer_data.csv'
#     transaction_file_path = './Data/transactions_data.csv'
#     output_file_path = './Data/Customer_Transaction_with_Satisfaction.csv'


#     customer_data, transaction_data = load_data(customer_file_path, transaction_file_path)
#     # display_data_head(customer_data, transaction_data)
#     transaction_data = convert_date_format(transaction_data)
#     customer_transaction_data = calculate_transactions_per_customer(transaction_data, customer_data)
#     customer_segment_distribution,customer_transaction_data = define_customer_segments(customer_transaction_data)
#     # print(customer_segment_distribution)
#     # print(customer_transaction_data)

#     customer_transaction_data = generate_satisfaction_scores(customer_transaction_data)
#     # print(customer_transaction_data)
#     customer_transaction_data.drop('first_name', inplace=True, axis=1) 
#     customer_transaction_data.drop('last_name', inplace=True, axis=1) 
#     customer_transaction_data.drop('phone_number', inplace=True, axis=1) 
#     # print(customer_transaction_data)
#     # Attempting to save the updated customer transaction data with satisfaction scores to a CSV file
#     import os 
#     # Check whether the specified 
#     # path exists or not 
#     if os.path.exists(output_file_path):
#         os.remove(output_file_path)
#         save_data_with_satisfaction_scores(customer_transaction_data, output_file_path)
#     else:
#         save_data_with_satisfaction_scores(customer_transaction_data, output_file_path)

#     # Load data
#     customer_data, transaction_data = load_data(customer_file_path, transaction_file_path)

#     # Display data head
#     display_data_head(customer_data, transaction_data)

#     # Convert date format
#     convert_date_format(transaction_data)

#     # Calculate transactions per customer
#     customer_transaction_data = calculate_transactions_per_customer(transaction_data, customer_data)
#     print(customer_transaction_data.head())

#     # Define customer segments
#     customer_segment_distribution,customer_transaction_data = define_customer_segments(customer_transaction_data)
#     print(customer_segment_distribution)
#     print(customer_transaction_data.head())

#     # Visualize customer segments
#     visualize_customer_segments(customer_segment_distribution)

#     # Analyze data
#     analysis_results = analyze_data(output_file_path)
#     print("\nAnalysis Results:\n", analysis_results)

#     # Visualize data
#     visualize_data(pd.read_csv(output_file_path))

# if __name__ == "__main__":
#     main()
    

"""1. Boxplot (Satisfaction Scores by Customer Segment):
    * This shows the distribution of satisfaction scores within each customer segment (Inactive, Occasional Buyer, One-Time Buyer, and Frequent Buyer).
    * All segments have a median satisfaction score of 7, indicating a uniform level of satisfaction across different customer types.
    * The spread of scores, as indicated by the length of the boxes and whiskers, shows variability in satisfaction within each segment. However, the consistency of the median suggests that across all segments, customers tend to report a similar level of satisfaction.
2. Scatter Plot (Transaction Count vs Satisfaction Score):
    * The scatter plot displays individual customer data points with their transaction count on the x-axis and satisfaction score on the y-axis.
    * The trend line is flat, which visually confirms the very low correlation coefficient we calculated earlier, suggesting no clear relationship between the number of transactions a customer makes and their reported satisfaction score.
    * The data points are spread widely on the satisfaction score axis for similar transaction counts, further demonstrating that transaction frequency does not necessarily predict satisfaction.
"""