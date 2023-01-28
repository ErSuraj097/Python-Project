from tkinter import*
import time
import datetime
import calendar

def digital_clock():
    root=Tk()
    root.title("DIGITAL CLOCK | DEVELOPED BY SURAJ YADAV ")
    root.geometry("1350x700+0+0")
    root.config(bg="#081923")

    def clock():

        #........Date........

        dd=str(time.strftime("%d"))
        mm=int(time.strftime("%m"))
        mm=calendar.month_name[mm]
        yy=(datetime.datetime.now())
        #print(dd,mm,yy)
        lbl_dd.config(text=dd)
        lbl_mm.config(text=str(mm))
        lbl_yy.config(text=str(yy.year))
        #.......................................
        
        #..........Time.....
        h=str(time.strftime("%H"))
        m=str(time.strftime("%M"))
        s=str(time.strftime("%S"))
        
        
        if int(h)>12 and int(m)>0:
            lbl_noon.config(text="PM")
                        
        if int(h)>12:
            h=str(int(int(h)/12))
    
        #print(h,m,s)
        lbl_hr.config(text=h)
        lbl_min.config(text=m)
        lbl_sec.config(text=s)

        lbl_hr.after(200,clock)

        
    #..........Time_Hour.........
    lbl_hr=Label(root,text="12",font=("times new roman",50,"bold"),bg="#087587",fg="white")
    lbl_hr.place(x=350,y=200,width=150,height=150)
    lbl_h2=Label(root,text="HOUR",font=("times new roman",20,"bold"),bg="#087587",fg="white")
    lbl_h2.place(x=350,y=360,width=150,height=50)

    #..........Date__Day..........
    lbl_dd=Label(root,text="DAY",font=("times new roman",20,"bold"),bg="#087587",fg="white")
    lbl_dd.place(x=350,y=420,width=150,height=50)

    #...........Time_Minute........
    lbl_min=Label(root,text="12",font=("times new roman",50,"bold"),bg="#008EA4",fg="white")
    lbl_min.place(x=520,y=200,width=150,height=150)
    lbl_min2=Label(root,text="MINUTE",font=("times new roman",20,"bold"),bg="#008EA4",fg="white")
    lbl_min2.place(x=520,y=360,width=150,height=50)

    #................Date__Month.........
    lbl_mm=Label(root,text="MONTH",font=("times new roman",20,"bold"),bg="#008EA4",fg="white")
    lbl_mm.place(x=520,y=420,width=150,height=50)

    #..................Time_Second...........
    lbl_sec=Label(root,text="12",font=("times new roman",50,"bold"),bg="#DF002A",fg="white")
    lbl_sec.place(x=690,y=200,width=150,height=150)
    lbl_sec2=Label(root,text="SECOND",font=("times new roman",20,"bold"),bg="#DF002A",fg="white")
    lbl_sec2.place(x=690,y=360,width=150,height=50)

    #........................Date__Year...........
    lbl_yy=Label(root,text="YEAR",font=("times new roman",20,"bold"),bg="#DF002A",fg="white")
    lbl_yy.place(x=690,y=420,width=150,height=50)

    lbl_noon=Label(root,text="AM",font=("times new roman",50,"bold"),bg="#DF002A",fg="white")
    lbl_noon.place(x=860,y=200,width=150,height=150)
    lbl_noon2=Label(root,text="NOON",font=("times new roman",20,"bold"),bg="#DF002A",fg="white")
    lbl_noon2.place(x=860,y=360,width=150,height=50)

    lbl_c_date=Label(root,text="C_DATE",font=("times new roman",20,"bold"),bg="#DF002A",fg="white")
    lbl_c_date.place(x=860,y=420,width=150,height=50)

    clock()


    root.mainloop()
digital_clock()
