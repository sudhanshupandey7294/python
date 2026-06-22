'''
#File Handling in binary
____________________________________

File Handling (Text , Binary)
Binary File (data stores in the form object)

syntax:
file_handler = open( 'filename.extension' , 'mode' )
# mode => rb , wb ,  ab , rb+ ,  ab+ , wb+

import pickle
import joblib

dump => to write data
pickle.dump( 'data' , file_handler )
joblib.dump( 'data' , file_handler )

load => to read data
pickle.load(file_handler)
joblib.load(file_handler)
'''
# Example write the data
import pickle
file = open('employee.bin' , 'wb') # erase past data and write new data
pickle.dump('Sudhanshu Pandey' , file)
file.close()
#'wb' is only write binary it cannot keep the old data

import pickle
file = open('employee.bin', 'ab') # ab append binary add new data also keep old data
pickle.dump('Priyanshu pandey', file)
file.close()

# Reading the data
import pickle
file=open('employee.bin', 'rb')  #rb=read binary
for i in range(2):
    data=pickle.load(file)      # data stored in object form so we print it by using loop  2 means >>> 1st lteration = Sudhanshu pandey , 2nd loop is = Priyanshu pandey
    print(data)
file.close()


import pickle
file = open( 'employee.bin' , 'rb' )
try:
    while True:
        data = pickle.load(file)       # better is to use try and except bllock beacuse  if we dont know how much data in file to read ,,,so use While loop true..and it run continuosly
        print(data)
except:
    print("\nData Read Successfully!")
file.close()
