import tkinter
from tkinter import ttk,messagebox

screen=tkinter.Tk()
screen.title("FirstApp")
screen.geometry('400x500')
screen.config(background='lightblue')

#lbl_fnm=tkinter.Label(text="Firstname").pack()
#lbl_fnm=tkinter.Label(text="Lastname").pack()

"""lbl_fnm=tkinter.Label(text="Firstname").place(x=0,y=0)
lbl_fnm=tkinter.Label(text="Lastname").place(x=0,y=30)"""

lbl_fnm=tkinter.Label(text="Firstname:",bg='lightblue',font='Bahnschrift 15',fg='red').grid(row=0,column=0)
lbl_fnm=tkinter.Label(text="Lastname:",bg='lightblue',font='Bahnschrift 15',fg='red').grid(row=1,column=0)

txt_fnm=tkinter.Entry().grid(row=0,column=1)
txt_lnm=tkinter.Entry().grid(row=1,column=1)

male=tkinter.Radiobutton(text='Male',value=0,font='Bahnschrift 15',fg='red',bg='lightblue').grid(row=2,column=0,sticky='W')
female=tkinter.Radiobutton(text='Female',value=1,font='Bahnschrift 15',fg='red',bg='lightblue').grid(row=2,column=1,sticky='W')

ch1=tkinter.Checkbutton(text="Python",font='Bahnschrift 15',fg='red',bg='lightblue').grid(row=3,column=0,sticky='W')
ch2=tkinter.Checkbutton(text="PHP",font='Bahnschrift 15',fg='red',bg='lightblue').grid(row=4,column=0,sticky='W')
ch3=tkinter.Checkbutton(text="JAVA",font='Bahnschrift 15',fg='red',bg='lightblue').grid(row=5,column=0,sticky='W')
ch4=tkinter.Checkbutton(text="Node",font='Bahnschrift 15',fg='red',bg='lightblue').grid(row=6,column=0,sticky='W')

city=['Ahmedabad','Baroda','Surat','Jamnagar','Rajkot','Junagadh']
ttk.Combobox(values=city).grid(row=7,column=0,sticky='W')

def btnclick():
    #print("Button Clickd!")
    #messagebox.askokcancel(title="Welcome",message="This is MSGbox!")
    #messagebox.askyesnocancel(title="Welcome",message="This is MSGbox!")
    #messagebox.showerror(title="Error",message="Something went wrong...Try again!")
    #messagebox.showinfo(title="Success",message="Your data has been saved!")
    messagebox.showwarning(title="Warning",message="Your disk is full!")


tkinter.Button(command=btnclick,text="Submit",font='Bahnschrift 15',fg='red').place(x=150,y=300)
screen.mainloop()

