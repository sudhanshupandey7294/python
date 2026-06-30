import mysql.connector

conn=mysql.connector.connect(
host='localhost', #127.0.0.1
port='3306',
user='root',
password='Y1a2s3h4p5@' ,  # mysql password
database='flipkart'
    )

#print(conn)


# To write query of mysql in python we connect it with cursor
cur=conn.cursor()
#=================================================================================================================
#write all sql queries using cursor
"""
sql='show databases'
cur.execute(sql)
print(cur.fetchall())


sql='create database flipkart'
cur.execute(sql)


sql="USE flipkart"
cur.execute(sql)
sql= '''
CREATE TABLE employee(
eid INT PRIMARY KEY AUTO_INCREMENT,
ename VARCHAR(30) NOT NULL,
eadd VARCHAR(50) NOT NULL,
esal DECIMAL(8,2) NOT NULL
)
'''
cur.execute(sql)


sql='INSERT INTO employee VALUE(101, "Ravi kumar", "Noida", 60000)'
cur.execute(sql)
#print(sql.rowcount)
if cur.rowcount>0 :
    print("Data inserted Successfully!")
else:
    print("Failed to insert data !")


ename=input("Enter new Employee Name: ")
eadd=input("Enter the address: ")
esal=input("Enter the salary: ")
sql='INSERT INTO employee(ename, eadd, esal) VALUE("'+ename+'", "'+eadd+'", "'+esal+'")' # sql= f'INSERT INTO employee(ename, eadd, esal) VALUE("{ename}", "{eadd}", "{esal}")'
cur.execute(sql)
if cur.rowcount>0:
    print('Data inserted successfully!')
else:
    print('Failed! data not inserted')

#OR

ename=input("Enter new Employee Name: ")
eadd=input("Enter the address: ")
esal=input("Enter the salary: ")
sql='INSERT INTO employee(ename, eadd, esal) VALUE(%s, %s, %s)'
data=(ename, eadd, esal)
cur.execute(sql, data)
if cur.rowcount>0:
    print('Data inserted successfully!')
else:
    print('Failed! data not inserted')
"""
#__________________________________________________

query='SELECT * FROM employee'
cur.execute(query)
print(cur.fetchall())

#OR
query='SELECT * FROM employee'
cur.execute(query)
data=cur.fetchall()
for i in data:
    print(i)
    print("Employee ID: ", i[0])
    print("Employee name: ", i[1])
    print("Employee address: ", i[2])
    print("Employee Salary: ", i[3])



#======================================CLOSE MYSQL CONNECTION=====================================================
conn.commit() # very important 
cur.close()
conn.close()
