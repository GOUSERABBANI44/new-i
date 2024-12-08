# list data type--> Sequence
new = [1, 22, 44, 55]
print(new)
servers = ["10.0.0.0", "10.0.0.1", "10.0.0.2"]
print("servers ip's:", servers)

new[0] = 10
print("replacement Values:", new)

new[1] = 20
print("replacement Values:", new)

servers.append("10.0.0.3")
print("added ips:", servers)