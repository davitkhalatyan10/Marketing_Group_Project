import CustomerFrequency.Model.customer_segmentation as cs
import pandas as pd

def main():
    """
    Main function to execute the analysis workflow.
    """
    customer_file_path = 'Data/customer_data.csv'
    transaction_file_path = 'Data/transactions_data.csv'
    output_file_path = 'Data/Customer_Transaction_with_Satisfaction.csv'


    customer_data, transaction_data = cs.load_data(customer_file_path, transaction_file_path)
    # display_data_head(customer_data, transaction_data)
    transaction_data = cs.convert_date_format(transaction_data)
    customer_transaction_data = cs.calculate_transactions_per_customer(transaction_data, customer_data)
    customer_segment_distribution,customer_transaction_data = cs.define_customer_segments(customer_transaction_data)
    # print(customer_segment_distribution)
    # print(customer_transaction_data)

    customer_transaction_data = cs.generate_satisfaction_scores(customer_transaction_data)
    # print(customer_transaction_data)
    customer_transaction_data.drop('first_name', inplace=True, axis=1) 
    customer_transaction_data.drop('last_name', inplace=True, axis=1) 
    customer_transaction_data.drop('phone_number', inplace=True, axis=1) 
    # print(customer_transaction_data)
    # Attempting to save the updated customer transaction data with satisfaction scores to a CSV file
    import os 
    # Check whether the specified 
    # path exists or not 
    if os.path.exists(output_file_path):
        os.remove(output_file_path)
        cs.save_data_with_satisfaction_scores(customer_transaction_data, output_file_path)
    else:
        cs.save_data_with_satisfaction_scores(customer_transaction_data, output_file_path)

    # Load data
    customer_data, transaction_data = cs.load_data(customer_file_path, transaction_file_path)

    # Display data head
    cs.display_data_head(customer_data, transaction_data)

    # Convert date format
    cs.convert_date_format(transaction_data)

    # Calculate transactions per customer
    customer_transaction_data = cs.calculate_transactions_per_customer(transaction_data, customer_data)
    print(customer_transaction_data.head())

    # Define customer segments
    customer_segment_distribution,customer_transaction_data = cs.define_customer_segments(customer_transaction_data)
    print(customer_segment_distribution)
    print(customer_transaction_data.head())

    # Visualize customer segments
    cs.visualize_customer_segments(customer_segment_distribution)

    # Analyze data
    analysis_results = cs.analyze_data(output_file_path)
    print("\nAnalysis Results:\n", analysis_results)

    # Visualize data
    cs.visualize_data(pd.read_csv(output_file_path))

if __name__ == "__main__":
    main()