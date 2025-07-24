import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error
import matplotlib.pyplot as plt
df = pd.read_csv("/content/dcgm.csv")
#Data preprocessing
df = df.drop(columns=["Node", "id_job"]) #Drop non numeric columns
df = df[(df["totalexecutiontime_sec"] > 0) & (df["maxgpumemoryused_bytes"] > 0)]
df = df.dropna()  #Drop rows with zero or missing execution time
X = df.drop(columns=["totalexecutiontime_sec", "maxgpumemoryused_bytes"]).values
y_time = df["totalexecutiontime_sec"].values
X_train_time, X_test_time, y_train_time, y_test_time = train_test_split(X, y_time, test_size=0.2, random_state=42)

#PART1: predicting CPUTimeRAW i.e amount of cpu time required by the job
time_model = DecisionTreeRegressor(random_state=42)
time_model.fit(X_train_time, y_train_time)
y_pred_time = time_model.predict(X_test_time)
print("Predicting CPUTimeRAW")
print("R2 Score:", r2_score(y_test_time, y_pred_time))
print("RMSE:", np.sqrt(mean_squared_error(y_test_time, y_pred_time)))
plt.scatter(y_test_time, y_pred_time, color='green')
plt.plot([y_test_time.min(), y_test_time.max()], [y_test_time.min(), y_test_time.max()], 'k--', lw=2)
plt.xlabel('Actual Time(sec)')
plt.ylabel('Predicted Time(sec)')
plt.title('Actual time vs Predicted time')
plt.show()

#PART 2: Predicting MaxRSS i.e amount of physical memory required by the job
y_mem = df["maxgpumemoryused_bytes"].values
X_train_mem, X_test_mem, y_train_mem, y_test_mem = train_test_split(X, y_mem, test_size=0.2, random_state=42)
mem_model = DecisionTreeRegressor(random_state=42)
mem_model.fit(X_train_mem, y_train_mem)
#memory prediction
y_pred_mem = mem_model.predict(X_test_mem)
print("Predicting MaxRSS:")
print("R2 score:", r2_score(y_test_mem, y_pred_mem))
print("Root Mean Square Error", mean_squared_error(y_test_mem, y_pred_mem))

plt.scatter(y_test_mem, y_pred_mem, color='blue')
plt.plot([y_test_mem.min(), y_test_mem.max()], [y_test_mem.min(), y_test_mem.max()], 'k--', lw=2)
plt.xlabel('Actual GPU Memory Used (bytes)')
plt.ylabel('Predicted GPU Memory Used (bytes)')
plt.title('Actual vs Predicted GPU Memory Usage')
plt.show()
