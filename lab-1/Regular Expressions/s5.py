import re

pattern = r"\d+"  # One or more digits
string = " 3 cats, 4 dogs, and 5 birds 9  10 12 20.56"
result = re.findall(pattern, string)

print(result) # displays numerical or integers  