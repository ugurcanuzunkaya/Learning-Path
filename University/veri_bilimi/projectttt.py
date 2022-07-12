import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import plot_confusion_matrix, classification_report
import pickle
import pycaret.classification as pyc

data = pd.read_csv("ai4i2020.csv")
data['Machine failure'].unique()
data['Machine failure'].value_counts()
data.info()
# check missing value
data.isna().sum()
data['Type'].unique()


def data_preparation(df):
    df = df.copy()

    # drop unnecessary columns
    df = df.drop(["UDI", "Product ID", "TWF", "HDF", "PWF", "OSF", "RNF"], axis=1)

    return df


X = data_preparation(data)
print(X)
print("23123")
print(pyc.setup(data=X, target="Machine failure", train_size=0.8, normalize=True))
print("23123")
print(pyc.compare_models())
print("23123")
best_model = pyc.create_model('lightgbm')
print(best_model)
print("23123")
pyc.evaluate_model(best_model)
tuned_lgbm_model = pyc.tune_model(best_model)
pyc.evaluate_model(tuned_lgbm_model)
pyc.save_model(best_model, "machine_failure")

print(data)
print("23123")


def preprocess_inputs(df):
    df = df.copy()

    # drop unnecessary columns
    df = df.drop(["UDI", "Product ID", "TWF", "HDF", "PWF", "OSF", "RNF"], axis=1)

    # X(features) and y(target/class/labels)
    X = df.drop('Machine failure', axis=1)
    y = df['Machine failure']

    # split
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.8, shuffle=True, random_state=1)

    return X_train, X_test, y_train, y_test


X_train, X_test, y_train, y_test = preprocess_inputs(data)
print(X_train)
print(y_train)
print(len(X_train))
print(len(X_test))
print(len(y_train))
print(len(y_test))

single_transformer = Pipeline(steps=[("encode", OneHotEncoder(sparse=False))])

col_transformer = ColumnTransformer(transformers=[("colencode", single_transformer, ['Type'])], remainder='passthrough')

model = Pipeline(
    steps=[("coltransform", col_transformer), ("scale", StandardScaler()), ("classifier", LogisticRegression())])

clf = model.fit(X_train, y_train)
print(clf)

score = clf.score(X_test, y_test)
print("Model score is:", np.round(score*100), "%")
y_pred = clf.predict(X_test)
print(y_pred)
plot_confusion_matrix(clf, X_test, y_test, labels=clf.classes_)
clr = classification_report(y_test, y_pred, labels=clf.classes_)
print(clr)

# save the model to disk
filename = 'logreg_model.pkl'
pickle.dump(clf, open(filename, 'wb'))