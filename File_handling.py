'''
File Handling:- To write/read data from a file
Two types
1- Text File (.xlsx , .txt , .csv etc)
2- Binary File  (.bin , .dat etc)

file_handler = open('file_name.extension','mode')
mode:- r , w , a , r+ , w+ , a+

TEXT FILE

file = open('student.txt' , 'w') # we use 'w' ,suppose we dont created any student.txt file in folder and want to write something directly creating a folder from here..
                                 #so use 'W' to write/create a folder (i.e student.txt) if not exist
file.close()


#WAP to write data in a file

file= open('student.txt' , 'w')
file.write("Hello India")
file.close()

file = open('student.txt','w')
file.write("Hello World")
file.close()

# but 'w' erase the older entered data once we enter a new data using file.write() code
# so usex 'a' ie. (append) it will keep older as well as newly entered text in text file
file = open('student.txt','a')
file.write("\n Yashu")
file.close()

file = open('student.txt','a')
file.write("\n Sudhanshu Pandey")   # 'a' will keep all older data and newly written data means, (Hello India hello World Yashu Sudhanshu Pandey )
file.close()

# using write method you can write only one data point
# To write multiple data points

names = ['\nAnu','\nManu','\nYogesh']
file = open('student.txt','a')
file.writelines(names)
file.close()

# To read data from a text file

file = open('student.txt','r')
data = file.read()    # read all data from a file
print(data)
file.close()

file = open('student.txt','r')
data = file.read(20)   # read only 20 characters
print(data)
file.close()

file = open('student.txt','r')
data = file.readline()  # Read only one line
print(data)
file.close()


file = open('student.txt','r')
data = file.readline()  # Read first line
print(data)
data = file.readline()  # Read second line
print(data)
data = file.readline()  # Read third line
print(data)
file.close()

file = open('student.txt','r')
data = file.readlines()  # read all lines in a list
print(data)
file.close()


file = open('student.txt','r')
data = file.readlines()
for names in data:
    print(names)
file.close()


file = open('student.txt','r')
data = file.readlines(25)
print(data)
file.close()

'''
