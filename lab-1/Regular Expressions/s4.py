import re
text = "hai this   is Gouse Rabbani Shaik i    am from Guntur and nick   name is Rabbani and my native is    Guntur"
new = r"\s+" 
data = re.sub(new, " ", text)
print(data)