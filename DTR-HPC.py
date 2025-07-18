import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
dataset = pd.read_csv("C:/Users/DELL/Downloads/sample_hpc_jobs.csv")
le_account = LabelEncoder()
dataset['Account'] = le_account.fit_transform(dataset['Account'])
dataset = pd.get_dummies(dataset, columns=['QOS'], prefix='QOS')
features = ['Account', 'ReqMem', 'Timelimit', 'ReqNodes', 'ReqCPUS'] + [col for col in dataset.columns if col.startswith('QOS')]
# Predicting Memory Usage 
X = dataset[features].values
y_memory = dataset['MaxRSS'].values
X_train_mem, X_test_mem, y_train_mem, y_test_mem = train_test_split(X, y_memory, test_size=0.2, random_state=42)
# Training for Memory Prediction
mem_model = DecisionTreeRegressor(random_state=42)
mem_model.fit(X_train_mem, y_train_mem)
# Test and evaluate memory prediction
y_pred_mem = mem_model.predict(X_test_mem)
print("Memory Prediction Results:")
print("R2 Score:", r2_score(y_test_mem, y_pred_mem))
print("RMSE:", np.sqrt(mean_squared_error(y_test_mem, y_pred_mem)))
plt.scatter(y_test_mem, y_pred_mem, color='blue')
plt.plot([y_test_mem.min(), y_test_mem.max()], [y_test_mem.min(), y_test_mem.max()], 'k--', lw=2)
plt.xlabel('Actual MaxRSS (GB)')
plt.ylabel('Predicted MaxRSS (GB)')
plt.title('Actual vs Predicted Memory Usage')
plt.show()
# Predicting CPU Time (CPUTimeRAW)
y_time = dataset['CPUTimeRAW'].values
X_train_time, X_test_time, y_train_time, y_test_time = train_test_split(X, y_time, test_size=0.2, random_state=42)
# Train  for Time Prediction
time_model = DecisionTreeRegressor(random_state=42)
time_model.fit(X_train_time, y_train_time)
# Test and evaluate time prediction
y_pred_time = time_model.predict(X_test_time)
print("\nTime Prediction Results:")
print("R2 Score:", r2_score(y_test_time, y_pred_time))
print("RMSE:", np.sqrt(mean_squared_error(y_test_time, y_pred_time)))
plt.scatter(y_test_time, y_pred_time, color='green')
plt.plot([y_test_time.min(), y_test_time.max()], [y_test_time.min(), y_test_time.max()], 'k--', lw=2)
plt.xlabel('Actual CPUTimeRAW (seconds)')
plt.ylabel('Predicted CPUTimeRAW (seconds)')
plt.title('Actual vs Predicted CPU Time')
plt.show()
