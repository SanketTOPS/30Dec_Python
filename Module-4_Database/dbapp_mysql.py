import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='tempdb')
    print("Database connected!")
except Exception as e:
    print(e)

cr=dbcon.cursor()

# Table Create
tbl_create="create table studinfo(id integer primary key auto_increment,name text,sub text)"
try:
    cr.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)


# Insert data
"""insert_data="insert into studinfo(name,sub) values('sanket','python'),('nirav','php'),('ashok','java'),('mitesh','html'),('hitesh','python')"
try:
    cr.execute(insert_data)
    dbcon.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""

# Update data
"""update_data="update studinfo set sub='android' where id=4"
try:
    cr.execute(update_data)
    dbcon.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""

# Delete data
"""delete_data="delete from studinfo where id=4"
try:
    cr.execute(delete_data)
    dbcon.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""

# Select Data
select_data="select * from studinfo"
try:
    cr.execute(select_data)
    data=cr.fetchall()
    #data=cr.fetchmany(3)
    #data=cr.fetchone()
    #print(data)
    for i in data:
        print(i[1])
except Exception as e:
    print(e)
