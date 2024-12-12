#importing the os module
import os
#finding the present working directory
result = os.getcwd()
print(result)

#list out the files in present working directory
output = os.listdir(".") #here . indicates present path or wokrking path
print(output)

