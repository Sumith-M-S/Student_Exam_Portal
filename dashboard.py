from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
from course import Courseclass
from student import studentClass
from result import resultClass
from report import reportClass
import os, sys


class RMS:
    def __init__(self, root):
        self.root = root
        self.root.title("CampusCore Pro Comprehensive Academic Records and Results Processing Platform")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # ***icons***
        self.logo_dash = ImageTk.PhotoImage(file="image/logo.jpg")

        # ***Title****
        title = Label(
            self.root,
            text="CampusCore Pro Comprehensive Academic Records and Results Processing Platform",
            image=self.logo_dash,
            padx=3,
            compound=LEFT,
            font=("goudy old style", 12, "bold"),
            bg="#033054",
            fg="white"
        )
        title.place(x=0, y=0, relwidth=1, height=50)

        # ***Menu***
        M_Frame = LabelFrame(self.root, text="Menus", font=("times new roman", 15), bg="white")
        M_Frame.place(x=10, y=70, width=1515, height=80)

        # **buttons**
        btn_course = Button(self.root, text="Course", font=("goudy old style", 15, "bold"),
                            bg="#0b5377", fg="white", cursor="hand2", command=self.add_course)
        btn_course.place(x=50, y=95, width=180, height=40)

        btn_student = Button(self.root, text="Student", font=("goudy old style", 15, "bold"),
                             bg="#0b5377", fg="white", cursor="hand2", command=self.add_student)
        btn_student.place(x=300, y=95, width=180, height=40)

        btn_result = Button(self.root, text="Result", font=("goudy old style", 15, "bold"),
                            bg="#0b5377", fg="white", cursor="hand2", command=self.add_result)
        btn_result.place(x=545, y=95, width=180, height=40)

        btn_view = Button(self.root, text="View", font=("goudy old style", 15, "bold"),
                          bg="#0b5377", fg="white", cursor="hand2", command=self.add_report)
        btn_view.place(x=790, y=95, width=180, height=40)

        btn_logout = Button(self.root, text="Logout", font=("goudy old style", 15, "bold"),
                            bg="#0b5377", fg="white", cursor="hand2", command=self.logout)
        btn_logout.place(x=1044, y=95, width=180, height=40)

        btn_exit = Button(self.root, text="Exit", font=("goudy old style", 15, "bold"),
                          bg="#0b5377", fg="white", cursor="hand2", command=self.exit_)
        btn_exit.place(x=1300, y=95, width=180, height=40)

        # ***content***
        self.bg_img = Image.open("image/bg.jpg")
        self.bg_img = self.bg_img.resize((920, 350))
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=860, y=159, width=650, height=400)

        # **update_details**
        self.lbl_course = Label(self.root, text="Total Courses\n[ 0 ]",
                                font=("goudy old style", 20), bd=10, relief=RIDGE,
                                bg="#e43b06", fg="white")
        self.lbl_course.place(x=875, y=580, width=200, height=100)

        self.lbl_student = Label(self.root, text="Total Students\n[ 0 ]",
                                 font=("goudy old style", 20), bd=10, relief=RIDGE,
                                 bg="#06e42f", fg="white")
        self.lbl_student.place(x=1090, y=580, width=200, height=100)

        self.lbl_result = Label(self.root, text="Total Results\n[ 0 ]",
                                font=("goudy old style", 20), bd=10, relief=RIDGE,
                                bg="#0a06e4", fg="white")
        self.lbl_result.place(x=1300, y=580, width=200, height=100)

        # ***footer****
        footer = Label(self.root,
                       text="GMIT - Comprehensive Academic Records and Results Processing Platform\nContact us for any technical issues: 8792550051",
                       font=("goudy old style", 12),
                       bg="#262626", fg="white")
        footer.pack(side=BOTTOM, fill=X)

    # ---------------- MENU FUNCTIONS ---------------- #
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Courseclass(self.new_win)

    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = studentClass(self.new_win)

    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = resultClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = reportClass(self.new_win)

    # ---------------- LOGOUT AND EXIT ---------------- #
    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you really want to logout?", parent=self.root)
        if op:
            self.root.destroy()
            os.system(f"{sys.executable} log_in.py")  # reopen login screen

    def exit_(self):
        op = messagebox.askyesno("Confirm", "Do you really want to Exit?", parent=self.root)
        if op:
            self.root.destroy()


# ---------------- MAIN ---------------- #
if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
