#A. Python IF (Single Condition) 
#1. Write a Python program to check if a number is positive.
'''
a=int(input("Enter the number :"))
if a%2==0:
    print("Even number")
else:
     print("Odd number")
'''
'''
 #2. Print "Eligible to vote" if age is 18 or above.
age=int(input("Enter the age :"))
if age>=18 :
         print("Eligible to vote")
else :
        print("cannot vote")

 #3. Check if a number is divisible by 7.
b=int(input("Enter the number :"))
if b%7==0 :
            print("Number is divisible by 7")
else :
            print("Number is not divisible by 7")

#4. Print "Pass" if marks are greater than 40.
marks=float(input("Enter your marks : "))
if marks>40 :
        print("Pass")
else :
        print("Fail")

#5. Check if a number is greater than 100. 
n=int(input("Enter the number : "))
if n>100 :
        print("Number is greater than 100")
else :
        print("Number is less than 100")

#6. Display a message if temperature exceeds 45°C.
t= int(input("Enter the temperature :"))
if t>45 :
         print("Temperature exceeds 45 degree")
else :
        print("Temperature is less than 45 degree")

#7. Check if a string length is more than 8 characters. 
str = input("Enter the strings : ")
if len(str)>8 :
         print("String length is more than 8 characters")
else :
         print("String is less than 8 characters")
         
#8. Print "Logged In" if password matches "admin123". 
p=input("Enter the password :")
password = 'admin123'
if p == password :
    print("Logged In")
else :
    print("Wrong password")
            
#9. Check if a number is a multiple of 10. 
m=int(input("Eter the number : "))
if m%10==0 :
    print("Number is multiple of 10")
else :
    print("Number is not divisibleby 10")

#10. Print a warning if balance is below minimum limit. 
b=float(input("Enter the balance amount to withdraw:"))
limit=10000
if b<limit :
    print("Low balance")
else :
    print("Sufficient balance to withdraw")



B. Python IF–ELSE (Two Conditions) 
11. Check whether a number is even or odd. 
12. Find the largest of two numbers. 
13. Check whether a person is eligible for driving license. 
14. Print "Pass" or "Fail" based on marks. 
15. Check whether a number is positive or negative. 
16. Check whether a character is a vowel or consonant. 
17. Check if a year is leap or not. 
18. Print "Valid Password" or "Invalid Password". 
19. Determine whether salary is taxable or not. 
20. Check whether a number is greater than 50 or not. 

num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print("Largest:", num1)
else:
    print("Largest:", num2)

    
age = int(input("Enter your age: "))

if age >= 18:
    print("Eligible for driving license")
else:
    print("Not eligible for driving license")


marks = int(input("Enter marks: "))

if marks >= 40:
    print("Pass")
else:
    print("Fail")


num = int(input("Enter a number: "))

if num >= 0:
    print("Positive")
else:
    print("Negative")


ch = input("Enter a character: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")


year = int(input("Enter a year: "))

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")




password = input("Enter password: ")

if len(password) >= 8:
    print("Valid Password")
else:
    print("Invalid Password")


    salary = float(input("Enter salary: "))

if salary > 500000:
    print("Taxable")
else:
    print("Not Taxable")



num = int(input("Enter a number: "))
if num > 50:
    print("Greater than 50")
else:
    print("Not greater than 50")

'''


