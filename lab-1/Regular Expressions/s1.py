import re #this regular expression module will help you out to findout the logs of the files(like errors, warnings etc...)
task = "Hello Rabbani how are you"
new = r"how"
result = re.match(new, task)
print(result)