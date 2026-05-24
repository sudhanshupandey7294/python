# Basic Input & Print Questions 
# 1. Write a program to print “Hello Python” on the screen. 
# 2. Take a name as input and print 
# Welcome <name> 
# 3. Take a number as input and print it. 
# 4. Take two numbers as input and print both numbers on separate lines. 
# 5. Take a name and age as input and print: 
# My name is ___ and my age is ___ 

print("Hello Python")

a= input("Enter your name :")
print("Welcome",a)
b=input("Enter a number :")
print(b)
c=input("Enter first number ")
d=input("Enter second number ")
print(c)
print(d) 
e=input("Enter your name")
f=input("Enter age ")
print("My name is :" ,e, "and my age is :",f)

#Integer (int) Based Questions 
#6. Take an integer as input and print its square. 
#7. Take two integers as input and print their sum. 
#8. Take two integers and print: 
#o Addition 
#o Subtraction 
#o Multiplication 
#9. Take a number and print: 
#The number entered is <number> 
#10. Take an integer and print its double.

a= int(input("Enter the integer number :"))
print("The square of the number is :",a**2)

a=int(input("Enter 1st integer :"))
b=int(input("Enter 2nd integer :"))
c=("The addition is :",a+b)
print(c)
d=("The substraction is :",a-b)
print(d)
e=("The multiplication is :",a*b)
print(e)
print("The number entered is :",a, "and" ,b)

f=int(input("Enter the number you want to get its double :"))
print("The double of the number is",f*2)


#Float (float) Based Questions 
#11. Take a float value as input and print it. 
#12. Take two float numbers and print their sum. 
#13. Take a float number and print its half value. 
#14. Take length and width (float) as input and print the area of a rectangle.  (length*width) 
#15. Take radius as float input and print the area of a circle 
#(Use π = 3.14)

a=float(input("Enter your float number :"))
print(a)
c=float(input("Enter your 1st float number :"))
d=float(input("Enter your 2nd float number :"))
print("The sum of the number is :", c+d)

e=float(input("Enter the number :"))
print("The half of the number is :", e/2)

f=float(input("Enter length :"))
g=float(input("Enter width :"))
print("The area of the rectangle is :", f*g)

r=float(input("Enter the radius :"))
π=3.14
print("Area of the circle is :", π*r**2)

#
#Mixed int & float Questions 
#16. Take one integer and one float as input and print both. 
#17. Take total marks (int) and number of subjects (int) and print the average as float. 
#18. Take price (float) and quantity (int) and print the total cost. 
#19. Take two numbers (one int, one float) and print their sum. 
#20. Take salary (float) and bonus (int) and print the final salary. 
#

a=int(input("Enter integer :"))
b=float(input("Enter float :"))
print("Integer is :",a, "and float is :",b)
c=int(input("Enter the total marks :"))
d=int(input("Enter the number of subjects :"))
avg=float(c/d)
print("The average is :", avg)

p=float(input("Enter the price :"))
q=float(input("Enter the quantity :"))
tc=float(p*q)
print("The total cost is :",tc)

a=int(input("Enter the 1st integer no. :"))
b=float(input("Enter 2nd float no. :"))
print("The sum of the number is :",a+b)

s=float(input("Enter the salary :"))
b=int(input("Enter the bonus :"))
print("The total salary is :",s+b)




              
              
