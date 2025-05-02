import pandas as pd

# Change this to the name of your Excel file
input_excel_file = "loan_prediction.xlsx"

# This will be the name of your new CSV file
output_csv_file = "loan_prediction.csv"

# Read the Excel file
excel_data = pd.read_excel(input_excel_file)

# Save as CSV
excel_data.to_csv(output_csv_file, index=False)
