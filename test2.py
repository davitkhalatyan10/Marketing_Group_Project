import pandas as pd
import CustomerFrequency.Model.rfm as rfm

def main():
    """
    Main function to execute the RFM analysis workflow.
    """
    transaction_file_path = 'Data/transactions_data.csv'
    output_file_path = 'Data/rfm_scores.csv'

    # Load transactional data
    transaction_data = pd.read_csv(transaction_file_path)

    # Perform RFM analysis
    rfm_table = rfm.calculate_rfm_scores(transaction_data)

    # Save RFM scores to a CSV file
    rfm_table.to_csv(output_file_path)

    # Display RFM table
    print(rfm_table)

if __name__ == "__main__":
    main()
