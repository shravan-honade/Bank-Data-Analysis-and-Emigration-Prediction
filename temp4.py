import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


df=pd.read_excel("TEST3.xlsx")

list3 = df.Efficiency
list4 = df["No_of_Epochs"]
plt.plot(list4,list3)
plt.xlabel("No. of Epochs")
plt.ylabel("Accuracy")
plt.show()
