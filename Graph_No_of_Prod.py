import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

One=0
Two=0
Three=0
Four=0

df=pd.read_csv("Churn_Modelling.csv")

products=df['NumOfProducts']

for i in products:
    if(i==1):
        One=One+1
    elif(i==2):
        Two=Two+1
    elif(i==3):
        Three=Three+1
    else:
        Four=Four+1

# Data to plot
labels = 'NOP 1','NOP 2','NOP 3','NOP 4'
sizes = [One,Two,Three,Four]
colors = ['gold', 'yellowgreen', 'lightcoral','red']
explode = (0.1, 0.1, 0.1,0.1)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.title('Number of Products Distribution')
plt.show()
