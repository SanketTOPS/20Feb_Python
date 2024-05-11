import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='newtempdb')
    print("Database connected!")
except Exception as e:
    print(e)


cr=dbcon.cursor()
#Create Table
create_tbl="create table studinfo(id integer primary key auto_increment,name varchar(20),city varchar(20))"
try:
    cr.execute(create_tbl)
    print("Table created!")
except Exception as e:
    print(e)

#Insert Data
"""insert_data="insert into studinfo(name,city)values('sanket','rajkot'),('ashok','morbi'),('harsh','surat'),('pratik','mumbai'),('harshit','jamnagar'),('nikunj','rajkot')"
try:
    cr.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

#Update Data
"""update_data="update studinfo set name='prasiddh',city='gondal' where id=3"
try:
    cr.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

#Delete Data
"""delete_data="delete from studinfo where id=3"
try:
    cr.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

#Show Data
show_data="select * from studinfo"
try:
    cr.execute(show_data)
    data=cr.fetchall()
    #data=cr.fetchmany(2)
    #data=cr.fetchone()
    #print(data)

    for i in data:
        print(i)
except Exception as e:
    print(e)