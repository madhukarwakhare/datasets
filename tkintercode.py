from tkinter import *
import joblib
import pickle 
 
def predictGender():
    weight=int(e1.get())
    height=int(e2.get())
    loaded_model=joblib.load(open('finalmodel.pkl','rb'))
    prediction=loaded_model.predict([[weight,height]])
    myText.set(prediction[0])
 
master = Tk()
master.title("Gender Prediction using Height and Weight")
myText=StringVar();
Label(master, text="Enter Weight").grid(row=0, sticky=W)
Label(master, text="Enter Height").grid(row=1, sticky=W)
Label(master, text="The Gender Of a Person is:").grid(row=3, sticky=W)
result=Label(master, text="", textvariable=myText).grid(row=3,column=1, sticky=W)
 
e1 = Entry(master)
e2 = Entry(master)
 
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
 
b = Button(master, text="Predict Gender", command=predictGender)
b.grid(row=0, column=2,columnspan=2, rowspan=2,sticky=W+E+N+S, padx=5, pady=5)
 
 
mainloop()
 
