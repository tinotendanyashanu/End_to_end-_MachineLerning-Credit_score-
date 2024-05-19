
# End-to-End Machine Learning Credit Score Prediction API

This project implements a credit score prediction API using a Support Vector Machine (SVM) model. The API is built using Flask and deployed on Render.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [API Reference](#api-reference)

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
      ```sh
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```sh
      source venv/bin/activate
      ```

4. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Flask app**:
    ```sh
    python app.py
    ```

2. The API will be available at `http://127.0.0.1:5000`.

## Deployment

To deploy the API on Render, follow these steps:

1. **Ensure all dependencies are listed in `requirements.txt`**:
    ```sh
    pip freeze > requirements.txt
    ```

2. **Create a `Procfile`**:
    ```
    web: python app.py
    ```

3. **Commit and push changes to GitHub**:
    ```sh
    git add .
    git commit -m "Prepare for deployment"
    git push origin main
    ```

4. **Create a new web service on Render**:
    - Go to your Render dashboard.
    - Click "New +" and select "Web Service".
    - Connect your GitHub repository and choose the correct branch.
    - Configure the build and start commands if needed.

5. **Deploy the service**.

## API Reference

### Predict Credit Score

#### Endpoint

#### Request

- **Content-Type**: `application/json`
- **Body**: JSON object with the following structure:

    ```json
    {
      "Month": "July",
      "Age": 23,
      "Occupation": "Scientist",
      "Annual_Income": 19114.12,
      "Monthly_Inhand_Salary": 1824.843333,
      "Num_Bank_Accounts": 3,
      "Num_Credit_Card": 4,
      "Interest_Rate": 3,
      "Delay_from_due_date": 3,
      "Num_of_Delayed_Payment": 8,
      "Changed_Credit_Limit": 0,
      "Num_Credit_Inquiries": 0,
      "Credit_Mix": "Standard",
      "Outstanding_Debt": 1885.0,
      "Credit_Utilization_Ratio": 28.72,
      "Credit_History_Age": 0.08333333333333333,
      "Payment_of_Min_Amount": "No",
      "Total_EMI_per_month": 84.28,
      "Amount_invested_monthly": 80.0,
      "Payment_Behaviour": "High_spent_Small_value_payments",
      "Monthly_Balance": 312.4944444444445,
      "Count_Auto Loan": 1,
      "Count_Credit-Builder Loan": 1,
      "Count_Personal Loan": 1,
      "Count_Home Equity Loan": 1,
      "Count_Not Specified": 0,
      "Count_Mortgage Loan": 0,
      "Count_Student Loan": 0,
      "Count_Debt Consolidation Loan": 0,
      "Count_Payday Loan": 0
    }
    ```

#### Response

- **Content-Type**: `application/json`
- **Body**: JSON object with the prediction result:

    ```json
    {
      "prediction": "Good"
    }
    ```

####  CURL Command

```sh
curl -X POST -H "Content-Type: application/json" -d '{
  "Month": "July",
  "Age": 23,
  "Occupation": "Scientist",
  "Annual_Income": 19114.12,
  "Monthly_Inhand_Salary": 1824.843333,
  "Num_Bank_Accounts": 3,
  "Num_Credit_Card": 4,
  "Interest_Rate": 3,
  "Delay_from_due_date": 3,
  "Num_of_Delayed_Payment": 8,
  "Changed_Credit_Limit": 0,
  "Num_Credit_Inquiries": 0,
  "Credit_Mix": "Standard",
  "Outstanding_Debt": 1885.0,
  "Credit_Utilization_Ratio": 28.72,
  "Credit_History_Age": 0.08333333333333333,
  "Payment_of_Min_Amount": "No",
  "Total_EMI_per_month": 84.28,
  "Amount_invested_monthly": 80.0,
  "Payment_Behaviour": "High_spent_Small_value_payments",
  "Monthly_Balance": 312.4944444444445,
  "Count_Auto Loan": 1,
  "Count_Credit-Builder Loan": 1,
  "Count_Personal Loan": 1,
  "Count_Home Equity Loan": 1,
  "Count_Not Specified": 0,
  "Count_Mortgage Loan": 0,
  "Count_Student Loan": 0,
  "Count_Debt Consolidation Loan": 0,
  "Count_Payday Loan": 0
}' https://end-to-end-machinelerning-credit-score.onrender.com/predict

