import tkinter
from tkinter import ttk,messagebox

tk=tkinter.Tk()
tk.title("HelloApp")
tk.geometry("400x400")
tk.config(bg='lightblue')


lbl_fnm=tkinter.Label(text="Firstname:",bg="lightblue",fg="black",font='Courier 15 bold')
#lbl_fnm.place(x=0,y=40)
lbl_fnm.grid(row=0,column=0,sticky='W')

lbl_lnm=tkinter.Label(text="Lastname:",bg="lightblue",fg="black",font='Courier 15 bold')
lbl_lnm.grid(row=1,column=0,sticky='W')

txt_fnm=tkinter.Entry()
txt_fnm.grid(row=0,column=1,sticky='W')

txt_lnm=tkinter.Entry()
txt_lnm.grid(row=1,column=1,sticky='W')

male=tkinter.Radiobutton(value=0,text="Male",bg="lightblue",fg="black",font='Courier 15 bold')
male.grid(row=2,column=0,sticky='W')

female=tkinter.Radiobutton(value=1,text="Female",bg="lightblue",fg="black",font='Courier 15 bold')
female.grid(row=2,column=1,sticky='W')

ch1=tkinter.Checkbutton(text="Gujarati",bg="lightblue",fg="black",font='Courier 15 bold')
ch1.grid(row=3,column=0,sticky='W')

ch2=tkinter.Checkbutton(text="Hindi",bg="lightblue",fg="black",font='Courier 15 bold')
ch2.grid(row=4,column=0,sticky='W')

ch3=tkinter.Checkbutton(text="English",bg="lightblue",fg="black",font='Courier 15 bold')
ch3.grid(row=5,column=0,sticky='W')

city=['Rajkot','Ahmedabad','Baroda','Surat','Jamnagar']
citylist=ttk.Combobox(values=city)
citylist.grid(row=6,column=0)

def btnclick():
    print("Firstname:",txt_fnm.get())
    print("Lastname:",txt_lnm.get())

    #messagebox
    #messagebox.showerror("Error","Something went wrong....")
    #messagebox.showinfo("Success","Signup Successfully!")
    #messagebox.showwarning("Warning!","Your disk is full!")

    messagebox.showinfo("Welcome",f"Firstname:{txt_fnm.get()}\nLastname:{txt_lnm.get()}")


btn=tkinter.Button(text="Submit",font='Courier 15 bold',command=btnclick)
btn.place(x=150,y=250)

tkinter.mainloop()