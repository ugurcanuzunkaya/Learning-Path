import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

# Read the data
titanic = pd.read_csv("titanic.csv")
print(titanic.head(5), "\n")

total = titanic.isnull().sum().sort_values(ascending=False)
percent_1 = titanic.isnull().sum() / titanic.isnull().count() * 100
percent_2 = (round(percent_1, 1)).sort_values(ascending=False)
missing_data = pd.concat([total, percent_2], axis=1, keys=['Total', '%'])
print(missing_data.head(5), "\n")

titanic = titanic.drop(['Cabin', "PassengerId"], axis=1)
titanic.dropna(axis=0, inplace=True)
print(titanic.isnull().sum(), "\n")
print(titanic.columns, "\n")

# Exploratory Data Analysis
# 1- Age and Sex
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 10))
women = titanic[titanic["Sex"] == "female"]
men = titanic[titanic["Sex"] == "male"]
ax = sns.distplot(women[women["Survived"] == 1].Age.dropna(), bins=18, label="survived", ax=axes[0], kde=False)
ax = sns.distplot(women[women["Survived"] == 0].Age.dropna(), bins=40, label="not_survived", ax=axes[0], kde=False)
ax.legend()
ax.set_title("Female")
ax = sns.distplot(men[men["Survived"] == 1].Age.dropna(), bins=18, label="survived", ax=axes[1], kde=False)
ax = sns.distplot(men[men["Survived"] == 0].Age.dropna(), bins=40, label="not_survived", ax=axes[1], kde=False)
ax.legend()
ax.set_title("Male")
plt.show()

# 2- Embarked, Pclass, Sex
FacetGrid = sns.FacetGrid(titanic, row="Embarked", size=4.5, aspect=1.6)
FacetGrid.map(sns.pointplot, "Pclass", "Survived", "Sex", palette=None, order=None, hue_order=None)
FacetGrid.add_legend()
plt.show()

# 3- Pclass
sns.barplot(x="Pclass", y="Survived", data=titanic)
plt.show()

grid = sns.FacetGrid(titanic, col="Survived", row="Pclass", size=2.2, aspect=1.6)
grid.map(plt.hist, "Age", alpha=.5, bins=20)
grid.add_legend()
plt.show()

titanic["Sex"] = pd.to_numeric(titanic["Sex"])
print(titanic["Sex"])
