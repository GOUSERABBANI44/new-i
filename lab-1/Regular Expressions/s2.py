import re #this regular expression module will help you out to findout the logs of the files(like errors, warnings etc...)
task = "Hello Rabbani how are you"
new = r"Rabbani"
data = re.search(new, task)
if data:
   print(data.group())