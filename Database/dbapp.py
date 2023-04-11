import pymysql

try:
    dbcon=pymysql.connect(host='localhost',user='root',password='',database='newdb')
    print("Server Connected")
except Exception as e:
    print(e)

# Database Created
cur=dbcon.cursor()
"""try:
   cur.execute("CREATE DATABASE IF NOT EXISTS ipdb")
   print("Database created!")
except Exception as e:
    print(e)
"""

#cur.execute('SHOW DATABASES')

# Table Created
tbl_create="create table studinfo(id int primary key auto_increment,name text,ub text)"
try:
    cur.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)
  
# Insert Data
"""insert_data="insert into studinfo(name,ub) values('nirav','java'),('sanket','python'),('mitesh','php'),('ashok','html')"
try:
    cur.execute(insert_data)
    dbcon.commit()
    print("Record Inserted!")
except Exception as e:
    print(e)"""
    
# Update Data
"""update_data="update studinfo set ub='iOS' where id=4"
try:
    cur.execute(update_data)
    dbcon.commit()
    print("Record Updated!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where id=3"
try:
    cur.execute(delete_data)
    dbcon.commit()
    print("Record Deleted!")
except Exception as e:
    print(e)"""


# Show Data
select_data="select * from studinfo"
try:
    cur.execute(select_data)
    data=cur.fetchall()
    #data=cur.fetchmany(2)
    #data=cur.fetchone()
    #print(data)

    for i in data:
        print(i)
except Exception as e:
    print(e)