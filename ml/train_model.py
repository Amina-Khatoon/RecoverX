import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ==========================================
# 1. LOAD DATASET
# ==========================================

data_path = "data/recovery_data.csv"

df = pd.read_csv(data_path)

print("\n==============================")
print("DATASET LOADED")
print("==============================")

print("Shape:", df.shape)
print("\nColumns:")
print(df.columns.tolist())

# ==========================================
# 2. REMOVE UNNECESSARY COLUMNS
# ==========================================

# Completely empty columns remove
df = df.dropna(axis=1, how="all")

# ==========================================
# 3. TARGET
# ==========================================

target = "recovered"

if target not in df.columns:
    raise ValueError("Target column 'recovered' not found!")

X = df.drop(columns=[target])
y = df[target]

print("\nTarget distribution:")
print(y.value_counts())

# ==========================================
# 4. IDENTIFY FEATURES
# ==========================================

numeric_features = X.select_dtypes(
    include=["int64", "float64", "int32", "float32"]
).columns.tolist()

categorical_features = X.select_dtypes(
    include=["object", "category", "bool"]
).columns.tolist()

print("\nNumeric features:")
print(numeric_features)

print("\nCategorical features:")
print(categorical_features)

# ==========================================
# 5. PREPROCESSING
# ==========================================

numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median"))
])

categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

preprocessor = ColumnTransformer([
    ("numeric", numeric_pipeline, numeric_features),
    ("categorical", categorical_pipeline, categorical_features)
])

# ==========================================
# 6. MACHINE LEARNING MODEL
# ==========================================

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    class_weight="balanced"
)

pipeline = Pipeline([
    ("preprocessing", preprocessor),
    ("model", model)
])

# ==========================================
# 7. TRAIN / TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\nTraining samples:", len(X_train))
print("Testing samples:", len(X_test))

# ==========================================
# 8. TRAIN MODEL
# ==========================================

print("\nTraining AI model...")

pipeline.fit(X_train, y_train)

print("Model training completed!")

# ==========================================
# 9. PREDICTION
# ==========================================

y_pred = pipeline.predict(X_test)

# ==========================================
# 10. EVALUATION
# ==========================================

accuracy = accuracy_score(y_test, y_pred)

print("\n==============================")
print("MODEL RESULTS")
print("==============================")

print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# ==========================================
# 11. SAVE MODEL
# ==========================================

model_path = "ml/recovery_model.pkl"

joblib.dump(pipeline, model_path)

print("\n==============================")
print("MODEL SAVED")
print("==============================")
print("Saved to:", model_path)