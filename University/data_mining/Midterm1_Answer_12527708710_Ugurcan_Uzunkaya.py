import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
corona = pd.read_csv("patient.csv", sep=",")
age=[]
corona["birth_year"].replace("", np.nan, inplace=True)
corona.dropna(subset=["birth_year"], inplace=True)
for i in range(len(corona.iloc[1:, 2])):
    c = 2020 - int(corona.iloc[i, 2])
    age.append(c)
agenp = np.array(age).reshape(1, len(age))
agenp = agenp.transpose()
agedf = pd.DataFrame(agenp, columns=list("a"))
corona["age"] = agedf
corona.boxplot(column="age", by="state")
plt.show()
corona.loc[corona["sex"] == "female", :].boxplot(column="age", by="state")
plt.show()
corona.loc[corona["sex"] == "male", :].boxplot(column="age", by="state")
plt.show()
corona["sex"].replace("", np.nan, inplace=True)
corona.dropna(subset=["sex"], inplace=True)
plt.hist(corona.sex, histtype="bar", color="red", label="sex")
plt.xlabel("sex")
plt.ylabel("count")
plt.title("Distribution of patients according to their gender")
plt.show()
coronadeceased = corona.loc[corona["state"]=="deceased",:]
plt.hist(coronadeceased.sex, histtype="bar", color="blue", label="Deceased_Sex")
plt.xlabel("sex")
plt.ylabel("count")
plt.title("Distribution of patients, whose state is deceased, according to their gender")
plt.show()