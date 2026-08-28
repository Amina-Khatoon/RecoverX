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

preprocessor = model.named_steps["preprocessing"]

feature_columns = []

for _, _, columns in preprocessor.transformers_:
    if columns is not None:
        feature_columns.extend(columns)


def predict_recovery(data):

    input_data = {}

    for column in feature_columns:

        if column in data:
            input_data[column] = data[column]

        elif column in df.columns:

            if pd.api.types.is_numeric_dtype(df[column]):
                input_data[column] = df[column].median()
            else:
                mode = df[column].mode()

                if len(mode) > 0:
                    input_data[column] = mode.iloc[0]
                else:
                    input_data[column] = None

    input_df = pd.DataFrame([input_data])

    input_df = input_df[feature_columns]

    prediction = int(model.predict(input_df)[0])

    probability = float(model.predict_proba(input_df)[0][1])

    if probability >= 0.75:
        level = "HIGH"
        action = "High Priority Follow-up"

    elif probability >= 0.50:
        level = "MEDIUM"
        action = "Moderate Follow-up + Flexible Plan"

    else:
        level = "LOW"
        action = "Low Priority + Alternative Recovery Strategy"

    return {
        "recovery_probability": round(probability * 100, 2),
        "prediction": (
            "RECOVERY LIKELY"
            if prediction == 1
            else "RECOVERY UNLIKELY"
        ),
        "recovery_level": level,
        "recommended_action": action,
    }  