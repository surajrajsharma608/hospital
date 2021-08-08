
from tkinter import *
from employee import EmployeeClass
from department import DepartmentClass
from checkup import CheckupClass
from report import ReportClass
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3
import time
import os
import nepali_datetime

class IMS:
    def __init__(self,root):
        self.root = root
        root.config(bg='#9ec9d9')
        root.geometry('1350x700+0+0')
        root.title('Inventory Management system')

        #=======title===============
       

        self.image = PhotoImage(file='images/logo1.png')
        self.title = Label(self.root,text='Kausalya Memorial Hospital',image=self.image,compound=LEFT,padx=15,font=('goudy old style',25,'bold'),bg='#596980',fg='white',anchor="w")
        self.title.place(x=0,y=0,relwidth=1,height=70)
        self.btn_logout = Button(self.root,text='Logout',font=('goudy old style',17,'bold'),bg='#596980',fg='white',cursor='hand2').place(x=1050,y=15,height=40,w=160)
        self.lbl_clock = Label(self.root,text='Welcome to Inventory System\t\t Date:DD:MM:YYYY\t\tTime:HH:MM:SS',font=('goudy old style',15),bg='gray',fg='white')
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)


        #======Left Menu===========
        self.l_image = Image.open('images/l_image.jpg')
        self.l_image = self.l_image.resize((290,200),Image.ANTIALIAS)
        self.l_image = ImageTk.PhotoImage(self.l_image)
        self.left_menu = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        self.left_menu.place(x=15,y=110,w=290,h=520)

        self.menu_logo = Label(self.left_menu,image=self.l_image)
        self.menu_logo.pack(side=TOP,fill=X)

        self.side_img = Image.open('images/arrow.png')
        self.side_img = self.side_img.resize((60,30),Image.ANTIALIAS)
        self.side_img = ImageTk.PhotoImage(self.side_img)
        menu_title = Label(self.left_menu,text='Menu',font=('goudy old style',20,'bold'),bg='#596980',fg='white').pack(side=TOP,fill=X)
        self.btn_employee = Button(self.left_menu,command=self.add_employee,text='Employee',image=self.side_img,compound=LEFT,anchor='w',padx=20,font=('goudy old style',17,'bold'),bg='#596980',fg='white',cursor='hand2').pack(side=TOP,fill=X)
        self.btn_Department = Button(self.left_menu,command=self.add_department,text='Department',image=self.side_img,compound=LEFT,anchor='w',padx=20,font=('goudy old style',17,'bold'),bg='#596980',fg='white',cursor='hand2').pack(side=TOP,fill=X)
        self.btn_check = Button(self.left_menu,command=self.add_checkup,text='Check',image=self.side_img,compound=LEFT,anchor='w',padx=20,font=('goudy old style',17,'bold'),bg='#596980',fg='white',cursor='hand2').pack(side=TOP,fill=X)
        self.btn_report = Button(self.left_menu,command=self.add_report,text='Reports',image=self.side_img,compound=LEFT,anchor='w',padx=20,font=('goudy old style',17,'bold'),bg='#596980',fg='white',cursor='hand2').pack(side=TOP,fill=X)
        self.btn_sale = Button(self.left_menu,text='Sales',image=self.side_img,compound=LEFT,anchor='w',padx=20,font=('goudy old style',17,'bold'),bg='#596980',fg='white',cursor='hand2').pack(side=TOP,fill=X)
        self.btn_exit = Button(self.left_menu,text='Exit',image=self.side_img,compound=LEFT,anchor='w',padx=20,font=('goudy old style',19,'bold'),bg='#596980',fg='white',cursor='hand2').pack(side=TOP,fill=X)

        #==========content===========
        self.lbl_employee = Label(self.root,text='Total Employee\n[ 0 ]',font=('goudy old style',17,'bold'),bg='#af5fd4',fg='white',bd=4,relief=RIDGE)
        self.lbl_employee.place(x=400,y=130,width=230,height=110)
        self.lbl_supplier = Label(self.root,text='Total Supplier\n[ 0 ]',font=('goudy old style',17,'bold'),bg='#5dba8c',fg='white',bd=4,relief=RIDGE)
        self.lbl_supplier.place(x=680,y=130,width=230,height=110)
        self.lbl_category = Label(self.root,text='Total Category\n[ 0 ]',font=('goudy old style',17,'bold'),bg='#696d96',fg='white',bd=4,relief=RIDGE)
        self.lbl_category.place(x=960,y=130,width=230,height=110)
        self.lbl_product = Label(self.root,text='Total Product\n[ 0 ]',font=('goudy old style',17,'bold'),bg='#c77752',fg='white',bd=4,relief=RIDGE)
        self.lbl_product.place(x=400,y=280,width=230,height=110)
        self.lbl_Sale = Label(self.root,text='Total Sale\n[0]',font=('goudy old style',17,'bold'),bg='#70224e',fg='white',bd=4,relief=RIDGE)
        self.lbl_Sale.place(x=680,y=280,width=230,height=110)
       
        #==============Footer==================
        footer = Label(self.root,text='Developed BY: Suraj@corporeation\nContact:9868290782',font=('goudy old style',15,'bold'),bg='#596980',fg='white').pack(side=BOTTOM,fill=X)
  
        self.date_time()
       

    def add_employee(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = EmployeeClass(self.new_win)
    def add_department(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = DepartmentClass(self.new_win)
    def add_checkup(self):
        self.new_win = Toplevel(self.root)
        self.new_obj =CheckupClass(self.new_win)

    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj =ReportClass(self.new_win)

    def date_time(self):
        da = nepali_datetime.date.today()
        time_ = time.strftime("%I:%M:%S")
        # date_ = time.strftime("%d-%m-%Y")
        self.lbl_clock.config(text=f'Welcome to Inventory System\t\t Date: {str(da)}\t\t{str(time_)}')

   

if __name__ == '__main__':
    root = Tk()
    obj = IMS(root)
    root.mainloop()