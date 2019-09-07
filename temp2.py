import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt



df=pd.read_excel("TEST2.xlsx")

list1 = df.Efficiency
list2 = df["No. of Neurons"]
plt.plot(list2,list1)
plt.xlabel("No. of Neurons")
plt.ylabel("Accuracy")


plt.show()
