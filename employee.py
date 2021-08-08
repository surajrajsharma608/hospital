from os import stat
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import qrcode
from PIL import Image,ImageTk
from resizeimage import resizeimage
import pyttsx3

class EmployeeClass:
    def __init__(self,root):
        self.root = root
        root.config(bg='white')
        root.geometry('1033x520+310+133')
        root.resizable(False,False)
        root.config(bg='#9ec9d9')
        root.focus_force()
        root.title('Employee Details')

        #========Label frame for search=========
        lbl_frame = LabelFrame(self.root,text='Search Employee',bg='#9ec9d9')
        lbl_frame.place(x=200,y=15,width=600,height=55)

        self.var_searchby = StringVar()
        self.var_searchtxt = StringVar()
        self.search_combo = ttk.Combobox(lbl_frame,textvariable=self.var_searchby,font=('times new roman',12),values=('EID','Name','Contact','Email'),state='readonly',justify=CENTER)
        self.search_combo.place(x=20,y=2)
        self.search_combo.set('Select')

        
        self.txt_search = Entry(lbl_frame,font=('times new roman',14),bg='lightyellow',textvariable=self.var_searchtxt)
        self.txt_search.place(x=210,y=2)

        self.btn_search = Button(lbl_frame,command=self.search,text='Search',font=('times new roman',14),bg='#51b54a',fg='white')
        self.btn_search.place(x=410,y=2,h=25,w=130)
        #=========heading Label================
        title = Label(self.root,text='Employee Details',font=('goudy old style',20,'bold'),bg='#596980',fg='white').place(x=30,y=80,width=970,height=30)
        #=============Employee details wigets========
            #==========variables=============
        self.var_emp_id  = StringVar()
        self.var_gender  = StringVar()
        self.var_contact  = StringVar()
        self.var_name  = StringVar()
        self.var_dob  = StringVar()
        self.var_doj  = StringVar()
        self.var_email  = StringVar()
        self.var_password = StringVar()
        self.var_user_type  = StringVar()
        self.var_salary  = StringVar()

        lbl_emp_id = Label(self.root,text='Emp id:',font=('times new roman',15),bg='#9ec9d9').place(x=30,y=120)
        self.txt_emp_id = Entry(self.root,font=('times new roman',14),bg='lightyellow',textvariable=self.var_emp_id)
        self.txt_emp_id.place(x=130,y=120)

        lbl_gender = Label(self.root,text='Gender:',font=('times new roman',15),bg='#9ec9d9').place(x=360,y=120)
        self.gender_combo = ttk.Combobox(self.root,font=('times new roman',14),values=('Male','Female'),state='readonly',justify=CENTER,textvariable=self.var_gender)
        self.gender_combo.place(x=460,y=120,h=23)
        self.gender_combo.set('Select')

        lbl_contact = Label(self.root,text='Contact:',font=('times new roman',15),bg='#9ec9d9').place(x=720,y=120)
        self.txt_contact = Entry(self.root,font=('times new roman',14),bg='lightyellow',textvariable=self.var_contact)
        self.txt_contact.place(x=825,y=120,width=176)

        #=========2nd row=========
        lbl_name = Label(self.root,text='Name:',font=('times new roman',15),bg='#9ec9d9').place(x=30,y=160)
        self.txt_name = Entry(self.root,font=('times new roman',14),bg='lightyellow',textvariable=self.var_name)
        self.txt_name.place(x=130,y=160)

        lbl_dob = Label(self.root,text='D.O.B:',font=('times new roman',15),bg='#9ec9d9').place(x=360,y=160)
        self.txt_dob = Entry(self.root,font=('times new roman',14),bg='lightyellow',textvariable=self.var_dob)
        self.txt_dob.place(x=460,y=160,h=23,w=202)

        lbl_doj = Label(self.root,text='D.O.J:',font=('times new roman',15),bg='#9ec9d9').place(x=720,y=160)
        self.txt_doj = Entry(self.root,font=('times new roman',14),bg='lightyellow',textvariable=self.var_doj)
        self.txt_doj.place(x=825,y=160,width=176)

        #=========3rd row=========
        lbl_email = Label(self.root,text='Email:',font=('times new roman',15),bg='#9ec9d9').place(x=30,y=200)
        self.txt_email = Entry(self.root,font=('times new roman',14),bg='lightyellow',textvariable=self.var_email)
        self.txt_email.place(x=130,y=200)

        lbl_password = Label(self.root,text='Password:',font=('times new roman',15),bg='#9ec9d9').place(x=360,y=200)
        self.txt_password = Entry(self.root,font=('times new roman',14),bg='lightyellow',textvariable=self.var_password)
        self.txt_password.place(x=460,y=200,h=23,w=202)

        lbl_user_type = Label(self.root,text='User Type:',font=('times new roman',15),bg='#9ec9d9').place(x=720,y=200)
        self.user_type = ttk.Combobox(self.root,font=('times new roman',14),values=('Admin','Doctor','Acountant','Employee'),state='readonly',justify=CENTER,textvariable=self.var_user_type)
        self.user_type.place(x=825,y=200,h=23,width=176)
        self.user_type.set('Select User Type')

        #=========4rd row=========
        lbl_address = Label(self.root,text='Address:',font=('times new roman',15),bg='#9ec9d9').place(x=30,y=240)
        self.txt_address = Text(self.root,font=('times new roman',14),bg='lightyellow')
        self.txt_address.place(x=130,y=240,w=535,h=70)

        lbl_salary = Label(self.root,text='Salary:',font=('times new roman',15),bg='#9ec9d9').place(x=720,y=240)
        self.txt_salary = Entry(self.root,font=('times new roman',14),bg='lightyellow',textvariable=self.var_salary)
        self.txt_salary.place(x=825,y=240,w=176)

        #========Buttons================
        self.btn_save = Button(self.root,command=self.save,text='Save',font=('times new roman',14),bg='#597b99',fg='white')
        self.btn_save.place(x=670,y=285,h=25,w=80)
        self.btn_update = Button(self.root,text='Update',command=self.update,state=DISABLED,font=('times new roman',14),bg='#256934',fg='white')
        self.btn_update.place(x=760,y=285,h=25,w=80)
        self.btn_delete = Button(self.root,text='Delete',command=self.delete,state=DISABLED,font=('times new roman',14),bg='#ad2a42',fg='white')
        self.btn_delete.place(x=850,y=285,h=25,w=80)
        self.btn_clear = Button(self.root,text='Clear',state=DISABLED,font=('times new roman',14),bg='#285863',fg='white')
        self.btn_clear.place(x=940,y=285,h=25,w=65)

        #=======Employee details frame===================
        emp_frame = Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=320,width=760,height=200)

        self.xscroll = Scrollbar(emp_frame,orient=HORIZONTAL)
        self.yscroll = Scrollbar(emp_frame,orient=VERTICAL)
        self.EmpTable = ttk.Treeview(emp_frame,columns=('e_id','name','email','gender','contact','dob','doj','pass','utype','address','salary'),xscrollcommand=self.xscroll.set,yscrollcommand=self.yscroll.set)
        
       
        self.xscroll.pack(side=BOTTOM,fill=X) 
        self.yscroll.pack(side=RIGHT,fill=Y)
        self.xscroll.config(command=self.EmpTable.xview)
        self.yscroll.config(command=self.EmpTable.yview)
        

        self.EmpTable.heading('e_id',text='Employee Id')
        self.EmpTable.heading('name',text='Name')
        self.EmpTable.heading('email',text='Email')
        self.EmpTable.heading('gender',text='Gender')
        self.EmpTable.heading('contact',text='Contact')
        self.EmpTable.heading('dob',text='D.O.B')
        self.EmpTable.heading('doj',text='D.O.J')
        self.EmpTable.heading('pass',text='Password')
        self.EmpTable.heading('utype',text='User Type')
        self.EmpTable.heading('address',text='Address')
        self.EmpTable.heading('salary',text='Salary')
        self.EmpTable['show'] = 'headings'
        self.EmpTable.column('e_id',width=100)
        self.EmpTable.column('name',width=150)
        self.EmpTable.column('email',width=180)
        self.EmpTable.column('gender',width=80)
        self.EmpTable.column('contact',width=130)
        self.EmpTable.column('dob',width=120)
        self.EmpTable.column('doj',width=120)
        self.EmpTable.column('pass',width=100)
        self.EmpTable.column('utype',width=100)
        self.EmpTable.column('address',width=200)
        self.EmpTable.column('salary',width=120)

        self.EmpTable.pack(fill=BOTH,expand=1)
        self.EmpTable.bind('<ButtonRelease>',self.fetch_data)
        self.show()

        
        #=======Bar Code frame===================
        bar_code_frame = Frame(self.root,bd=3,relief=RIDGE)
        bar_code_frame.place(x=760,y=320,width=250,height=200)

        self.lbl_qr  = Label(bar_code_frame,text="No Qr\nAvailable",font=('goudy old style',15,'bold'),bg='skyblue',fg='white',bd=3,relief=RIDGE)
        self.lbl_qr.place(x=30,y=5,w=180,h=160)
        self.btn_qr= Button(bar_code_frame,text='Generate QR Code',font=('times new roman',8),bg='#285863',fg='white')
        self.btn_qr.place(x=30,y=168,w=180)

    
    # #=========Generate Bar code====================
    def generate(self):
        qr_data = (f"Employee ID: {self.var_emp_id.get()}\nEmployee Name: {self.var_name.get()}\nEmail: {self.var_email.get()}\nGender: {self.var_gender.get()}\nContact: {self.var_contact.get()}\nDOB: { self.var_dob.get()}\nDOJ: {self.var_doj.get()}\nPassword: {self.var_password.get()}\nUser Type: { self.var_user_type.get()}\nSalary: { self.var_salary.get()}\nAddress: { self.txt_address.get('1.0',END)}")
        # print(qr_data)
        qr_code = qrcode.make(qr_data)
        # print(qr_code)
        #==for resize qr code====================
        qr_code = resizeimage.resize_cover(qr_code,[180,160])
        #===========for save qr code======
        qr_code.save("Emp_QR_Code/Emp_"+str(self.var_emp_id.get())+'.png')
        #========QR IMAGE===========
        self.image = ImageTk.PhotoImage(qr_code)
        self.lbl_qr.config(image=self.image)
        
    
    # #==========functions start here==========================
    def save(self):
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get()=='':
                messagebox.showerror('Error','Employee id must be required',parent=self.root)
            else:
                cur.execute('select * from employee where eid=?',(self.var_emp_id.get(),))
                rows = cur.fetchone()
                if rows!=None:
                     messagebox.showerror('Error','Employee id already exists in your record , please try again with another id!!!',parent=self.root)
                else:
                    cur.execute('insert into employee(eid,name,email,gender,contact,dob,doj,pass,utype,address,salary) values(?,?,?,?,?,?,?,?,?,?,?)',(  
                        self.var_emp_id.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_password.get(),
                        self.var_user_type.get(),
                        self.txt_address.get('1.0',END),
                        self.var_salary.get()
                    ))
                    con.commit()
                    e = pyttsx3.init()
                    e.say('record added successfully')
                    e.runAndWait()
                    con.close()
                    
                    self.show()
                    self.btn_save.config(state=DISABLED)
                    self.btn_clear.config(state=NORMAL)
                    self.btn_update.config(state=NORMAL)
                    self.btn_delete.config(state=NORMAL)
        
        except Exception as ex:
            messagebox.showerror('Error',f'error due to:{str(ex)}',parent=self.root)

    def update(self):
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get()=='':
              messagebox.showerror('Error','Employee id must be required',parent=self.root)  
            else:
                cur.execute('select * from employee where eid=?',(self.var_emp_id.get(),)) 
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Please select record from list',parent=self.root)
                else:
                    cur.execute('update employee set name=?,email=?,gender=?,contact=?,dob=?,doj=?,pass=?,utype=?,address=?,salary=? where eid=?',(
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_contact.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_password.get(),
                        self.var_user_type.get(),
                        self.txt_address.get('1.0',END),
                        self.var_salary.get(),
                        self.var_emp_id.get()
                    ))
                    con.commit()
                    e = pyttsx3.init()
                    e.say('record updated successfully')
                    e.runAndWait()
                    con.close()
                    self.show()
                    self.clear()
        except Exception as ex:
            messagebox.showerror('error',f'error due to:{str(ex)}',parent=self.root)

    def delete(self):
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
            if self.var_emp_id.get()=='':
                messagebox.showerror('Error','Employee id must be required!!!',parent=self.root)
            else:
                cur.execute('select * from employee where eid=?',(self.var_emp_id.get(),))
                row = cur.fetchone()
                if row==None:
                    messagebox.showerror('Error','Please select record from list',parent=self.root)
                else:
                    op = messagebox.askyesno('Confirm','are u sure?',parent=self.root)
                    if op==True:
                        cur.execute('delete from employee where eid=?',(self.var_emp_id.get(),))
                        con.commit()
                        e = pyttsx3.init()
                        e.say('record deleted successfully')
                        e.runAndWait()
                        con.close()
                        self.show()
                        self.clear()
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to:{str(ex)}',parent=self.root)
  
    def show(self):
        try:
            con = sqlite3.connect(database='database/ims.db')
            cur = con.cursor()
            cur.execute('select * from employee')
            rows = cur.fetchall()
            self.EmpTable.delete(*self.EmpTable.get_children())
            for row in rows:
                self.EmpTable.insert('',END,values=row)
            con.close()
        except Exception as ex:
            messagebox.showerror('Error',f'error due to:{str(ex)}')
    def fetch_data(self,e):
        self.btn_save.config(state=DISABLED)
        self.btn_clear.config(state=NORMAL)
        self.btn_update.config(state=NORMAL)
        self.btn_delete.config(state=NORMAL)

        r =self.EmpTable.focus()
        content = self.EmpTable.item(r)
        row = content['values']
        # print(row)
        self.var_emp_id.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_gender.set(row[3])
        self.var_contact.set(row[4])
        self.var_dob.set(row[5])
        self.var_doj.set(row[6])
        self.var_password.set(row[7])
        self.var_user_type.set(row[8])
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,row[9])
        self.var_salary.set(row[10])  
        self.generate()
    
    def clear(self):
        self.btn_save.config(state=NORMAL)
        self.btn_clear.config(state=NORMAL)
        self.btn_update.config(state=DISABLED)
        self.btn_delete.config(state=DISABLED)

        self.var_emp_id.set('')
        self.var_name.set('')
        self.var_email.set('')
        self.var_gender.set('Select')
        self.var_contact.set('')
        self.var_dob.set('')
        self.var_doj.set('')
        self.var_password.set('')
        self.var_user_type.set('Select')
        self.txt_address.delete('1.0',END)
        self.txt_address.insert(END,'')
        self.var_salary.set('')
        self.var_searchtxt.set('')
        self.var_searchby.set('Select')
    
    def search(self):
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=='Select':
                messagebox.showerror('Error','Please select search by option first!!!',parent=self.root)
            elif self.var_searchtxt.get()=='':
                messagebox.showerror('Error','Search area should required!!!',parent=self.root)
            else:
                cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                row = cur.fetchall() 
                if len(row)!=0:
                    self.EmpTable.delete(*self.EmpTable.get_children())
                    for i in row:
                        self.EmpTable.insert('',END,values=i)
                else:
                     messagebox.showerror('Error','Record not found!!!!!',parent=self.root)
                self.btn_clear.config(state=NORMAL)
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to:{str(ex)}',parent=self.root)


if __name__ == '__main__':
    root = Tk()
    obj = EmployeeClass(root)
    root.mainloop()