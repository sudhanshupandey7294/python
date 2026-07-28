from utils.Connection import DBConnect
class Employee:
    def addEmployee():
        ename =input("\n\tEnter new Employee name: ")
        eadd=input("\tEnter the new Employee address: ")
        esal=input("\tEnter Employee's salary: ")
        sql='insert into employee(ename, eadd, esal) value(%s, %s, %s)'
        data=(ename, eadd, esal)
        conn=DBConnect.getConnection()
        cur=conn.cursor()
        cur.execute(sql,data)
        if cur.rowcount>0:
            print("\n\tEmployee added successfully!")
        else :
            print("\n\t Failed to add Employee")

        conn.commit()
        cur.close()
        conn.close()


    def viewEmployee():
        sql='select * from employee'
        conn=DBConnect.getConnection()
        cur=conn.cursor()
        cur.execute(sql)
        data=cur.fetchall()
        print("\n\t EMPID EMPNAME           EMP_ADDRESS   EMP_SALARY")
        for emp in data:
            print(f"\t{emp[0]:<6} {emp[1]:<15} {emp[2]:11}  {emp[3]}")
        conn.commit()
        cur.close()
        conn.close()    

    def deleteEmployee():
        eid=print("\n\tEnter EID to delete: ")
        sql="select * from employee where eid=" +eid
        conn=DBConnect.getConnection()
        cur=conn.cursor()
        cur.execute(sql)
        data=cur.fetchone()
        print(data)
        if data:
                print("\tEmployee Name: ", data[1])
                print("\t Employee Address: ", data[2])
                sql="delete from employee where eid=" +eid
                cur.execute(sql)
                if cur.rowcount>0:
                    print("\n\tEmployee deleted successfully!")
                else:
                    print("\n\tFailed to delete employee") 
        else:
                print("\n\tEmployee not found on this ID!")
    
