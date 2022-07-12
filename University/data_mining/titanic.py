import pandas as pd
import matplotlib.pyplot as plt
titanic = pd.read_csv("train.csv", sep=",")
"""
titanic.Pclass.unique() 
titanic['Pclass'].unique()
titanic.iloc[:,2]
titanic.iloc[:,2].unique()
titanic.Sex.value_counts() 
titanic['Sex'].value_counts()
titanic.iloc[:,4].value_counts()
firstsixcol = titanic.iloc[:, 0:6]
firsthundred = titanic.iloc[0:100, [1,4,5]]
firsthundred2 = titanic.loc[0:99, ["Age", "Sex", "Survived"]]
firsthundred3 = titanic.loc[titanic.Survived == 1, :]
firsthundred3.1 = titanic.loc[titanic[Survived] == 1, :]
survived = titanic[titanic["Survived"] == 1]
survived_man = titanic.loc[(titanic["Survived"] == 1) & (titanic["Sex"] == "male")]
survived_man1 = titanic.loc[(titanic["Survived"] == 1) & (titanic["Sex"] == "male"), ["Age", "Sex"]]
survived_female = titanic.loc[(titanic["Survived"] == 1) & (titanic["Sex"] == "female")]
survived_male = titanic.loc[(titanic["Survived"] == 1) & (titanic["Sex"] == "male")]
print("Ortalamar kadın: ", survived_female.Age.mean(), "erkek: ", survived_male.Age.mean())
titanic = titanic.drop("Name",axis=1) sütun yok etme
print(titanic.columns)
name = titanic.pop("Name") sütunu ana veride yok edip pandas serisinde tutma
print(name)
titanic.isnull().sum(axis=0)
titanic_full = titanic.loc[titanic.isnull().any(axis=1) == False]
print(titanic_full.isnull().any().any())
titanic.corr()

plt.figure("Cinsiyet dağılımı")
plt.hist(titanic.Sex, histtype="bar", color="red", label="sex")
plt.xlabel("Sex")
plt.ylabel("Passenger number")
plt.title("Passenger")
plt.show()

plt.figure("Cinsiyet dağılımı") ??????????
sex = titanic.loc[titanic.Survived == 1,:]
plt.hist(sex.Survived, histtype="bar", color="blue,red")
plt.xlabel("Sex")
plt.ylabel("Passenger number")
plt.title("Passenger")
plt.show()

titanic.boxplot(column="Age", by="Survived")    all
plt.show()

titanic.loc[titanic["Sex"]=="female",:].boxplot(column="Age", by="Survived")    female
plt.show()

titanic.loc[titanic["Sex"]=="male",:].boxplot(column="Age", by="Survived")  male
plt.show()

titanic.boxplot(column="Fare", by="Survived")
plt.show()

plt.scatter(titanic.Age, titanic.Fare, color="blue", marker="x")
plt.show()

plt.scatter(titanic.loc[titanic.Survived == 1, :].Age, titanic.loc[titanic.Survived == 1, :].Fare, color="blue",
            marker="x")
plt.show()

plt.scatter(titanic.loc[titanic.Survived == 1, :].Age, titanic.loc[titanic.Survived == 1, :].Fare, color="blue",
            marker="x")
plt.scatter(titanic.loc[titanic.Survived == 0, :].Age, titanic.loc[titanic.Survived == 0, :].Fare, color="red",
            marker="x")
plt.show()

"""
plt.scatter(titanic.loc[titanic.Survived == 1, :].Age, titanic.loc[titanic.Survived == 1, :].Fare, color="blue",
            marker="x")
plt.scatter(titanic.loc[titanic.Survived == 0, :].Age, titanic.loc[titanic.Survived == 0, :].Fare, color="red",
            marker="x")
plt.show()
