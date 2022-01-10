from smdt import datasets
from smdt import molecular_descriptors
from smdt import regression
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np

data = pd.read_csv('desc.csv')
numeric_cols = data.select_dtypes(exclude='number')
check = data.drop(numeric_cols, axis=1)
H = pd.read_csv('clean_final.csv',delimiter=' ')
y=H['mp']
X=check
import regression

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

model1, y_pred1, metrics1 = regression.fit_Ridge(X_train, X_test, y_train, y_test)
np.save('ypred1',y_pred1)
np.save('metrics1',metrics1

model2, y_pred2, metrics2 = regression.fit_Lasso(X_train, X_test, y_train, y_test)
np.save('ypred2',y_pred2)
np.save('metrics2',metrics2)
model3, y_pred3, metrics3 = regression.fit_ElasticNet(X_train, X_test, y_train, y_test)
np.save('ypred3',y_pred3)
np.save('metrics3',metrics3)
model4, y_pred4, metrics4 = regression.fit_LinearSVR(X_train, X_test, y_train, y_test)
np.save('ypred4',y_pred4)
np.save('metrics4',metrics4)
model5, y_pred5, metrics5 = regression.fit_RandomForestRegressor(X_train, X_test, y_train, y_test)
np.save('ypred5',y_pred5)
np.save('metrics5',metrics5)
