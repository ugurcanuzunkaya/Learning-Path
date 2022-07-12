import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

df_deneme = pd.read_csv("housing.data", sep="\s+")

print(df_deneme.isnull().sum())

sns.set(rc={'figure.figsize': (9, 8)})
sns.distplot(df_deneme["MEDV"])

corr_matrix = df_deneme.corr().round(2)

# sns.set(rc={'figure.figsize': (15,10)})
# sns.heatmap(data=corr_matrix, annot=True)

train_set1 = corr_matrix["MEDV"].loc[abs(corr_matrix["MEDV"]) >= 0.5]
print(train_set1)
train_set2 = df_deneme[train_set1.index]
print(train_set2)

X = pd.DataFrame(np.c_[train_set2["RM"], train_set2["LSTAT"]], columns=["LSTAT", "RM"])
Y = train_set2["MEDV"]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=5)

linear = LinearRegression()
linear.fit(X_train, Y_train)

y_train_predict = linear.predict(X_train)
rmsetrain = np.sqrt(mean_squared_error(Y_train, y_train_predict))
r2train = r2_score(Y_train, y_train_predict)
print("model performance on training set", "RMSE:", rmsetrain, "R2:", r2train)

y_test_predict = linear.predict(X_test)
rmsetest = np.sqrt(mean_squared_error(Y_test, y_test_predict))
r2test = r2_score(Y_test, y_test_predict)
print("model performance on test set", "RMSE:", rmsetest, "R2:", r2test)


plt.plot(X_train, Y_train, ".")
plt.plot(X_train, y_train_predict, "*")

plt.show()

plt.plot(X_test, Y_test, ".")
plt.plot(X_test, y_test_predict, "*")
plt.show()