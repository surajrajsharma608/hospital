from os import stat
from sqlite3.dbapi2 import connect
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
from tkcalendar import DateEntry
import nepali_datetime

class CheckupClass:
    def __init__(self,root):
        self.root = root
        root.geometry('1033x500+310+140')
        root.resizable(False,False)
        root.config(bg='#9ec9d9')
        root.focus_force()
        root.title('Check Details')

       

        #===========Search============
        self.var_searchby = StringVar()
        srch_lbl_frame = LabelFrame(self.root,text='Search',bg='#9ec9d9')
        srch_lbl_frame.place(x=200,y=15,w=600,h=55)
        self.search_combo = ttk.Combobox(srch_lbl_frame,font=('times new roman',13,'bold'),textvariable=self.var_searchby,values=('Doctor','Date','Department'),justify=CENTER,state='readonly')
        self.search_combo.place(x=20,y=3,width=200)
        self.search_combo.set('Select')

        self.var_searchtxt = StringVar()
        self.txt_search = Entry(srch_lbl_frame,font=('times new roman',14),bg='lightyellow',textvariable=self.var_searchtxt)
        self.txt_search.place(x=230,y=3)

        self.btn_search = Button(srch_lbl_frame,text='Search',font=('times new roman',14),bg='#51b54a',fg='white',command=self.search)
        self.btn_search.place(x=420,y=2,h=25,w=125)

         #=========heading Label================
        title = Label(self.root,text='Check Details',font=('goudy old style',20,'bold'),bg='#596980',fg='white').place(x=30,y=80,width=970,height=30)

        #============widgets===================
        prod_frame = LabelFrame(self.root,bg='white')
        prod_frame.place(x=30,y=120,w=970,h=150)
        self.var_doctor = StringVar()
        self.var_department = StringVar()
        self.var_patient = StringVar() 
        self.var_charge = StringVar()
        self.var_total = StringVar()
        self.var_doctor_charge = StringVar() 
        self.var_income = StringVar() 
        self.var_date = StringVar() 
        self.var_check_id = StringVar() 

        self.doctor_list = []
        self.fetch_doctor()
        self.department_list = []
        self.fetch_department()

        self.txt_p = Entry(prod_frame,font=('times new roman',14),bg='lightyellow',textvariable=self.var_check_id,state='readonly',justify=CENTER)
        self.txt_p.place(x=173,y=5,h=23,w=160)

        da = nepali_datetime.date.today()
        lbl_date = Label(prod_frame,text='Date:',font=('times new roman',15),bg='white').place(x=360,y=5)
        # self.date_combo = DateEntry(prod_frame, width=12, year=2021, month=6, day=22, background='darkblue', foreground='white', borderwidth=2,font=('times new roman',14),state='readonly',justify=CENTER,textvariable=self.var_date)
        self.date_combo= Entry(prod_frame,font=('times new roman',14),bg='lightyellow',textvariable=self.var_date,state='readonly',justify=CENTER)
        self.date_combo.place(x=460,y=5,h=23,w=160)
        self.var_date.set(str(da))
        

        lbl_doctor = Label(prod_frame,text='Doctor:',font=('times new roman',15),bg='white').place(x=80,y=35)
        self.doctor_combo = ttk.Combobox(prod_frame,font=('times new roman',14),state='readonly',justify=CENTER,textvariable=self.var_doctor,values=self.doctor_list)
        self.doctor_combo.place(x=173,y=35,h=23,w=160)
        self.doctor_combo.set('Select')

        lbl_department = Label(prod_frame,text='Department:',font=('times new roman',15),bg='white').place(x=360,y=35)
        self.txt_department_combo = ttk.Combobox(prod_frame,font=('times new roman',14),state='readonly',justify=CENTER,textvariable=self.var_department,values=self.department_list)
        self.txt_department_combo.place(x=460,y=35,h=23)
        self.txt_department_combo.set('Select')

        lbl_patient = Label(prod_frame,text='Patient:',font=('times new roman',15),bg='white').place(x=700,y=35)
        self.txt_patient = Entry(prod_frame,font=('times new roman',14),bg='lightyellow',textvariable=self.var_patient,justify=CENTER)
        self.txt_patient.place(x=800,y=35,h=23,w=120)

        lbl_charge = Label(prod_frame,text='Charge:',font=('times new roman',15),bg='white').place(x=80,y=70)
        self.txt_charge = Entry(prod_frame,font=('times new roman',14),bg='lightyellow',textvariable=self.var_charge,justify=CENTER)
        self.txt_charge.place(x=173,y=70,h=23,w=160)

        lbl_total = Label(prod_frame,text='Total:',font=('times new roman',15),bg='white').place(x=360,y=70)
        self.txt_total = Entry(prod_frame,font=('times new roman',14),bg='lightyellow',textvariable=self.var_total,justify=CENTER)
        self.txt_total.place(x=460,y=70,h=23,w=203)

        lbl_doctor_charge = Label(prod_frame,text='Doctor Fe:',font=('times new roman',15),bg='white').place(x=700,y=70)
        self.txt_doctor_charge = Entry(prod_frame,font=('times new roman',14),bg='lightyellow',justify=CENTER,textvariable=self.var_doctor_charge)
        self.txt_doctor_charge.place(x=800,y=70,h=23,w=120)

        lbl_income = Label(prod_frame,text='Income',font=('times new roman',15),bg='white').place(x=80,y=105)
        self.txt_income = Entry(prod_frame,font=('times new roman',14),bg='lightyellow',justify=CENTER,textvariable=self.var_income)
        self.txt_income.place(x=173,y=105,h=23,w=120)
        self.btn_cal = Button(prod_frame,text='cal',font=('times new roman',14),bg='#597b99',fg='white',command=self.cal)
        self.btn_cal.place(x=300,y=105,h=25,w=80)
        self.btn_save = Button(prod_frame,text='Add',command=self.save,font=('times new roman',14),bg='#597b99',fg='white')
        self.btn_save.place(x=385,y=105,h=25,w=80)

        self.table_frame = Frame(self.root,bg='white',bd=3,relief=RIDGE)
        self.table_frame.place(x=30,y=270,w=970,h=190)

        self.xscroll = Scrollbar(self.table_frame,orient=HORIZONTAL)
        self.yscroll = Scrollbar(self.table_frame,orient=VERTICAL)
        self.checkTable = ttk.Treeview(self.table_frame,columns=('d_id','date','doctor','department','total_patient','unit_charge','total_charge','doctor_fee','hospital_income'),xscrollcommand=self.xscroll.set,yscrollcommand=self.yscroll.set)
        
       
        self.xscroll.pack(side=BOTTOM,fill=X) 
        self.yscroll.pack(side=RIGHT,fill=Y)
        self.xscroll.config(command=self.checkTable.xview)
        self.yscroll.config(command=self.checkTable.yview)
        

        self.checkTable.heading('d_id',text='S.L')
        self.checkTable.heading('date',text='Date')
        self.checkTable.heading('doctor',text='Doctor Name')
        self.checkTable.heading('department',text='Department')
        self.checkTable.heading('total_patient',text='Total Patient')
        self.checkTable.heading('unit_charge',text='Unit Charge')
        self.checkTable.heading('total_charge',text='Total')
        self.checkTable.heading('doctor_fee',text='Doctor Fee')
        self.checkTable.heading('hospital_income',text='Hospital Income')
        self.checkTable['show'] = 'headings'
        self.checkTable.column('d_id',width=70)
        self.checkTable.column('date',width=120)
        self.checkTable.column('doctor',width=180)
        self.checkTable.column('department',width=80)
        self.checkTable.column('total_patient',width=90)
        self.checkTable.column('unit_charge',width=90)
        self.checkTable.column('total_charge',width=100)
        self.checkTable.column('doctor_fee',width=100)
        self.checkTable.column('hospital_income',width=100)

        self.checkTable.pack(fill=BOTH,expand=1)
        self.lbl_total_patiant = Label(self.root,text='Doctor:',font=('times new roman',15),bg='white')
        self.lbl_total_patiant.place(x=485,y=460,w=80)

        self.lbl_total_amount = Label(self.root,font=('times new roman',15),bg='white')
        self.lbl_total_amount.place(x=665,y=460,w=100)

        self.lbl_total_doctor_fee = Label(self.root,font=('times new roman',15),bg='white')
        self.lbl_total_doctor_fee.place(x=770,y=460,w=100)

        self.lbl_total_income = Label(self.root,font=('times new roman',15),bg='white')
        self.lbl_total_income.place(x=875,y=460,w=120)
        
        self.show()
        self.check()
        

    def cal(self):
        ca = int(self.var_patient.get())*int(self.var_charge.get())
        d = int(self.var_charge.get())-200
        d_f= int(self.var_patient.get())*d
        inc = int(ca-d_f)
        self.var_doctor_charge.set(str(round(d_f,2)))
        self.var_total.set(str(round(ca,2)))
        self.var_income.set(str(round(inc,2)))
    
    def fetch_doctor(self):
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
            cur.execute('select name from employee')
            row = cur.fetchall()
            if len(row)>0:
                for i in row:
                    self.doctor_list.append(i[0])

        except Exception as ex:
            messagebox.showerror('error',f'error due to:{str(ex)}',parent=self.root)

    def fetch_department(self):
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
            cur.execute('select name from department')
            row = cur.fetchall()
            if len(row)>0:
                for i in row:
                    self.department_list.append(i[0])

        except Exception as ex:
            messagebox.showerror('error',f'error due to:{str(ex)}',parent=self.root)
    
    def save(self):
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
           if self.var_doctor.get()=='Select' or self.var_department.get()=='Select':
               messagebox.showerror('Error','Please select optional fields!!',parent=self.root)
           else:
                cur.execute('select * from checks where cid=?',(self.var_check_id.get(),))
                rows = cur.fetchone()
                if rows!=None:
                     pass
                else:
                   cur.execute('insert into checks(date,doctor,department,total_patient,unit_charge,total_charge,doctor_fee,hospital_income) values(?,?,?,?,?,?,?,?)',(
                       
                        self.var_date.get(),
                        self.var_doctor.get(),
                        self.var_department.get(),
                        self.var_patient.get(), 
                        self.var_charge.get(),
                        self.var_total.get(),
                        self.var_doctor_charge.get(), 
                        self.var_income.get(), 
                        

                   ))
                   con.commit()
                   messagebox.showinfo('Success','Record added successfully!!!',parent=self.root)
                   con.close()
                   self.show()

        except Exception as ex:
            messagebox.showerror('error',f'error due to:{str(ex)}',parent=self.root)

    def show(self):
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
           cur.execute('select * from checks')
           row = cur.fetchall()
           if len(row)>0:
               self.checkTable.delete(*self.checkTable.get_children())
               for i in row:
                   self.checkTable.insert('',END,values=i)
        except Exception as ex:
            messagebox.showerror('error',f'error due to:{str(ex)}',parent=self.root)

    def check(self):
        hospital_income=0
        doctor_fee = 0
        total = 0
        total_patient = 0
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
           cur.execute('select * from checks')
           row = cur.fetchall()
           for i in row:
                hospital_income+=int(i[8])
                self.lbl_total_income.config(text=f'Rs. {str(round(hospital_income,2))}')

                doctor_fee+=int(i[7])
                self.lbl_total_doctor_fee.config(text=f'Rs. {str(round(doctor_fee,2))}')

                total+=int(i[6])
                self.lbl_total_amount.config(text=f'Rs. {str(round(total,2))}')

                total_patient+=int(i[4])
                self.lbl_total_patiant.config(text=f'{str(round(total_patient,2))}')
                # self.lbl_total_patiant.after(200,self.check)
              
        except Exception as ex:
            messagebox.showerror('error',f'error due to:{str(ex)}',parent=self.root)

    def search(self):
        # print('hello')
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get()=='Select':
                messagebox.showerror('Error','Please select search by option first!!!',parent=self.root)
            elif self.var_searchtxt.get()=='':
                messagebox.showerror('Error','Search area should required!!!',parent=self.root)
            else:
                cur.execute("select * from checks where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                row = cur.fetchall() 
                if len(row)!=0:
                    self.checkTable.delete(*self.checkTable.get_children())
                    for i in row:
                        self.checkTable.insert('',END,values=i)
                else:
                     messagebox.showerror('Error','Record not found!!!!!',parent=self.root)
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to:{str(ex)}',parent=self.root)

        
        
if __name__ == '__main__':
    root = Tk()
    obj = CheckupClass(root)
    root.mainloop()