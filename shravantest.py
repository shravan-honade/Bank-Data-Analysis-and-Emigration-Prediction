from tkinter import *
from PIL import Image,ImageTk
import csv
import random
import os
from tkinter import ttk

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui
import matplotlib.pyplot as plt
#import test


def logdoc(frame,h,w,root,num):			#HOME PAGE , LOGIN AS ANALYST

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("Bank.jpg")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=300,y=0)

    wel=Label(frame,text="Enter Your Login Details",font=("Calibri",20,"bold italic"),foreground = "green")
    wel.pack()
    wel.place(x=485,y=195)

    usr=Label(frame,text="Username",font=("Calibri",15))
    usr.pack()
    usr.place(x=500,y=260)

    pas=Label(frame,text="Password",font=("Calibri",15))
    pas.pack()
    pas.place(x=500,y=310)

    entry1=Entry(frame,font=("Calibri",15))
    entry1.pack()
    entry1.place(x=600,y=260)

    entry2=Entry(frame,show='*',font=("Calibri",15))
    entry2.pack()
    entry2.place(x=600,y=310)
    
    submit=Button(frame, text = 'Submit',font=("Calibri",15),command=lambda:logdoc1(frame,h,w,root,entry1.get(),entry2.get()))
    submit.pack()
    submit.place(x=730,y=360)

    num=0
    
    home=Button(frame, text = 'Back to Home Page',font=("Calibri",15),command=lambda:main(frame,h,w,root))
    home.pack()
    home.place(x=500,y=360)
    
    if(inc==1):
        inc=Label(frame,text="Incorrect Username and Password...Please Try Again",font=("Calibri",12))
        inc.pack()
        inc.place(x=335,y=452)

def logdoc1(frame,h,w,root,username,password):		# SECOND PAGE , LOGIN WINDOW

    if(username=='sinhgad' and password=='bank'):
        inc=0
        logdoc2(frame,h,w,root,inc)
        
    else:
        num=1
        logdoc(frame,h,w,root,num)

def logdoc2(frame,h,w,root,inc):			#EXPLORATORY DATA ANALYSIS AND PREDICTION ANALYSIS

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("Bank.jpg")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=300,y=0)
    
    
   
   
    EDA=Button(frame, text = 'Exlploratory data analysis',font=("Calibri",15),command=lambda:logdoc3(frame,h,w,root))
    EDA.pack()
    EDA.place(x=530,y=270)
    
    EXE=Button(frame, text = 'Prediction analysis',font=("Calibri",15),command=lambda:logdoc10(frame,h,w,root))
    EXE.pack()
    EXE.place(x=530,y=470)
    home=Button(frame, text = 'LOGOUT',font=("Calibri",15),command=lambda:logdoc(frame,h,w,root,0))
    home.pack()
    home.place(x=1100,y=660)


def logdoc3(frame,h,w,root):				#INSIDE EXPLORATORY DATA ANALYSIS

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("Bank.jpg")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=300,y=0)
    
    graph1=Button(frame, text = 'Age',font=("Calibri",15),command=lambda:logdoc4(frame,h,w,root))
    graph1.pack()
    graph1.place(x=570,y=170)
    
    graph4=Button(frame, text = 'Country',font=("Calibri",15),command=lambda:logdoc5(frame,h,w,root))
    graph4.pack()
    graph4.place(x=670,y=270)
    
    graph3=Button(frame, text = 'Gender',font=("Calibri",15),command=lambda:logdoc6(frame,h,w,root))
    graph3.pack()
    graph3.place(x=570,y=370)
    
    graph2=Button(frame, text = 'Has Credit Card',font=("Calibri",15),command=lambda:logdoc7(frame,h,w,root))
    graph2.pack()
    graph2.place(x=670,y=670)
    
    graph5=Button(frame, text = 'Credit score',font=("Calibri",15),command=lambda:logdoc8(frame,h,w,root))
    graph5.pack()
    graph5.place(x=570,y=570)
    
    graph6=Button(frame, text = 'Is Active Member',font=("Calibri",15),command=lambda:logdoc9(frame,h,w,root))
    graph6.pack()
    graph6.place(x=670,y=470)  
    
    home=Button(frame, text = 'Back to previous Page',font=("Calibri",15),command=lambda:logdoc2(frame,h,w,root,0))
    home.pack()
    home.place(x=1100,y=660)

def logdoc4(frame,h,w,root):

   
    os.system('python Graph_Age.py')
    
    
def logdoc5(frame,h,w,root):


    
    os.system('python Country.py')
    
def logdoc6(frame,h,w,root):

    
    os.system('python gender.py')

def logdoc7(frame,h,w,root):

    os.system('python Graph_Credit.py')

def logdoc8(frame,h,w,root):

    
    os.system('python graphd4.py')

def logdoc9(frame,h,w,root):

   
    os.system('python Graph_Active.py')
    
