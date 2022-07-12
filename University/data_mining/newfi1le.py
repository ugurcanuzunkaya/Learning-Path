import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
titanic=pd.read_csv('train.csv',sep=',')
kıyas_titanic = titanic.drop(['PassengerId','Name','Ticket','Cabin'], axis = 1)
corr = kıyas_titanic.corr()
sns.heatmap(corr)
plt.show()