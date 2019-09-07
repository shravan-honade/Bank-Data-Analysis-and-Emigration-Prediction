import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt


M=0
F=0

df=pd.read_csv("Churn_Modelling.csv")

nation=df['Gender']

for i in nation:
	if(i=='Female'):
		F=F+1
	else:
		M=M+1		
		 
# Data to plot
labels = 'Male', 'Female'
sizes = [M,F]
colors = ['gold', 'yellowgreen']
explode = (0.1, 0.1)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.title('Gender Distribution')
plt.show()
