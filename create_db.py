import sqlite3
def create_database():
    con = sqlite3.connect(database='database/ims.db')
    cur = con.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS department(depid INTEGER PRIMARY KEY AUTOINCREMENT,name text)")
    con.commit()

    # d_id,date,doctor,department,total_patient,unit_charge,total_charge,doctor_fee,hospital_income
    cur.execute("CREATE TABLE IF NOT EXISTS checks(cid INTEGER PRIMARY KEY AUTOINCREMENT,date text,doctor text,department text,total_patient text,unit_charge text,total_charge text,doctor_fee text,hospital_income text)")
    con.commit()


    con.close()
    
create_database()