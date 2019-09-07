import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

S=0
G=0
F=0

df=pd.read_csv("Churn_Modelling.csv")

nation=df['Geography']

for i in nation:
	if(i=='France'):
		F=F+1
	elif(i=='Germany'):
		G=G+1
	else:
		S=S+1		
		 
# Data to plot
labels = 'France', 'Germany', 'Spain'
sizes = [F,G,S]
colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0.1, 0.1, 0)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.title('Country Distribution')
plt.show()
