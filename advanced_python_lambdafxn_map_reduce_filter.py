'''
def cube(num):
    return num**3
print(cube(9))
print (cube(2))

#Advance Python
#lambda Expression
 #   map , filter , reduce

 ##function_name=lambda parameter : definition

 #Lambda expression

cube= lambda num : num**3

print(cube(3))
print(cube(5))


# By normal fxn
def checkeven(num):
    if num%2==0:
        return 'Even'
    else :
        return 'Odd'

li=[1,2,3,4,5,6,7,8,9,10]
for i in li:
    print(i, '\t', checkeven(i))

#Same question using Lambda fxn    

checkeven=lambda num: 'Even' if num%2==0 else 'odd'
for i in li:
    print(i, '\t', checkeven(i))
#or________________________________________________________________________

checkeven=lambda num : num%2==0
li = [23,45,67,78,7665,43,32,4,56,78]
for i in li:
     print(i, '\t', 'Even' if checkeven(i) else 'Odd')

square= lambda num : num**2

li=[1,2,3,4,5,6,7,8,9]
for i in li:
    print(i, '\tSquare-->', square(i))
'''
#________________________________________________________________________________________________________________
    # map , filter , reduce

square =lambda num : num**2

li=[1,2,3,4,5,6,7,8,9]
print(li)
res=list(map(square, li))
print(res)


cube=lambda num:num**3
li=[1,2,3,4,5,6,7,8]
res=list(map(cube, li))
print(res)


#FILTER______________________________________________________
checkEven=lambda num: num%2==0
li=[1,2,3,4,5,6,7,8]
for i in li:
    if checkEven(i):
        print(li)

#BY using FILTER
checkEven=lambda num :num%2==0

li=[3,45,67,78,4,6,8,2]
res=list(filter(checkEven, li))
print(res)

#REDUCE____________________________
add= lambda a,b : a+b
li=[1,2,3,4,5,6,7,8,9]
res=0
for i in li:
    res=add(res, i)
print(res)


#Using Reduce
from functools import reduce
add= lambda a,b : a+b
li=[1,2,3,4,5,6,7,8,9]
res= reduce(add , li)
print(res)



#*********
# WAP to add cubes of all even numbers of a list

from functools import reduce
li=[2,3,4,5,5,5,5,7,7,8,8,9,5,4]
res=filter(lambda num : num%2==0, li)
res=map(lambda num : num**3 ,res)
res=reduce(lambda a,b: a+b , res)
print(res)
        
