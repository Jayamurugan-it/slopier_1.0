import pandas as pd
from slopier import Slopier

# Load CSV
df = pd.read_csv("data.csv")
df = df.sort_values("x")

x_train = df["x"]
y_train = df["y"]

# Train Slopier
model = Slopier(x_train, y_train)

# Predict
x_test = pd.Series([3.2, 7.5, 12.1])
y_pred_df = model.predict(x_test)
print(y_pred_df)