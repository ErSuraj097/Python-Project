from tkinter import*
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage

class Qr_code_Generator:

    def __init__(self,root):

        self.root=root
        self.root.title("QR Generator | Developed By Suraj Yadav")
        self.root.geometry("900x500+200+50")
        self.root.resizable(False ,False)
        self.root.config(bg='wheat')

        title=Label(self.root,text="Government Polytechnic Mau",font=("times new roman",40,"bold"),bg="oldlace",fg="black",anchor="center").place(x=0,y=0,relwidth=1)
        title=Label(self.root,text="UTTAR PRADESH",font=("times new roman",15,"bold"),bg="oldlace",fg="black").place(x=610,y=55)
        title=Label(self.root,text="Student Details QR Generator",font=("times new roman",15),bg="oldlace",fg="black").place(x=50,y=70)

        #==========Employee Details window
        self.var_stu_code=StringVar()
        self.var_stu_name=StringVar()
        self.var_stu_age=StringVar()
        self.var_stu_fathername=StringVar()
        
        stu_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        stu_Frame.place(x=50,y=100,width=500,height=380)

        stu_title=Label(stu_Frame,text="Student Details",font=("Goudy old style",20),fg="white",bg="#043256").place(x=0,y=0,relwidth=1)


        #.........Label.........
        lbl_stu_id=Label(stu_Frame,text="Enrolment No.",font=("times new roman",15),bg="white").place(x=20,y=60)
        lbl_stu_name=Label(stu_Frame,text="Name",font=("times new roman",15),bg="white").place(x=20,y=100)
        lbl_stu_age=Label(stu_Frame,text="Age",font=("times new roman",15),bg="white").place(x=20,y=140)
        lbl_stu_fathername=Label(stu_Frame,text="Father Name",font=("times new roman",15),bg="white").place(x=20,y=180)

        #==========Entry=====
        txt_stu_id=Entry(stu_Frame,font=("times new roman",15),textvariable=self.var_stu_code,bg="lightyellow").place(x=200,y=60)
        txt_stu_name=Entry(stu_Frame,font=("times new roman",15),textvariable=self.var_stu_name,bg="lightyellow").place(x=200,y=100)
        txt_stu_age=Entry(stu_Frame,font=("times new roman",15),textvariable=self.var_stu_age,bg="lightyellow").place(x=200,y=140)
        txt_stu_fathername=Entry(stu_Frame,font=("times new roman",15),textvariable=self.var_stu_fathername,bg="lightyellow").place(x=200,y=180)

        btn_gen=Button(stu_Frame,text="QR Generate",command=self.generate,font=("times new roman",18),bg="#2196f3",fg="white").place(x=90,y=250,width=180,height=30)

        btn_clear=Button(stu_Frame,text="Clear",command=self.clear,font=("times new roman",18),bg="#607d8b",fg="white").place(x=282,y=250,width=120,height=30)

        self.msg=''
        self.lbl_msg=Label(stu_Frame,text=self.msg,font=("times new roman",20),bg="white",fg="green")
        self.lbl_msg.place(x=0,y=310,relwidth=1)

        #==========Employee QR code window
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        qr_Frame.place(x=600,y=100,width=250,height=380)

        qr_title=Label(qr_Frame,text="Student QR Code",font=("Goudy old style",20),fg="white",bg="#043256").place(x=0,y=0,relwidth=1)

        self.qr_code=Label(qr_Frame,text="No QR \ Avaolable",font=("times new roman",15),bg="wheat",bd=1,relief=RIDGE)
        self.qr_code.place(x=35,y=100,width=180,height=180)

        #...............Generate data......
    def clear(self):
        self.var_stu_code.set('')
        self.var_stu_name.set('')
        self.var_stu_age.set('')
        self.var_stu_fathername.set('')
        
        self.msg=""
        self.lbl_msg.config(text=self.msg)
        self.qr_code.config(image='')
        
        #...............Generate data......
    def generate(self):
        if self.var_stu_code.get()==""or self.var_stu_name.get()=="" or self.var_stu_age.get()=="" or self.var_stu_fathername.get()=="":
            self.msg="All Fields Are Required!!!"
            self.lbl_msg.config(text=self.msg,fg="red")
        
        else:
            qr_data=(f"Name : {self.var_stu_code.get()}\nFather Name : {self.var_stu_name.get()}\nAge : {self.var_stu_age.get()}\nMobile No. : {self.var_stu_fathername.get()}")
            qr_code=qrcode.make(qr_data)
            #print(qr_code)
            qr_code=resizeimage.resize_cover(qr_code,[180,180])
            qr_code.save("Student_QR"+str(self.var_stu_code.get())+'.png')
            #...........Qr Code Image Update.....
            self.im=ImageTk.PhotoImage(file="Student_QR"+str(self.var_stu_code.get())+'.png')
            self.qr_code.config(image=self.im)
            
            #............Updati notification.............
            self.msg='QR Generated Successfully!!!'
            self.lbl_msg.config(text=self.msg,fg="green")
        
root=Tk()
obj=Qr_code_Generator(root)
root.mainloop()
