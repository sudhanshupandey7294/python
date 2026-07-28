"""
Employee Management System

1. Add employee
2. View all employee
3. Update employee salary
4. Delete employee
0. Exit
"""
# Importing libraries and functions
from utils.Entity import Employee
#Dashboard

while True:
    print('''
  1. Add employee
2. View all employee
3. Update employee salary
4. Delete employee
0. Exit
''')
    ch=int(input("\tEnter your choice: "))
    if ch==0:
      print("\n\t Thank you!")
    elif ch==1:
      Employee.addEmployee()
      print("Press ENTER to continue...")
    elif ch==2:
       Employee.viewEmployee()
       print("Press ENTER to continue...")
    elif ch==4:
           Employee.deleteEmployee()
           print("Press ENTER to continue...") 


