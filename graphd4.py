import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt




high=0
average=0
low=0

df=pd.read_csv("Churn_Modelling.csv")

credit=df['CreditScore']
print(credit.median())

for i in credit:
	if(i<500):
		low=low+1
	elif(i<650):
		average=average+1
	else:
		high = high+1
		
		
# Data to plot
labels = 'High Credit', 'Average Credit', 'Low Credit'
sizes = [low,average,high]
colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0.1, 0.1, 0.1)  #explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.title("Credit Card Score distribution")
plt.show()




