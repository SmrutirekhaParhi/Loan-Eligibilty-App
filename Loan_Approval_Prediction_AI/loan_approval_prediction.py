import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.svm import SVC
import matplotlib.pyplot as plt

# Load the CSV data
df = pd.read_csv('../Loan_Approval_Prediction_AI/loan_prediction.csv')

# Drop Loan_ID column if it exists
if 'Loan_ID' in df.columns:
    df = df.drop('Loan_ID', axis=1)

# Fill missing values (no inplace, to avoid FutureWarning)
for col in ['Gender', 'Married', 'Dependents', 'Self_Employed']:
    df[col] = df[col].fillna(df[col].mode()[0])

df['LoanAmount'] = df['LoanAmount'].fillna(df['LoanAmount'].median())
df['Loan_Amount_Term'] = df['Loan_Amount_Term'].fillna(df['Loan_Amount_Term'].mode()[0])
df['Credit_History'] = df['Credit_History'].fillna(df['Credit_History'].mode()[0])

'''
# ==== 1. Gender Distribution Bar Chart ====
gender_counts = df['Gender'].value_counts()
plt.bar(gender_counts.index, gender_counts.values, color='#50703A')  # <-- Changed to green
plt.xlabel('Gender')
plt.ylabel('Count')
plt.title('Gender Distribution')
plt.show()

# ==== 2. Loan Status vs Property Area Grouped Bar Chart ====
ax = df.groupby(['Property_Area', 'Loan_Status']).size().unstack().plot(
    kind='bar', color=['#50703A', '#B53524'])  # <-- Changed colors (green first, red second)
plt.xlabel('Property Area')
plt.ylabel('Count')
plt.title('Loan Status by Property Area')
plt.legend(title='Loan Status', labels=['Approved', 'Not Approved'])  # <-- Swapped labels to match colors
plt.tight_layout()
plt.show()'''


# Convert categorical columns to numbers
cat_cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']
df = pd.get_dummies(df, columns=cat_cols)

# Split data
X = df.drop('Loan_Status', axis=1)
y = df['Loan_Status']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale numerical features
scaler = StandardScaler()
numerical_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']
X_train[numerical_cols] = scaler.fit_transform(X_train[numerical_cols])
X_test[numerical_cols] = scaler.transform(X_test[numerical_cols])

# Train the model
model = SVC(random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Print some results
print("Predictions for test data:")
print(y_pred)

# Make a table with the test data and predictions
X_test_df = pd.DataFrame(X_test, columns=X_test.columns)
X_test_df['Predicted Loan Status'] = y_pred

# Show the first 10 predictions as a table
print("\nFirst 10 predictions:")
print(X_test_df.head(10))

# Show how many 'Y' and 'N' predictions
unique, counts = np.unique(y_pred, return_counts=True)
result_counts = dict(zip(unique, counts))
print("\nPrediction counts:", result_counts)

# Save the results to a CSV file
X_test_df.to_csv('loan_predictions_with_results.csv', index=False)
print("\nResults saved to loan_predictions_with_results.csv")

'''
# ==== 3. Loan Approval Predictions Bar Chart ====
plt.bar(result_counts.keys(), result_counts.values(), color=['#50703A', '#B53524'])  # <-- Changed colors
plt.xlabel('Loan Status')
plt.ylabel('Number of Predictions')
plt.title('Loan Approval Predictions')
plt.show()'''

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Confusion Matrix
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

import joblib
joblib.dump(model, 'svm_loan_model.pkl')