age = int(input ("Your age: "))    ## with input

if (age <=4):
    print ("You are baby!")
elif (age > 4) and (age < 12):
    print ("You are kid")
elif (age >= 12) and (age < 19):
    print ("You are teenager")
else:
    print("You are old!")


print("---END---")

all_cars = ['chrysler', 'dacia', 'bmw', 'kia', 'vw', 'seat', 'skoda', 'lada', 'audi', 'ford', 'Chevrolet']
german_cars = ['bmw', 'vw', 'audi']


if 'lada' in all_cars:
    print("Yes LADA is in the list")
else:
    print("LADA Not in the list")


for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + " is German car")
    else:
        print(xxxx + " is not German car")    

