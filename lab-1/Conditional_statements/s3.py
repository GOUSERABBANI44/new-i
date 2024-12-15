import sys

type = sys.argv[1]

if type == "t2.micro":
    print("It will charge 2 dollers per day")
elif type == "t2.medium":
    print("It will charge 4 dollers per day")    
elif type == "t2.xlarge":
    print("It will charge 6 dollers per day")        
else:
    print("Enter a valid instance type like t2.micro, t2.medium and t2.xlarge")
