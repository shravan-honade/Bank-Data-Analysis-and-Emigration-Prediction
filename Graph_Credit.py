import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

One=0
Two=0
Three=0

df=pd.read_csv("Churn_Modelling.csv")

products=df['HasCrCard']

for i in products:
    if(i==1):
        One=One+1
    else:
        Two=Two+1

# Data to plot
labels = 'YES','NO'
sizes = [One,Two]
colors = ['gold', 'yellowgreen']
explode = (0.1, 0.1)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.title('Credit Card Distribution')


plt.show()
