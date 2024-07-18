import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Reading Data
data = pd.read_csv("your_dataset.csv")

# Data preprocessing
# ...(Execute data cleaning, feature selection, feature encoding, data segmentation and other operations as needed)

# Define features and target variables
features = data[["Prompt", "Model", "isSeq"]]
target_sum = data["SUM"]
target_mem = data["MEM Change"]
target_utilization = data["Average GPU Utilization(%)"]

# Data segmentation
X_train, X_test, y_sum_train, y_sum_test, y_mem_train, y_mem_test, y_utilization_train, y_utilization_test = train_test_split(
    features, target_sum, target_mem, target_utilization, test_size=0.2, random_state=42
)

# Define and train a linear regression model for SUM
sum_model = LinearRegression()
sum_model.fit(X_train, y_sum_train)

# Define and train a linear regression model for MEM changes
mem_model = LinearRegression()
mem_model.fit(X_train, y_mem_train)

# Define and train a linear regression model for Average GPU Utilization(%)
utilization_model = LinearRegression()
utilization_model.fit(X_train, y_utilization_train)

# Predict
sum_predictions = sum_model.predict(X_test)
mem_predictions = mem_model.predict(X_test)
utilization_predictions = utilization_model.predict(X_test)

# Evaluating the Model
sum_mse = mean_squared_error(y_sum_test, sum_predictions)
mem_mse = mean_squared_error(y_mem_test, mem_predictions)
utilization_mse = mean_squared_error(y_utilization_test, utilization_predictions)

print("SUM prediction mean square error:", sum_mse)
print("MEM Change prediction mean square error:", mem_mse)
print("Average GPU Utilization(%) prediction mean square error:", utilization_mse)
