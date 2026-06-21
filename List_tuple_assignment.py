'''
Python Programming Questions – LIST 
Basic Level 
1. Write a Python program to create a list of integers and print its elements. 
2. Write a program to find the sum and average of all elements in a list. 
3. Write a program to find the largest and smallest element in a list. 
4. Write a Python program to count the number of elements in a list without using len(). 
5. Write a program to reverse a list without using built-in functions. 
6. Write a program to check if an element exists in a list. 
7. Write a Python program to remove duplicate elements from a list. 
8. Write a program to sort a list in ascending and descending order.

#1. Write a Python program to create a list of integers and print its elements.
li=[1,2,3,4,5,6,7,8]
for i in li:
    print(i)

for i in range(len(li)):
    print(i)
#2. Write a program to find the sum and average of all elements in a list.
L=[1,2,3,4,5,6,7,8,9]
sum=0
count=0
for i in L:
    sum=sum+i
    count=count+1

print("Sum of all elements are: ", sum)
Avg=sum//count
print("Average of all elements are: ", Avg)
    
#3. Write a program to find the largest and smallest element in a list.
L=[1,2,3,4,5,6,7,8,9]
print("The largest element is:", max(L))
print("The smallest element is:", min(L))


#4. Write a Python program to count the number of elements in a list without using len(). 
count=0
for i in L:
    count=count+1
print("The number of elements in the list are:", count)

#5. Write a program to reverse a list without using built-in functions.
List=[1,2,3,4,5]
for i in range(len(List)-1,-1,-1):
    print(List[i])
#6. Write a program to check if an element exists in a list.
l=[12,23,34,45,4,12,13,12]
l.count(12)  #3 use this logic

target =15
if l.count(15)>0:
    print(target, "is present")
else:
    print(target, "is not found in the given list")
     
#7. Write a Python program to remove duplicate elements from a list. 
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 2, 2, 33, 4, 3]
res = []
for i in li:
    if i not in res:
        res.append(i)
print(res)

#OR___________________

li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 1, 2, 2, 33, 4, 3]
res=set(li)  # keep the list in a set because set always remove duplicate values automatically
print(res)
print(list(res))

#8. Write a program to sort a list in ascending and descending order.
li=[1,2,3,4,5,6,9,8,11,15,12,10]
li.sort()
print("Ascending:" , li)

li.sort(reverse=True)
print("Descending:" , li)

Intermediate Level 
9. Write a program to merge two lists and remove duplicates. 
10. Write a program to find common elements between two lists. 
11. Write a program to split a list into even and odd numbers. 
12. Write a program to rotate a list by n positions. 
13. Write a Python program to find the second largest number in a list. 
14. Write a program to flatten a nested list. 
15. Write a program to count frequency of each element in a list. 
16. Write a program to replace all negative numbers with zero in a list. 


#9. Write a program to merge two lists and remove duplicates. 
L1=[1,3,2,5,6,4,8,9,15]
L2=[10,11,13,12,14]

res=set(L1+L2)
print(res)
print(list(res))

#10. Write a program to find common elements between two lists. 
L1=[1,3,2,5,6,4,8,9,15]
L2=[1,2,3,4,5,10,11,13,12,14]

S1=set(L1)
S2=set(L2)
res=S1.intersection(S2)
print(res)

#11. Write a program to split a list into even and odd numbers.
L1=[1,2,3,4,5,10,11,13,12,14]
even_list=[]
odd_list=[]
for i in L1:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)

print("Even number list:" , even_list)
print("Odd number list:" , odd_list)

#12. Write a program to rotate a list by n positions.
li=[10,20,30,40,50,60,70,80]
def rotate_list(li,n):
    n=n%len(li)
    return li[n:] + li[:n]

print(rotate_list(li, 4))

#*****13. Write a Python program to find the second largest number in a list. 

li = [10, 45, 4, 99, 99, 23, 7]
s1=set(li)  # now, no any duplicate value present
print(s1)
Shorted_set=sorted(s1) # list will be sorted ascending order
Second_largest=Shorted_set[-2]      # largest will be at last index and second largest will be at second laast index i.e. at [-2] index
print("Second largest number is :", Second_largest)

#14. Write a program to flatten a nested list.
nested_list=[[1,2,3], [4,5], [6,7,8]]
flat_list=[]

for i in nested_list:
    flat_list.extend(i)   #extend(): unpack all the items directly ie flattened the list 
                          # append() :Adds the whole list as ONE item do not unpack    
print(flat_list)

#15. Write a program to count frequency of each element in a list. 
#16. Write a program to replace all negative numbers with zero in a list. 
li=[1,2,3,4,-1,-2,-3,-4]
for i in range(len(li)):
    if li[i] < 0:
        li[i] = 0  # Replace negative number with 0

print(li)

Advanced Level 
17. Write a program to remove all occurrences of a given element from a list. 
18. Write a program to check if a list is a palindrome. 
19. Write a Python program to find missing numbers in a given list of consecutive integers. 
20. Write a program to perform element-wise addition of two lists. 
21. Write a Python program to find the longest increasing subsequence in a list. 
22. Write a program to group elements based on frequency. 
  '''
#17. Write a program to remove all occurrences of a given element from a list.

def remove_occurrence(input_list, target):
    for i in input_list:
        if i==target:
            input_list.remove(target)
    return input_list

input_list=[1,2,3,4,5,2,4,2,5,2]
target=2

print(remove_occurrence(input_list, target))

#Or________________
li=[1,2,3,4,20,30,20]
target=20
for i in li:
    if i==target:
        li.remove(target)
print(li)        

#18. Write a program to check if a list is a palindrome. 

li = [1, 2, 3, 2, 1]
reversed_list = list(reversed(li))
if li == reversed_list:
    print("The list is a palindrome.")
else:
    print("The list is NOT a palindrome.")

#19. Write a Python program to find missing numbers in a given list of consecutive integers.
li =[1,2,4,5,7,9,10]
lowest = min(li)
highest = max(li)

missing = []
for i in range(lowest, highest + 1):
    if i not in li:
        missing.append(i)
print("Missing numbers:", missing)

#20. Write a program to perform element-wise addition of two lists.
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
result=[]

for i in range(len(l1)):
    total=l1[i]+l2[i]
    result.append(total)
print("Sum of lists: ", result)    

#21. Write a Python program to find the longest increasing subsequence in a list. 
#22. Write a program to group elements based on frequency. 

