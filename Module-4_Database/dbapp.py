import sqlite3

try:
    dbcon=sqlite3.connect('pydb.db')
    print("Database connected!")
except Exception as e:
    print(e)

#Create Table
create_tbl="create table studinfo(id integer primary key autoincrement,name varchar(20),city varchar(20))"
try:
    dbcon.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)


#Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('ashok','morbi'),('harsh','surat'),('pratik','mumbai'),('harshit','jamnagar'),('nikunj','rajkot')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)
"""


#Update Data
"""update_data="update studinfo set name='prasiddh',city='gondal' where id=3"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

#Delete Data
"""delete_data="delete from studinfo where id=3"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

cr=dbcon.cursor()

#Show Data
show_data="select * from studinfo" 
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(3)
    #data=cr.fetchone()
    #print(data)

    for i in data:
        #print(i)
        print(i[2])
except Exception as e:
    print(e)
