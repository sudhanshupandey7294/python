'''Python While Loop Exercise 
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


'''
    
