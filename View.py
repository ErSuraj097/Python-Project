from tkinter import *
from tkinter import messagebox



root=Tk()
root.title("DEVELOPED BY SURAJ YADAV")
root.geometry("700x400+0+0")
#root.config(bg="")
root.resizable(False,False)


def title():

        def clear():
                txt1.delete(0,END)
                txt2.delete(0,END)
                txt3.delete(0,END)
                txt4.delete(0,END)
                txt5.delete(0,END)

                
        def get_data():
                if txt1.get()=="" or txt2.get()=="" or txt3.get()=="" or txt4.get()=="":
                        messagebox.showerror("Error","All Feild Are Required!")
                else:
                        messagebox.showinfo("Success","Registration Successfull!")
                        lbl5.config(text="Name  : "+str(txt1.get()))
                        lbl6.config(text="Father Name  : "+str(txt2.get()))
                        lbl7.config(text="Age  : "+str(txt3.get()))
                        lbl8.config(text="Mobile  : "+str(txt4.get()))
                        lbl9.config(text="Address  : "+str(txt5.get()))

        
        lbl_1=Label(root,text="Registration Form",font=("times new roman",20,"bold"),bg="dodgerblue",fg="white",bd="5",relief=GROOVE).pack(fill = BOTH)
        frame_stu=Frame(root,bg="white").place(x=10,y=60,width=330,height=320)

        lbl=Label(frame_stu,text="Registration Here",font=("times new roman",15,"bold"),bg="dodgerblue",fg="white",bd=5,relief=FLAT).place(x=10,y=60,width=330)

        lbl1=Label(frame_stu,text="Name",font=("times new roman",15),bg="white",fg="black")
        lbl1.place(x=15,y=120)
        lbl2=Label(frame_stu,text="Father Name",font=("times new roman",15),bg="white",fg="black")
        lbl2.place(x=15,y=160)
        lbl3=Label(frame_stu,text="Age",font=("times new roman",15),bg="white",fg="black")
        lbl3.place(x=15,y=200)
        lbl4=Label(frame_stu,text="Mobile",font=("times new roman",15),bg="white",fg="black")
        lbl4.place(x=15,y=240)
        text=Label(frame_stu,text="Address",font=("times new roman",15),bg="white",fg="black")
        text.place(x=15,y=280)

        txt1=Entry(frame_stu,font=("times new roman",15),bg="white",fg="black")
        txt1.place(x=130,y=120)
        txt2=Entry(frame_stu,font=("times new roman",15),bg="white",fg="black")
        txt2.place(x=130,y=160)
        txt3=Entry(frame_stu,font=("times new roman",15),bg="white",fg="black")
        txt3.place(x=130,y=200)
        txt4=Entry(frame_stu,font=("times new roman",15),bg="white",fg="black")
        txt4.place(x=130,y=240)
        txt5=Entry(frame_stu,font=("times new roman",15),bg="white",fg="black")
        txt5.place(x=130,y=280,width=205,height=60)

        btn=Button(frame_stu,text="Submit",font=("times new roman",15,"bold"),command=get_data,bg="dodgerblue",fg="white",cursor="hand2").place(x=65,y=365,width=100,height=30)
        btn=Button(frame_stu,text="Reset",font=("times new roman",15,"bold"),command=clear,bg="red",fg="white",cursor="hand2").place(x=175,y=365,width=100,height=30)

        frame_stu_data=Frame(root,bg="white").place(x=360,y=60,width=330,height=320)
        lbl_details=Label(frame_stu_data,text="Your Data",font=("times new roman",15,"bold"),bg="dodgerblue",fg="white",bd=5,relief=FLAT).place(x=360,y=60,width=330)

        '''lbl=Label(frame_stu_data,text="Name:",font=("times new roman",15),bg="white",).place(x=370,y=120)
        lbl=Label(frame_stu_data,text="FatherName:",font=("times new roman",15),bg="white",).place(x=370,y=160)
        lbl7=Label(frame_stu_data,text="Age:",font=("times new roman",15),bg="white").place(x=370,y=200)
        lbl8=Label(frame_stu_data,text="Mobile:",font=("times new roman",15),bg="white").place(x=370,y=240)
        lbl9=Label(frame_stu_data,text="Addres:",font=("times new roman",15),bg="white").place(x=370,y=280)'''

        lbl5=Label(frame_stu_data,font=("times new roman",15),bg="white",fg="red")
        lbl5.place(x=370,y=120)
        lbl6=Label(frame_stu_data,font=("times new roman",15),bg="white",fg="red")
        lbl6.place(x=370,y=160)
        lbl7=Label(frame_stu_data,font=("times new roman",15),bg="white",fg="red")
        lbl7.place(x=370,y=200)
        lbl8=Label(frame_stu_data,font=("times new roman",15),bg="white",fg="red")
        lbl8.place(x=370,y=240)
        lbl9=Label(frame_stu_data,font=("times new roman",15),bg="white",fg="red")
        lbl9.place(x=370,y=280)


        
                
title()
root.mainloop()
