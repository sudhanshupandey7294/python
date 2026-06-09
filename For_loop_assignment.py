'''
#Q1. Print Numbers 
#Use a for loop to print numbers from 1 to 10.

for i in range(1,11) :
    print(i)

#Q2. Print Even Numbers 
#Print all even numbers between 1 and 20.
for i in range(1,21):
     if i%2==0 :
        print(i)
           
#Q3. Find Sum 
#Print the sum of numbers from 1 to 10 using a for loop.
sum=0
for i in range(1,11):
  sum+=i
print(sum)

#Q4. Multiplication Table 
#Take a number from the user and print its multiplication table up to 10.
num =int(input("Enter a number : "))
for i in range(1,11) :
    print(num,"*",i,"=",num*i)

#Q5. Count Characters 
#Take a string and count the total number of characters using a for loop.    
count=0
string=input("Enter the characters :")
for char in string :
    count+=1
print("Total characters:", count)

#PART 2 – Break Related Questions 
#Q6. Stop at 5 
#Print numbers from 1 to 10. 
#Stop the loop when the number becomes 5.

for i in range(1,11):
     print(i)
     if i==5 :
         break

#Q7. Search in List 
#Search for number 25 in a list. 
#If found, print "Found" and stop the loop.

l=[1,2,3,4,5,6,7,8,25]
for i in l:
    if i==25:
        print("Found")
        break

#Q8. First Negative Number 
#Given a list of numbers, print the first negative number and stop the loop.
neg=0
l=[1,2,3,4,5,6,7,8,2,-5,-1,-3]
for i in l:
    if i<0:
        print(i)
        break


#Q9. Skip 5 
#Print numbers from 1 to 10. 
#Skip number 5.
for i in range(1,11):
    if i==5 :
        continue
    print(i)

#Q10. Skip Even Numbers 
#Print numbers from 1 to 20. 
#Skip all even numbers.
for i in range(1,21) :
    if i%2==0:
        continue
    print(i)


#Q11. Skip Letter 
#Print each character of the string "PYTHON". 
#Skip the letter "O".
text="PYTHON"
for char in text:
    if char=="O":
        continue
    print(char)

#PART 4 – Pass Related Questions 
 
#Q12. Empty Loop 
#Run a loop from 1 to 5 but do nothing inside the loop using pass.
for i in range(1,6):
    pass
 
#Q13. Skip Using Pass 
#Loop from 1 to 10. 
#If number is 6, just use pass. 
for i in range(1,11):
    if i==6 :
        pass
    else :
        print(i)
'''
#Q14. Search Number Using for-else 
#Search for number 100 in a list. 
#If found, print "Found". 
#If not found, print "Not Found". 

listL=[1,2,3,4,5,6,7,99,100]
for i in listL:
    if i == 100:
        print("Found")
        break
    else:
            print("Not Found")
   
#Q15. Prime Number Check 
#Take a number from the user and check whether it is prime using for-else.
count = 0
a = int(input("Enter any number :"))

for i in range(1, a + 1):
    if a % i == 0: 
        count = count + 1
        print("The factors of the number are :", i)
        
    # Check if it fails the prime test early
    if count > 2:
        print("Not a Prime number")
        break
else:
    # The loop finished without breaking. Now we check the final count!
    if count == 2:
        print("Prime number")
    else:
        print("Not a Prime number")
    


