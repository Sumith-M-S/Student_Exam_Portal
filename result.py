from tkinter import *
from PIL import Image,ImageTk #pip intall pillow
from tkinter import ttk,messagebox
import sqlite3
class resultClass:
    def __init__(self,root):
        self.root=root
        self.root.title("CampusCore Pro Comprehensive Academic Records and Results Processing Platform")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        #***Titile****
        title=Label(self.root,
                    text="Add Student Results",
                    font=("goudy old style",20,"bold"),
                    bg="orange",fg="#262626"
                    )
        title.place(x=10,y=15,relwidth=1,height=50)
        #******weights****
        #****variables***
        self.var_roll=StringVar()
        self.var_name=StringVar()
        self.var_course=StringVar()
        self.var_marks=StringVar()
        self.var_full_marks=StringVar()
        self.rool_list=[]
        self.fetch_roll()
        
        lbl_select=Label(self.root,text="Select Student",font=("goudy old style",20,"bold"),bg="white").place(x=50,y=105)
        lbl_name=Label(self.root,text="Name",font=("gody old style",20,"bold"),bg="white").place(x=50,y=155)
        lbl_course=Label(self.root,text="Course",font=("gody old style",20,"bold"),bg="white").place(x=50,y=205)
        lbl_full_Marks=Label(self.root,text="Full_Marks",font=("gody old style",20,"bold"),bg="white").place(x=50,y=255)
        lbl_Marks_obtained=Label(self.root,text="Marks_obtained",font=("gody old style",20,"bold"),bg="white").place(x=50,y=305)

        self.txt_student=ttk.Combobox(self.root,
                    textvariable=self.var_roll,values=self.rool_list,
                    font=("goudy old style",15,"bold"),
                    state="readonly",justify=CENTER
                    )
        self.txt_student.place(x=280,y=100,width=200)
        self.txt_student.set("Select")
        btn_Search=Button(self.root,text="Search",font=("goudy old style",15,"bold"),bg="#6f25ca",fg="white",cursor="hand2",command=self.search).place(x=500,y=100,width=120,height=28)
        txt_name=Entry(self.root,
                    textvariable=self.var_name,
                    font=("goudy old style",15,"bold"),
                    bg="lightyellow",state='readonly'
                    ).place(x=280,y=160,width=340)
        txt_course=Entry(self.root,
                    textvariable=self.var_course,
                    font=("goudy old style",15,"bold"),
                    bg="lightyellow",state='readonly'
                    ).place(x=280,y=209,width=340)
        txt_marks=Entry(self.root,
                    textvariable=self.var_marks,
                    font=("goudy old style",15,"bold"),
                    bg="lightyellow"
                    ).place(x=280,y=260,width=340)
        txt_full_marks=Entry(self.root,
                    textvariable=self.var_full_marks,
                    font=("goudy old style",15,"bold"),
                    bg="lightyellow"
                    ).place(x=280,y=310,width=340)

#button****

        btn_add=Button(self.root,text="Submit",font=("times new roman",15),bg="lightgreen",activebackground="lightgreen",cursor="hand2",command=self.add).place(x=300,y=420,width=120,height=35)
        btn_clear=Button(self.root,text="Clear",font=("times new roman",15),bg="lightgray",activebackground="white",cursor="hand2",command=self.clear).place(x=430,y=420,width=120,height=35)
#image***
        self.bg_img=Image.open("image/logo.jpg")
        self.bg_img=self.bg_img.resize((500,300))
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg=Label(self.root,image=self.bg_img).place(x=650,y=100)
        
        
#*********************
    def fetch_roll(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            cur.execute("select roll from student")
            rows=cur.fetchall()
            
            if len(rows)>0:
                for row in rows:
                    self.rool_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
            
    def search(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            cur.execute("select name,course from student where roll=?",(self.var_roll.get(),))
            row=cur.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error","NO RECORD FOUND",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error","No record found",parent=self.root)
            
#**************
    def add(self):
        con=sqlite3.connect(database="RMS.db")
        cur=con.cursor()
        try:
            if self.var_name.get()=="":
                messagebox.showerror("Error","Please search student record",parent=self.root)
            else:
                cur.execute("select*from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
                row=cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error","result already Present",parent=self.root)
                else:
                    per=(int(self.var_marks.get())*100/int(self.var_full_marks.get()))
                    cur.execute("insert into result(roll,name,course,marks_obtained,full_marks,percentage)values(?,?,?,?,?,?)",
                                (self.var_roll.get(),
                                 self.var_name.get(),
                                 self.var_course.get(),
                                 self.var_marks.get(),
                                 self.var_full_marks.get(),
                                 str(per)
                                ))
                    
                    con.commit()
                    messagebox.showinfo("Success","Result Added successfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to{str(ex)}")
            
#****************
    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(" "),
        self.var_course.set(" "),
        self.var_marks.set(" "),
        self.var_full_marks.set(" "),
                                 
            
        

if __name__=="__main__":
    root=Tk()
    obj=resultClass(root)
    root.mainloop()