"""
Python While Loop Exercise 
Part 1 – Basic Level 
1. Print numbers from 1 to 10 using a while loop. 
2. Print even numbers from 1 to 20. 
3. Print odd numbers from 1 to 20. 
4. Print numbers from 10 to 1 (reverse order). 
5. Print multiplication table of 5 using while loop. 

#1. Print numbers from 1 to 10 using a while loop.
i=1
while i<11 :
    print(i)
    i=i+1 
#2. Print even numbers from 1 to 20.
    i=1
    while i<21 :
        if i%2==0 :
            print(i)
        i=i+1



#3. Print odd numbers from 1 to 20.
i=1
while i<21 :
    if i%2!=0:
        print(i)
    i=i+1    

#4. Print numbers from 10 to 1 (reverse order). 
i=10
while i>0 :
     print(i)
     i=i-1
#5. Print multiplication table of 5 using while loop.
i=1
while i<11:
    print(5,'*',i,'=',5*i)
    i=i+1

#______________________________________________________________________________________________________________________
    Part 2 – Intermediate Level 
6. Find the sum of first 10 natural numbers using while loop. 
7. Find factorial of a number entered by user. 
8. Count number of digits in a given number. 
9. Reverse a number using while loop. 
10. Check whether a number is palindrome or not using while loop.

#6. Find the sum of first 10 natural numbers using while loop.
i=0
sum=0
while i<11: 
    sum=sum+i
    i=i+1
print("The total sum is :", sum)

#7. Find factorial of a number entered by user.
fact=1
i=int(input("Enter the number : "))
while i>0:
    fact=fact*i
    i=i-1
    
print("The factorial of the number is :", fact)
    

#8. Count number of digits in a given number.
count=0
i=int(input("Enter the number : "))
if i == 0:
    count = 1

while i>0 :
    count+=1
    i=i//10
print(" Total number of digits are : ",count)

#9. Reverse a number using while loop.
num=int(input("Enter the number you want to reverse :" ))
reversed_number=0            
while num>0 :
    remainder=num%10
    reversed_number=remainder+(reversed_number*10)
    num=num//10
print("Reversed number :", reversed_number)

#10. Check whether a number is palindrome or not using while loop.

original_num = int(input("Enter the number to check : "))
num = original_num  # Store a copy to compare later
reversed_num = 0

while num > 0:
    remainder = num % 10
    reversed_num = (reversed_num * 10) + remainder
    num = num // 10

# Compare the original copy with the reversed result
if original_num == reversed_num:
    print(f"{original_num} is a Palindrome.")
else:
    print(f"{original_num} is NOT a Palindrome.")



Part 4 – Logical / Real Scenario 
13. Ask user to enter password until correct password is entered. 
14. Create a number guessing game: 
• Generate a random number (1–10) 
• Keep asking user until they guess correctly 
15. Keep taking input numbers until user enters 0, then print total sum.
  
#13. Ask user to enter password until correct password is entered.
password='1234'
while True :
    a=input("Enter the password :")
    if a==password:
        print("Access granted!")
        break
    else:
        print("Incorrect password. Please try again. \n")
#________________________________________OR
password='1234'
a=input("Enter the password :")
while a!=password:
    print("Incorrect password, try again.\n")
    a=input("Enter the password :")

print("Access granted ")

#_______________________________________OR
CORRECT_PASSWORD = "secret_password"
user_input = ""

# The loop continues as long as the inputs do not match
while user_input != CORRECT_PASSWORD:
    user_input = input("Enter the password: ")
    
    if user_input != CORRECT_PASSWORD:
        print("Incorrect password. Try again.\n")

print("Access Granted!")


#______________________________________________________________________
    #14. Create a number guessing game: 
#• Generate a random number (1–10) 
#• Keep asking user until they guess correctly
import random
random_num=random.randint(1,10)
guess_num=0
while guess_num!=random_num:
    guess_num=int(input("Guess the number between 1 to 10 :"))
    
    if guess_num!= random_num:
       print("Wrong! Try again...")
       
print("Right guess, You win!.")


#_______________________________________________
#15. Keep taking input numbers until user enters 0, then print total sum.
input_num=1
sum=0
while input_num!=0:
    input_num=int(input("Enter the number :"))
    sum+=input_num

print("Total sum :",sum)
#______________________________________________________________
Bonus Challenge (Interview Level) 
16. Print Fibonacci series up to N terms using while loop. 
17. Check whether a number is Armstrong number. 
18. Print prime numbers between 1 to 50 using while loop.


#16. Print Fibonacci series up to N terms using while loop. 
N=int(input("Enter the number of terms: " ))
a=0
b=1
i=0
while i <N:
    print(a, end=",")
    a,b=b,a+b
    i+=1
#or____________________________
a=0
b=1
N=int(input("Enter the number of terms: "))
for i in range(N):
    print(a, end=",")
    c=a+b
    a=b
    b=c
   
#17. Check whether a number is Armstrong number. 
num=int(input("Enter a 3 number: "))

digit1=num//100  #To get 1st digit
digit2=(num//10)%10     #To get middle digit
digit3= num%10          #To get last digit

Total=digit1**3 + digit2**3 + digit3**3
if Total==num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

    
#18. Print prime numbers between 1 to 50 using while loop.
num=1

while num<=50:
    factors=0
    i=1
    while i<=num:
        if num%i==0:
            factors+=1
        i+=i
    if factors==2:
        print(num , end=" ")
num=num+i
#_______________________________________________________________or
print("Prime numbers between 1 and 50 are:")

# Start from 1 instead of 0
for num in range(1, 51):
    factors = 0
    
    # Start from 1 instead of 0 to avoid dividing by zero
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1
            
    if factors == 2:
        print(num, end=" ")
#___________________________________________________________
#THIS IS THE LOGIC IF NOT UNDERSTAND
        // Loop through numbers 1 to 50
        for (int num = 1; num <= 50; num++) {
            int factors = 0;

            // Count how many numbers divide 'num' perfectly
            for (int i = 1; i <= num; i++) {
                if (num % i == 0) {
                    factors++;
                }
            }

            // Prime numbers have exactly 2 factors (1 and itself)
            if (factors == 2) {
                System.out.print(num + " ");
            }
        }
    }
}
                
 """    
