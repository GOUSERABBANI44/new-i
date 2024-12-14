import sys

#print all command line arguments
print("print all arguments:", sys.argv)

#print file name
print("file name:", sys.argv[0])

if len(sys.argv) == 2:
    output = int(sys.argv[1])
    print("first argument:", output)
elif len(sys.argv) > 2:
    output = int(sys.argv[2])
    print("second argument:", output)    
else:
    print("No Arguments passed")
