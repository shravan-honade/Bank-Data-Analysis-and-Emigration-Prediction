import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt

One=0
Two=0
Three=0

df=pd.read_csv("Churn_Modelling.csv")

products=df['Age']

for i in products:
    if(i>=19 and i<=32):
        One=One+1
    elif(i>=33 and i<=50):
        Two=Two+1
    else:
        Three=Three+1

# Data to plot
labels = 'Teen','Adults','Senior'
sizes = [One,Two,Three]
colors = ['gold', 'yellowgreen','red']
explode = (0.1, 0.1,0.1)  # explode 1st slice
 
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.title('Age Distribution')



plt.show()
