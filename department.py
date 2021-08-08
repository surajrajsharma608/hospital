from os import stat
from sqlite3.dbapi2 import connect
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import pyttsx3
class DepartmentClass:
    def __init__(self,root):
        self.root = root
        root.geometry('1033x500+310+140')
        root.resizable(False,False)
        root.config(bg='#9ec9d9')
        root.focus_force()
        root.title('Departments Details')

        #===========Search============
        self.var_searchby = StringVar()
        srch_lbl_frame = LabelFrame(self.root,text='Search Department',bg='#9ec9d9')
        srch_lbl_frame.place(x=200,y=15,w=600,h=55)
        self.search_combo = ttk.Combobox(srch_lbl_frame,font=('times new roman',13,'bold'),textvariable=self.var_searchby,values=('DepID','Name'),justify=CENTER,state='readonly')
        self.search_combo.place(x=20,y=3,width=200)
        self.search_combo.set('Select')

        self.var_searchtxt = StringVar()
        self.txt_search = Entry(srch_lbl_frame,font=('times new roman',14),bg='lightyellow',textvariable=self.var_searchtxt)
        self.txt_search.place(x=230,y=3)

        self.btn_search = Button(srch_lbl_frame,text='Search',font=('times new roman',14),bg='#51b54a',fg='white')
        self.btn_search.place(x=420,y=2,h=25,w=125)
         #=========heading Label================
        title = Label(self.root,text='Department Details',font=('goudy old style',20,'bold'),bg='#596980',fg='white').place(x=30,y=80,width=970,height=30)
        #============widgets===================
        supp_frame = LabelFrame(self.root,bg='white',text='Category')
        supp_frame.place(x=30,y=120,w=970,h=90)

        self.var_department = StringVar()
        self.var_department_id = StringVar()
        lbl_department = Label(supp_frame,text='Department:',font=('times new roman',15),bg='white').place(x=200,y=5)
        self.txt_department = Entry(supp_frame,font=('times new roman',14),bg='lightyellow',textvariable=self.var_department)
        self.txt_department.place(x=310,y=5)



        #========Buttons================
        self.btn_save = Button(supp_frame,command=self.add,text='Save',font=('times new roman',14),bg='#597b99',fg='white')
        self.btn_save.place(x=230,y=40,h=25,w=80)
        self.btn_update = Button(supp_frame,text='Update',command=self.update,font=('times new roman',14),bg='#256934',fg='white')
        self.btn_update.place(x=320,y=40,h=25,w=80)
        self.btn_delete = Button(supp_frame,text='Delete',command=self.delete,font=('times new roman',14),bg='#ad2a42',fg='white')
        self.btn_delete.place(x=410,y=40,h=25,w=80)
        self.btn_clear = Button(supp_frame,text='Clear',font=('times new roman',14),bg='#285863',fg='white')
        self.btn_clear.place(x=500,y=40,h=25,w=80)

        #==========employee details table============
        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=30,y=210,h=265,w=600)

        self.xscroll = Scrollbar(emp_frame,orient=HORIZONTAL)
        self.yscroll = Scrollbar(emp_frame,orient=VERTICAL)
        self.departmentTable = ttk.Treeview(emp_frame,columns=('catid','name'),xscrollcommand=self.xscroll.set,yscrollcommand=self.yscroll.set)
        self.xscroll.pack(side=BOTTOM,fill=X)
        self.yscroll.pack(side=RIGHT,fill=Y)
        self.xscroll.config(command=self.departmentTable.xview)
        self.yscroll.config(command=self.departmentTable.yview)

        self.departmentTable.heading('catid',text='department ID')
        self.departmentTable.heading('name',text='Name')
        self.departmentTable['show'] = 'headings'
        self.departmentTable.pack(fill=BOTH,expand=1)
        self.departmentTable.bind('<ButtonRelease>',self.fetch_data)
        self.show()

    def show(self):
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
            cur.execute('select * from department')
            row = cur.fetchall()
            if len(row)!=0:
                self.departmentTable.delete(*self.departmentTable.get_children())
                for i in row:
                    self.departmentTable.insert('',END,values=i)
        except Exception as ex:
            messagebox.showerror('Error',f'error due to:{str(ex)}',parent=self.root)
    
    def add(self):
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
            if self.var_department.get()=='':
                messagebox.showerror('Error','Department name required to be entered!!',parent=self.root)
            else:
                cur.execute('select * from department where depid=?',(self.var_department_id.get(),))
                row = cur.fetchone()
                if row!=None:
                    messagebox.showerror('Error','Department name already exist!!',parent=self.root)
                else:
                    cur.execute('insert into department (name) values(?)',(self.var_department.get(),))
                    con.commit()
                    e = pyttsx3.init()
                    e.say('department added successfully')
                    e.runAndWait()
                    con.close()
                    self.show()
        except Exception as ex:
            messagebox.showerror('Error',f'error due to:{str(ex)}',parent=self.root)

    def update(self):
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
            if self.var_department.get()=='':
                messagebox.showerror('Error','Department name required to be entered!!',parent=self.root)
            # else:
            #     cur.execute('select * from category where name=?',(self.var_category.get(),))
            #     row = cur.fetchone()
            #     if row==None:
            #         messagebox.showerror('Error','please select category from list !!',parent=self.root)
            else:
                        cur.execute('update department set name=? where depid=?',(
                        self.var_department.get(),
                        self.var_department_id.get()
                        ))
                        con.commit()
                        e = pyttsx3.init()
                        e.say('department updated successfully')
                        e.runAndWait()
                        con.close()
                        self.show()
        except Exception as ex:
            messagebox.showerror('Error',f'error due to:{str(ex)}',parent=self.root)

    def clear(self):
        self.var_department.set('')
        self.var_searchby.set('Select')
        self.var_searchtxt.set('')

    def fetch_data(self,e):
        r= self.departmentTable.focus()
        content = self.departmentTable.item(r)
        row = content['values']
        # print(row)
        self.var_department_id.set(row[0])
        self.var_department.set(row[1])

    def delete(self):
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
            if self.var_department_id.get()=='':
                messagebox.showerror('Error','Department id must be required!!!',parent=self.root)
            else:
                cur.execute('select * from department where depid=?',(self.var_department_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Please select record from list',parent=self.root)
                else:
                    op = messagebox.askyesno('confirm','Do you really want to delete this record!!!',parent=self.root)
                    if op==True:
                        cur.execute('delete from department where depid=?',(self.var_department_id.get(),))
                        con.commit()
                        e = pyttsx3.init()
                        e.say('department deleted successfully')
                        e.runAndWait()
                        self.show()
                        con.close()
        except Exception as ex:
            messagebox.showerror('Error',f'error due to:{str(ex)}',parent=self.root)
    

if __name__ == '__main__':
    root = Tk()
    obj = DepartmentClass(root)
    root.mainloop()