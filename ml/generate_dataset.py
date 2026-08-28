import numpy as np
import pandas as pd
from pathlib import Path

# Reproducible dataset
np.random.seed(42)

# Number of records
N = 50000

# -----------------------------
# 1. Generate customer features
# -----------------------------

amount_due = np.round(
    np.random.lognormal(mean=8.0, sigma=0.8, size=N), 2
)

days_overdue = np.random.randint(1, 181, N)

monthly_income = np.round(
    np.random.lognormal(mean=10.5, sigma=0.5, size=N), 2
)

monthly_expense = np.round(
    monthly_income * np.random.uniform(0.35, 0.95, N), 2
)

payment_history_score = np.round(
    np.random.uniform(20, 100, N), 2
)

missed_payments = np.random.poisson(2, N)

previous_recovery_rate = np.round(
    np.random.uniform(0, 1, N), 3
)

contact_success_rate = np.round(
    np.random.uniform(0, 1, N), 3
)

last_payment_days_ago = np.random.randint(1, 181, N)

account_age_days = np.random.randint(90, 2500, N)

reminders_received = np.random.randint(0, 8, N)

digital_engagement = np.round(
    np.random.uniform(0, 1, N), 3
)

hardship_flag = np.random.choice(
    [0, 1],
    size=N,
    p=[0.8, 0.2]
)

# -----------------------------
# 2. Calculate financial pressure
# -----------------------------

income_expense_ratio = (
    monthly_expense / monthly_income
)

# -----------------------------
# 3. Create recovery probability
# -----------------------------

score = (
    1.5 * previous_recovery_rate
    + 1.2 * contact_success_rate
    + 0.012 * payment_history_score
    + 0.8 * digital_engagement
    - 0.010 * days_overdue
    - 0.25 * missed_payments
    - 0.004 * last_payment_days_ago
    - 0.8 * hardship_flag
    - 1.0 * np.maximum(income_expense_ratio - 0.75, 0)
)

# Convert score into probability
recovery_probability = 1 / (1 + np.exp(-score + 1.8))

recovery_probability = np.clip(
    recovery_probability,
    0.03,
    0.97
)

# -----------------------------
# 4. Generate target variable
# -----------------------------

recovered = np.random.binomial(
    1,
    recovery_probability
)

# -----------------------------
# 5. Create recovery time
# -----------------------------

recovery_days = np.where(
    recovered == 1,
    np.random.randint(1, 31, N),
    np.nan
)

# -----------------------------
# 6. Create dataset
# -----------------------------

df = pd.DataFrame({
    "case_id": np.arange(1, N + 1),

    "amount_due": amount_due,

    "days_overdue": days_overdue,

    "monthly_income": monthly_income,

    "monthly_expense": monthly_expense,

    "payment_history_score": payment_history_score,

    "missed_payments": missed_payments,

    "previous_recovery_rate": previous_recovery_rate,

    "contact_success_rate": contact_success_rate,

    "last_payment_days_ago": last_payment_days_ago,

    "account_age_days": account_age_days,

    "reminders_received": reminders_received,

    "digital_engagement": digital_engagement,

    "hardship_flag": hardship_flag,

    "recovered": recovered,

    "recovery_days": recovery_days
})

# -----------------------------
# 7. Save dataset
# -----------------------------

output_path = Path("data") / "recovery_data.csv"

df.to_csv(output_path, index=False)

# -----------------------------
# 8. Display information
# -----------------------------

print("\n====================================")
print("      RECOVERX DATASET CREATED")
print("====================================")

print(f"Total records : {len(df)}")
print(f"Total columns : {len(df.columns)}")

print("\nRecovery distribution:")
print(df["recovered"].value_counts())

print("\nDataset preview:")
print(df.head())

print(f"\nSaved to: {output_path}")
print("====================================")