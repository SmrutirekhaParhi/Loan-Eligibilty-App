import pandas as pd

# Load the dataset
df = pd.read_csv(r'Loan-Eligibility-App\model\loan_prediction.csv')  # Ensure the CSV is in the same folder

# Drop ID column if it exists
if 'Loan_ID' in df.columns:
    df = df.drop('Loan_ID', axis=1)

# Fill missing values
for col in ['Gender', 'Married', 'Dependents', 'Self_Employed']:
    df[col] = df[col].fillna(df[col].mode()[0])
df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0])
df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode()[0])

# Convert Loan_Status to numeric
df['Loan_Status'] = df['Loan_Status'].map({'Y': 1, 'N': 0})

# Check class distribution
print("Class distribution (as ratio):")
print(df['Loan_Status'].value_counts(normalize=True))

print("\nAbsolute class counts:")
print(df['Loan_Status'].value_counts())
