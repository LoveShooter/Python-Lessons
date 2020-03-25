name = input("Please Enter your name: ")

print("Helo " + name)

num1 = input("Enter X: ")
num2 = input("Enter Y: ")

sum = int(num1) + int(num2)
print(sum)


message = ""

while message != 'sekret':
    message = input("Enter password: ")
    if message == 'sekret': 
        break 
    print(message + " Password not correct")

print("Password was:" + message)