def logdoc10(frame,h,w,root):

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("Bank.jpg")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=300,y=0)
    

   
    
    
    res=Button(frame, text = 'Start Execution',font=("Calibri",15),command=lambda:logdoc11(frame,h,w,root))
    res.pack()
    res.place(x=600,y=450)
    
    
    ana=Button(frame, text = 'Analysis of Neural Network',font=("Calibri",15),command=lambda:logdoc12(frame,h,w,root))
    ana.pack()
    ana.place(x=600,y=300)
    
    
    home=Button(frame, text = 'Back to Previous Page',font=("Calibri",15),command=lambda:logdoc2(frame,h,w,root,0))
    home.pack()
    home.place(x=1100,y=660)
    
    
def logdoc12(frame,h,w,root):

    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("Bank.jpg")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=300,y=0)
    
    hid=Button(frame, text = 'Fluctuate hidden layers',font=("helvetica",15),command=lambda:logdoc13(frame,h,w,root))
    hid.pack()
    hid.place(x=50,y=360)
    
    epo=Button(frame, text = 'Fluctuate epochs',font=("Calibri",15),command=lambda:logdoc14(frame,h,w,root))
    epo.pack()
    epo.place(x=570,y=360)
    
    neu=Button(frame, text = 'Fluctuate neurons',font=("Calibri",15),command=lambda:logdoc15(frame,h,w,root))
    neu.pack()
    neu.place(x=1100,y=360)
    
    home=Button(frame, text = 'Back to Previous Page',font=("Calibri",15),command=lambda:logdoc10(frame,h,w,root))
    home.pack()
    home.place(x=1100,y=660)
    
def logdoc13(frame,h,w,root):
    os.system('python temp3.py')

def logdoc14(frame,h,w,root):
    os.system('python temp4.py ')

def logdoc15(frame,h,w,root):
    os.system('python temp2.py')
    
    
'''def logdoc11(frame,h,w,root):
    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("8.png")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=300,y=0)
    os.system('python test.py')
    
    label = Label(frame,text = test.accuracy,font=("Calibri",15))
    label.pack()
    label.place(x=550,y=330)


    home=Button(frame, text = 'Back to Home Page',font=("Calibri",15),command=lambda:logdoc12(frame,h,w,root))
    home.pack()
    home.place(x=1100,y=660)
'''


#code start here   
root = Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

frame = Frame(root,width=w,height=h)
frame.pack()

def main(frame,h,w,root):
    
    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("Bank.jpg")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=300,y=0)

    num=0
    
    doctor=Button(frame, text = 'Login As Analyst',bg="grey",font=("Corbert",15),command=lambda:logdoc(frame,h,w,root,num))
    doctor.pack()
    doctor.place(x=602,y=470)
    
  

    #cpatient=Button(frame, text = 'Analysis',font=("Calibri",15),command=lambda:analysis(frame,h,w,root,num))
    #cpatient.pack()
    #cpatient.place(x=550,y=360)#
    
    root.mainloop()
    

    
def logdoc11(frame,h,w,root):
    frame.pack_forget()
    frame = Frame(root,width=w,height=h)
    frame.pack()
    
    load=Image.open("Bank.jpg")
    render=ImageTk.PhotoImage(load)
    img=Label(frame,image=render)
    img.image=render
    img.place(x=300,y=0)
    import test
    
    label = Label(frame,text = "Confusion Matrix: "+str(test.cm),font=("Calibri",15))
    label = Label(frame,text = "The accuracy of this model in classsifying the customer is "+str(test.accuracy*100),font=("Calibri",15))
    label.pack()
    label.place(x=360,y=200)
    
    #label = Label(frame,text = str(test.y_pred),font=("Calibri",15))
    #label.pack()
    #label.place(x=550,y=550)
    



    class PandasModel(QtCore.QAbstractTableModel):
    

        def __init__(self, data, parent=None):
            QtCore.QAbstractTableModel.__init__(self, parent)
            self._data = data

        def rowCount(self, parent=None):
            return len(self._data.values)

        def columnCount(self, parent=None):
            return self._data.columns.size
  
        def data(self, index, role=QtCore.Qt.DisplayRole):
            if index.isValid():
                if role == QtCore.Qt.DisplayRole:
                    if(index.column() != 0):
                        return str('%.2f'%self._data.values[index.row()][index.column()])
                    else:
                        return str(self._data.values[index.row()][index.column()])
            return None

        def headerData(self, section, orientation, role):
            if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
                return self._data.columns[section]
            elif orientation == QtCore.Qt.Vertical and role == QtCore.Qt.DisplayRole:
                return str(self._data.index[section])
            return None

        def flags(self, index):
            flags = super(self.__class__,self).flags(index)
            flags |= QtCore.Qt.ItemIsSelectable
            flags |= QtCore.Qt.ItemIsEnabled
            return flags
        
    import pandas as pd
    import numpy as np
    x=test.compare(test.X_testmod,test.y_predmod)
    df = pd.DataFrame(x)
    del df['Row_number']
    app = QtWidgets.QApplication([])
    table = QtWidgets.QTableView()
    mymodel = PandasModel(df)
    table.setModel(mymodel)
    table.show()
    app.exec_() 





    home=Button(frame, text = 'Back to Previous Page',font=("Calibri",15),command=lambda:logdoc10(frame,h,w,root))
    home.pack()
    home.place(x=1100,y=660)
    
    test.drawAccuracy()
    
    







if __name__=="__main__":
    main(frame,h,w,root)
 
   
 
