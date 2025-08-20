# To Create the db
import sqlite3 
def create_db():
    con=sqlite3.connect(database="RMS.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,duration text,charges text, description text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY,name text,Email text,Gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY ,roll text,name text,course text,marks_obtained text,full_marks text,percentage text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT)")
    con.commit()


    
    con.close()
create_db()