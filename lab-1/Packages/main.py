# importing modules from package directory and package directory name is my_package
import my_package

#callling the functions with package directory name
addition = my_package.add(5, 10)
subtraction = my_package.sub(20, 8)

upper_case = my_package.to_upper("rabtha")
lower_case = my_package.to_lower("Rabbani")

print(f"the two numbers addition: {addition}")
print(f"the two numbers subtraction: {subtraction}")

print(f"the string uppercase: {upper_case}")
print(f"the string lowercase: {lower_case}")
