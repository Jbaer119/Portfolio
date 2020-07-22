from tkinter import *
global encrypt

#msg = input("Message?: ") #The Message
#message = msg.lower()
alphabet='abcdefghijklmnopqrstuvwxyz' #Possible Digits
#key= 9  #Steps
#####################################FUNCTIONS START#################################
def Enc():
    encrypt= '' #encrypt Varible
    Res.delete(0,END)
   
    for i in Msg.get().lower(): #Gets message, and then turns it to lowercase for the next step
        position=alphabet.find(i)
        newposition=(position+int(Key.get()))%26 #Encrpyt Function
        encrypt+=alphabet[newposition]
        
    print("Mode: Encrpt: input:"+Msg.get()+" Output: "+ encrypt + " Key: "+Key.get())
    Res.insert(0,encrypt)
   
def Denc():
    decrypt= '' #Decrypt Varible


    for i in Msg.get().lower():                                  
        position=alphabet.find(i)
        newposition=(position-int(Key.get()))%26 #Decrypt Fuction
        decrypt+=alphabet[newposition]
    Res.delete(0,END)
    Res.insert(0,decrypt)
    print("Mode: Decrypt: input:"+Msg.get()+" Output: "+ decrypt + " Key: "+Key.get())

def Clear():
    Res.delete(0,END)
  
def Clear2():
    Msg.delete(0,END)
####################################FUNCTIONS END###################################
#########TK Main##################
root = Tk()
root.title("Encryption Algo 2")
#########TK Main##################
################GUI PARTS####################################################
Lb1 = Label(root,text="Result") #Results Label
Lb1.grid(row=0,column=0) #Results Label Position
Res = Entry(root,width=35,borderwidth=5) #Results Entry
Res.grid(row=0,column=1,columnspan=3,padx=10,pady=10) #Results Entry Position
Lb2 = Label(root,text="Message") #Message Label
Lb2.grid(row=1,column=0) #Message Label Position
Msg = Entry(root,width=35,borderwidth=5) #Message Entry
Msg.grid(row=1,column=1,columnspan=3,padx=10,pady=10) #Message Entry Position
Lb3=Label(root,text="Key") #Key Label
Lb3.grid(row=2,column=0,columnspan=1) #Key Label Position
Key = Entry(root,width=10,borderwidth=5) #Key Entry 
Key.grid(row=2,column=1) #Key Entry Position
E = Button(root,text="Encrypt",command=Enc) #Encrypt Button
E.grid(row=2,column=2) #Encrypt Button Position
D = Button(root,text="Decrypt",command=Denc) #Decrypt Button
D.grid(row=2,column=3) #Decrypt Button Postion
Cl1 = Button(root,text="Clear",command=Clear) #Clear Result Button
Cl1.grid(row=0,column=4) #Clear Result Button Position
Cl2 = Button(root,text="Clear",command=Clear2) #Clear Message Button
Cl2.grid(row=1,column=4) #Clear Message Button Position
################GUI PARTS######################################################
root.mainloop()