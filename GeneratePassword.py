import random
password_length = int(input("Enter the length of Password:"))
combination = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%&*"
password = "".join(random.sample(combination,password_length))
print(password)
# dictionary = dict()
# key= input("Enter the name:")
# dictionary[key] = [password]
# print(dictionary)
