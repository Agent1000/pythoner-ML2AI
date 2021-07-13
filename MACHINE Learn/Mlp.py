import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from  sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

dataset = pd.read_csv("C:\Users\A C E R\Desktop\python basic to AI\pythoner-ML2AI\MACHINE Learn\Weather.csv")

x = dataset["MinTemp"].values.reshape(-1,1)
y = dataset["MaxTemp"].values.reshape(-1,1)

x_train,x_test,y_test,y_train = train_test_split(x,y,test_size=0.3,random_state=0)

model = LinearRegression()
model.fit(x_train,y_train)

y_pred = model.predict(x_test)

df=pd.DataFrame({'Actually':y_test.flatten(),'Predicted':y_pred.flatten()})

print("MAE = ",metrics.mean_absolute_error(y_test,y_pred))
print("MSE = ",metrics.mean_squared_error(y_test,y_pred))
print("RMSE = ",np.sqrt(metrics.mean_squared_error(y_test,y_pred))
print("Score = ",metrics.r2_score(y_test,y_pred))





