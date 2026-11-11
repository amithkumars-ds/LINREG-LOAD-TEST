import numpy as np
import pandas as pd

data = pd.read_csv("data/Housing.csv") # loading data

# sanity check
# print(data.columns[data.isna().any()])
# print(data.duplicated())

# data segregation 
X = data["area"].values.reshape(-1,1)
y = data["price"].values

# data splitting
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,
                                                    test_size=0.2,
                                                    random_state=42)


# train the model on data
from sklearn.linear_model import LinearRegression
lr_model = LinearRegression()
print(f"[INFO] Model training started...")
lr_model.fit(X_train, y_train)
print(f"[INFO] Model training completed...")


# evaluate the model
from sklearn.metrics import mean_absolute_error, r2_score
y_pred = lr_model.predict(X_test)
mae = round(mean_absolute_error(y_test,y_pred),2)
r2 = round(r2_score(y_test,y_pred),2)
evaluation_metrics = {
        "mae": mae,
        "r2": r2
        }
print(evaluation_metrics)


# serialize the model
import joblib
joblib.dump(lr_model, "lr_model.joblib")
print(f"[INFO] Model saved to disk...")
