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
    con.close()

create_db()
