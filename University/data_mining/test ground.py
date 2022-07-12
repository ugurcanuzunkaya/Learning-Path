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