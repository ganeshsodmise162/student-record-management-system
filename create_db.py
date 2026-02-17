import sqlite3

def create_db():
    con = sqlite3.connect(database="STUDENT_RECORD_MANAGEMENT_SYSTEM.db")
    cur = con.cursor()
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS course( 
            cid INTEGER PRIMARY KEY AUTOINCREMENT, 
            name TEXT, 
            duration TEXT,
            charges TEXT,
            describtion TEXT
        )
    """)
    con.commit()

    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS student( 
            roll INTEGER PRIMARY KEY AUTOINCREMENT, 
            name text, email text, gender text, dob text,contact text,state text,admission text,course text,city text,pin text,address text
        )
    """)
    con.commit()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS result(rid
             INTEGER PRIMARY KEY AUTOINCREMENT, 
            roll text, name text, course text, marks_ob text,full_marks text,per text
        )
    """)
    con.commit()

    con.close()

create_db()
