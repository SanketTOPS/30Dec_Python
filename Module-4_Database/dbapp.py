import sqlite3

# Database Create/Connect
try:
    dbcon=sqlite3.connect("mydb.db")
    print("Database connected!")
except Exception as e:
    print(e)

# Table Create
create_tbl="create table studinfo(id integer primary key autoincrement,name text,sub text)"
try:
    dbcon.execute(create_tbl)
    print("Table created successfully!")
except Exception as e:
    print(e)

# Insert data
"""insert_data="insert into studinfo(name,sub) values('sanket','python'),('mitesh','java'),('ashok','php'),('pratik','node'),('hitesh','android')"
try:
    dbcon.execute(insert_data)
    dbcon.commit()
    print("Record inserted successfully!")
except Exception as e:
    print(e)"""


# Update data
"""update_data="update studinfo set sub='react' where id=4"
try:
    dbcon.execute(update_data)
    dbcon.commit()
    print("Record updated successfully!")
except Exception as e:
    print(e)"""

# Delete Data
"""delete_data="delete from studinfo where id=4"
try:
    dbcon.execute(delete_data)
    dbcon.commit()
    print("Record deleted successfully!")
except Exception as e:
    print(e)"""

cur=dbcon.cursor()
# Show Data
show_data="select * from studinfo"
try:
    cur.execute(show_data)
    #data=cur.fetchmany(3)
    data=cur.fetchone()
    print(data)
except Exception as e:
    print(e)