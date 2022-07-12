import seaborn as sb
import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv("train.csv", sep=",")
titanic2 = titanic.corr()
heat_map = sb.heatmap(titanic2, xticklabels=False, yticklabels=False, cbar= False, annot=True)
plt.show()
