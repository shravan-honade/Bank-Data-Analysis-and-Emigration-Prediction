
# Part-1 Data Preprocessing

#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the dataset
dataset = pd.read_csv('Churn_Modelling.csv')

X = dataset.iloc[:,3:13].values
y = dataset.iloc[:,13].values


X_mod = pd.DataFrame(X)

X_testmod = X_mod.iloc[8000:,0:14]
X_testmod = pd.DataFrame(X_testmod)

datasetmod = pd.DataFrame(dataset)
datasetmod = datasetmod.iloc[8000:,0:14].values
datasetmod = pd.DataFrame(datasetmod)



#Encoding the categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
labelencoder_X_1 = LabelEncoder()
X[:,1] = labelencoder_X_1.fit_transform(X[:,1])
labelencoder_X_2 = LabelEncoder()
X[:,2] = labelencoder_X_2.fit_transform(X[:,2])

#Creating the dummy variable
onehotencoder = OneHotEncoder(categorical_features =[1])
X = onehotencoder.fit_transform(X).toarray()

#Avoiding the dummy variable trap
X = X[:,1:]



#Splitting the dataset into the Training set and Test Set,#cross validation is repalced by model_selection 
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,test_size = 0.2,random_state = 0)



#Feature Scaling,We need to 100% apply feature scaling in deep learning or neural networks.to ease the calculations
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)


#Part-2 Making the ANN!!!!

import keras
from keras.models import Sequential
from keras.layers import Dense

#Initializing the ANN

classifier = Sequential() # object is nothing but future ann that we are going to build,defining it as the sequence of layers
 
#Adding the input layer  and the first hidden layer

#output_dim is the number of nodes in hidden layer
#there is no thumb rule to decide the numbber on nodes and hidden layer,trial and error ,parameter tuning can be done 
#to  get best results.k-fold validation can also be used
#init is used to initialize the weights of synapses close to zero generally
#input dim - number of independent variables
classifier.add(Dense(output_dim = 6,init ='uniform',activation = "relu",input_dim = 11))
 
#classifier.add(Dense(input_dim = 11,units = 6,kernel_initializer ='uniform',activation = "relu"))
''' first hidden layer and input layer created,input_dim parameter is only needed for first hidden layer 
  because the first hidden layer did not knew how many nodes to expect'''


#Adding the second layer
classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu'))

classifier.add(Dense(output_dim = 6, init = 'uniform', activation = 'relu'))








#Adding the output layer,sigmoid function to get probabilities
classifier.add(Dense(output_dim = 1, init = 'uniform', activation = 'sigmoid'))
'''units = 1 coz we have output as a boolean value since customer will either stay or leave
  Suppose our dependent variable have more than two categories of values then units = no. of categories and 
  activation = stuffed_max'''

#Compiling the ANN
classifier.compile(optimizer = 'adam',loss = 'binary_crossentropy',metrics=['accuracy'])
'''loss = 'binary_crossentropy' since we have binary outcome.if not binary then 'categorical_crossentropy' 
metrics value is just the criterion you choose to evaluate the model,accuracy is generally used,accuracy 
 when the weights are updated after each batch ,the algo uses accuracy criterion to improve the accuracy'''
 
 
 #Fitting the ANN to training set
classifier.fit(X_train,y_train,batch_size = 64,nb_epoch = 60)
'''batch size is the number of observations after which we want to update the weights'''


#Predicting the set results
y_predprob = classifier.predict(X_test)#y_pred is the probabilities that the customer leave the bank

y_predn = (y_predprob > 0.5)
y_pred = pd.DataFrame(y_predn)
y_predmod = y_pred


#Making the Confusion Matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)


correct =  cm[0][0]+cm[1][1]
wrong   =  cm[0][1]+cm[1][0]
accuracy = (cm[0][0]+cm[1][1])/2000

def drawAccuracy():
	labels = 'Correctly Predicted','Wrongly Predicted'
	sizes = [correct,wrong]
	colors = ['gold', 'yellowgreen']
	explode = (0.1, 0.1)  # explode 1st slice
 
# Plot
	plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
	plt.axis('equal')

	plt.title("Model Performance")

	plt.show()
	
	
def compare(X_testmod,y_predmod):
	'''df2 = y_pred.iloc[y_pred[:,0]==True].index
	return df2'''
	X_testmod = X_testmod.assign(y_predmod=y_predmod.values)
	X_testmod = X_testmod.rename(columns={0:'Credit Score',1:'Country',2:'Gender',3:'Age',4:'Tenure',5:'Balance',6:'No. of Products',7:'Has Crd. Card',8:'Is active member',9:'Estimated Salary'})
	X_testmod = X_testmod[X_testmod['y_predmod']==1]
	X_testmod = X_testmod.assign(Row_number=X_testmod.index+1)
	#cols = list(df.columns.values)
	return X_testmod
	
def compare2(datasetmod,y_predmod):
	'''df2 = y_pred.iloc[y_pred[:,0]==True].index
	return df2'''
	datasetmod = datasetmod.assign(y_predmod=y_predmod.values)
	return datasetmod
	

'''cnf_matrix = confusion_matrix(y_test, y_pred)
np.set_printoptions(precision=2)

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Confusion matrix, without normalization')

# Plot normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names, normalize=True,
                      title='Normalized confusion matrix')

plt.show()'''

x=compare2(datasetmod,y_predmod)
df = pd.DataFrame(x)
df=df.rename(columns={1:'Customer ID',2:'Name',3:'Credit Score',4:'Country',5:'Gender',6:'Age',7:'Tenure',8:'Balance',9:'No. of Products',10:'Has Crd. Card',11:'Is Active Member',12:'Estimated Salary'})
del df[13]
df=df[df['y_predmod']==True]

#86.15 accuracy obtained




