from os import stat
from sqlite3.dbapi2 import connect
from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
from tkcalendar import DateEntry
import nepali_datetime

class ReportClass:
    def __init__(self,root):
        self.root = root
        root.geometry('1033x500+310+140')
        root.resizable(False,False)
        root.config(bg='#9ec9d9')
        root.focus_force()
        root.title('Check Details')

        #=========heading Label================
        title = Label(self.root,text='Reports',font=('goudy old style',20,'bold'),bg='#596980',fg='white').place(x=30,y=10,width=970,height=30)

        #===========Search============
        self.var_searchby = StringVar()
        srch_lbl_frame = LabelFrame(self.root,text='Search',bg='#9ec9d9')
        srch_lbl_frame.place(x=200,y=60,w=600,h=55)
        self.search_combo = ttk.Combobox(srch_lbl_frame,font=('times new roman',13,'bold'),textvariable=self.var_searchby,values=('Date'),justify=CENTER,state=DISABLED)
        self.search_combo.place(x=20,y=3,width=200)
        self.search_combo.set('Date')

        self.var_searchtxt = StringVar()
        self.txt_search = Entry(srch_lbl_frame,font=('times new roman',14),bg='lightyellow',textvariable=self.var_searchtxt)
        self.txt_search.place(x=230,y=3)

        self.btn_search = Button(srch_lbl_frame,text='Search',font=('times new roman',14),bg='#51b54a',fg='white',command=self.search)
        self.btn_search.place(x=420,y=2,h=25,w=125)
    #==============================================table frame==============================================
        self.table_frame = Frame(self.root,bg='white',bd=3,relief=RIDGE)
        self.table_frame.place(x=30,y=150,w=970,h=190)

        self.xscroll = Scrollbar(self.table_frame,orient=HORIZONTAL)
        self.yscroll = Scrollbar(self.table_frame,orient=VERTICAL)
        self.reportTable = ttk.Treeview(self.table_frame,columns=('date','hospital_income','expanse'),xscrollcommand=self.xscroll.set,yscrollcommand=self.yscroll.set)
        
       
        self.xscroll.pack(side=BOTTOM,fill=X) 
        self.yscroll.pack(side=RIGHT,fill=Y)
        self.xscroll.config(command=self.reportTable.xview)
        self.yscroll.config(command=self.reportTable.yview)
        

        self.reportTable.heading('date',text='Date')
        self.reportTable.heading('hospital_income',text='Income')
        self.reportTable.heading('expanse',text='Expanse')
        self.reportTable['show'] = 'headings'
        self.reportTable.column('date',width=120)
        self.reportTable.column('hospital_income',width=100)
        self.reportTable.column('expanse',width=100)

        self.reportTable.pack(fill=BOTH,expand=1)
        # self.show()
        self.sho()
    
    # def show(self):
    #     total = 0
    #     con = sqlite3.connect(database='database/ims.db')
    #     cur = con.cursor()
    #     try:
    #        cur.execute('select date,hospital_income from checks')
    #        row = cur.fetchall()
    #        if len(row)>0:
    #            self.reportTable.delete(*self.reportTable.get_children())
    #            for i in row:
    #                self.reportTable.insert('',END,values=i)
    #     except Exception as ex:
    #         messagebox.showerror('error',f'error due to:{str(ex)}',parent=self.root)
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
                cur.execute("select date,hospital_income from checks where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                row = cur.fetchall() 
                if len(row)!=0:
                    self.reportTable.delete(*self.reportTable.get_children())
                    for i in row:
                        self.reportTable.insert('',END,values=i)
                else:
                     messagebox.showerror('Error','Record not found!!!!!',parent=self.root)
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to:{str(ex)}',parent=self.root)
    def sho(self):
        total = 0
        da = nepali_datetime.date.today()
        con = sqlite3.connect(database='database/ims.db')
        cur = con.cursor()
        try:
           cur.execute('select date,hospital_income from checks')
           row = cur.fetchall()
           for i in row:
               if str(i[0])==da:
                  total=total+int(i[1])
                  print(total)
            #    print(total)
            #    self.reportTable.insert('',END,values=(da,total))

        except Exception as ex:
            messagebox.showerror('error',f'error due to:{str(ex)}',parent=self.root)


        
if __name__ == '__main__':
    root = Tk()
    obj = ReportClass(root)
    root.mainloop()