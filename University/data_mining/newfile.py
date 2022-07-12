import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import rcParams

titanic = pd.read_csv("train.csv", sep=",")
rcParams['figure.figsize'] = 15, 6
plt.figure(figsize=(14, 12))
sns.heatmap(titanic.astype(float).corr(), linewidths=0.1, square=True, linecolor='white', annot=True)
plt.show()
