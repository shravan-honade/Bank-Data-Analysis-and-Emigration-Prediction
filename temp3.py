import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


df=pd.read_excel("TEST1.xlsx")

list3 = df.Efficiency
list4 = df["hidden_layers"]
plt.plot(list4,list3)
plt.xlabel("No. of Hidden layers")
plt.ylabel("Accuracy")
plt.show()
