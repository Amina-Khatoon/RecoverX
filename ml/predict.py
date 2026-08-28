from pathlib import Path
import pandas as pd
import joblib


BASE_DIR = Path(r"C:\Users\Shabina\Desktop\RecoverX")

DATA_PATH = BASE_DIR / "data" / "recovery_data.csv"
MODEL_PATH = BASE_DIR / "ml" / "recovery_model.pkl"


if not DATA_PATH.exists():
    raise FileNotFoundError(f"Dataset not found: {DATA_PATH}")

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model not found: {MODEL_PATH}")


df = pd.read_csv(DATA_PATH)

model = joblib.load(MODEL_PATH)


FEATURES = [
    "case_id",
    "amount_due",
    "days_overdue",
    "monthly_income",
    "monthly_expense",
    "payment_history_score",
    "missed_payments",
    "previous_recovery_rate",
    "contact_success_rate",
    "last_payment_days_ago",
    "account_age_days",
    "reminders_received",
    "digital_engagement",
    "hardship_flag",
    "recovery_days",
]


def predict_recovery(input_data):

    if not isinstance(input_data, dict):
        raise ValueError("Input must be a JSON object")

    missing = [feature for feature in FEATURES if feature not in input_data]

    if missing:
        raise ValueError(
            f"Missing required fields: {', '.join(missing)}"
        )

    input_df = pd.DataFrame(
        [[input_data[feature] for feature in FEATURES]],
        columns=FEATURES
    )

    prediction = model.predict(input_df)

    return prediction[0]
