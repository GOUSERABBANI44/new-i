total = 0
while True:
    number = float(input("ENter the positive value, if you enter negative value loop will break: "))
    if number < 0:
        break
    total += number
print(total)