import joblib
import numpy as np
import pandas as pd
import sys
import json

# Load model and tools
model = joblib.load('model/svm_loan_model.pkl')
scaler = joblib.load('model/scaler.pkl')
model_columns = joblib.load('model/model_columns.pkl')

def preprocess_input(user_input):
    df = pd.DataFrame([user_input])
    categorical = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']
    df = pd.get_dummies(df, columns=categorical)

    for col in model_columns:
        if col not in df.columns:
            df[col] = 0

    df = df[model_columns]

    numerical = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']
    df[numerical] = scaler.transform(df[numerical])

    return df

def main():
    input_data = json.loads(sys.stdin.read())
    processed = preprocess_input(input_data)
    pred = model.predict(processed)[0]
    prob = model.predict_proba(processed)[0].max()

    print(json.dumps({
        "prediction": str(pred),
        "probability": round(float(prob), 2)
    }))

if __name__ == '__main__':
    main()