'''
C. Python NESTED IF–ELSE 
21. Find the largest of three numbers. 
22. Check whether a number is positive, negative, or zero. 
23. Assign grades: 
● A → marks ≥ 90 
● B → marks ≥ 75 
● C → marks ≥ 60 
● Fail → below 60 
24. Check whether a triangle is equilateral, isosceles, or scalene. 
25. Check whether a character is uppercase, lowercase, digit, or special character. 
26. Calculate electricity bill using slab-wise rates. 
27. Validate login using username and password. 
28. Check student result using marks of 3 subjects. 
29. Find the second largest number among three numbers. 
30. Check loan eligibility using age, salary, and credit score. 


a=int(input(" Enter 1st number :"))
b=int(input(" Enter 2nd number :"))
c=int(input(" Enter 3rd number :"))

if a>b and a>c :
  print("Largest is : ", a)
elif b>a and b>c:
  print("Largest is :",b)
else :
  print("Largest is :",c)

m=int(input("Input the marks : "))
if m>=90 :
  print("A grade")
elif m>=75 :
  print("B grade")
elif m>=60 :
  print("C grade")
else :
  print("Fail")

print("Enter the sides of triangle :")
s1=int(input("Enter first side :"))
s2=int(input("Enter second side :"))
s3=int(input("Enter third side :"))
if s1==s2 and s1==s3 :
  print("Equilateral triangle")
elif s1==s2 or s1==s3 or s2==s3 :
  print("Isosceles triangle")
else :
  print("Scalen triangle")


ch=input("Enter the character :")
if len(ch)!=1 :
  print("Enter exactly one character.")
elif ch.isupper() :
  print(ch, "is an uppercase letter.")
elif ch.islower() :
  print(ch, "is a lowercase letter.")
elif ch.isdigit() :
  print(ch, "is a digit.")
else :
  print(ch, "is a special character.")

  
#26. Calculate electricity bill using slab-wise rates. 
units= float(input("Enter the units of electricity consumed"))
fixed_charge =50.0
bill=0.0

if units<=100:
  bill=units*3.00
  
elif units<=200 :
  #units are between 101 and 200
  #first 100 units at 3.00 Rs and remaining units at 4.50
  bill=(100*3.00) +((units-100)*4.50)

else :
  #Units is above 200
  #first 100 at 3rs/unit next 100 at 4.5rs/unit and remaining units at 6.00/unit
  bill =(100*3.00) + (100*4.50) +((units-200)*6.00)
  
  total_amount = bill+fixed_charge
  
print("--- Electricity Bill Statement ---")
print(f"Units Consumed: {units}")
print(f"Energy Charges: ₹{bill:}")
print(f"Fixed Charges : ₹{fixed_charge:}")
print(f"Total Bill    : ₹{total_amount:}")


#27. Validate login using username and password. 
Correct_username= 'admin123'
Correct_password= 'password123'

username_input=input("Enter username")
password=input("Enter password")

if username_input==Correct_username and password==Correct_password :
  print("Login successful welcome back.")

elif username_input==Correct_username and password!=Correct_password :
  print("Incorrect password try again.")

elif username_input!=Correct_username and password==Correct_password :
  print("Incorrect username try again.")

else :
  print("Login failed.")  
 

 #28. Check student result using marks of 3 subjects. 
 # 1. Take marks input for 3 subjects
sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

# Define passing criteria per subject (e.g., 40 out of 100)
PASS_MARK = 40.0

# 2. Check for individual subject failure first
if sub1 < PASS_MARK or sub2 < PASS_MARK or sub3 < PASS_MARK:
    print("\nResult: FAILED")
    print("Reason: You did not clear the minimum passing marks in one or more subjects.")

else:
    # 3. Calculate percentage if passed in all subjects
    total_marks = sub1 + sub2 + sub3
    percentage = (total_marks / 300) * 100
    
    print(f"\nTotal Marks: {total_marks} / 300")
    print(f"Percentage : {percentage:.2f}%")
    
    # 4. Determine division based on percentage
    if percentage >= 60:
        print("Result     : PASSED (First Division) 🥇")
    elif percentage >= 50:
        print("Result     : PASSED (Second Division) 🥈")
    elif percentage >= 40:
        print("Result     : PASSED (Third Division) 🥉")
    else:
        print("Result     : FAILED ❌")


#29. Find the second largest number among three numbers. 
# 1. Take three numbers as input
num1 = float(input("Enter first number (A): "))
num2 = float(input("Enter second number (B): "))
num3 = float(input("Enter third number (C): "))

# 2. Find the second largest using if-elif-else
if (num2 >= num1 >= num3) or (num3 >= num1 >= num2):
    # Condition 1: A is between B and C
    second_largest = num1

elif (num1 >= num2 >= num3) or (num3 >= num2 >= num1):
    # Condition 2: B is between A and C
    second_largest = num2

else:
    # Condition 3: If neither A nor B is middle, then C is middle
    second_largest = num3

# 3. Print the result
print(f"The second largest number is: {second_largest}")
 
#30. Check loan eligibility using age, salary, and credit score. 
# 1. Input applicant details
age = int(input("Enter applicant's age: "))
salary = float(input("Enter monthly salary (in ₹): "))
credit_score = int(input("Enter credit score (300-900): "))

# Define Bank Standards
MIN_AGE = 21
MAX_AGE = 60
MIN_SALARY = 30000.0
MIN_CREDIT_SCORE = 750

# 2. Check for loan eligibility using if-elif-else
if age < MIN_AGE or age > MAX_AGE:
    # Condition 1: Age out of bounds
    print("\nLoan Status: REJECTED ❌")
    print(f"Reason: Age must be between {MIN_AGE} and {MAX_AGE} years.")

elif salary < MIN_SALARY:
    # Condition 2: Income too low
    print("\nLoan Status: REJECTED ❌")
    print(f"Reason: Monthly salary must be at least ₹{MIN_SALARY:,.2f}.")

elif credit_score < MIN_CREDIT_SCORE:
    # Condition 3: Bad credit history
    print("\nLoan Status: REJECTED ❌")
    print(f"Reason: Minimum required credit score is {MIN_CREDIT_SCORE}.")

else:
    # Condition 4: Passed all individual parameter tests
    print("\nLoan Status: APPROVED_ELIGIBLE  🎉")
    print("Congratulations! You meet all the eligibility criteria for the loan.")

'''
