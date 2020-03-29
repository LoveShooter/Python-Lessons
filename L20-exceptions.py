filename = "../user_names.txt"


try:
    print("Inside TRY")
    myfile = open(filename, mode='r', encoding="utf_8")
except Exception:
    print("Inside EXCEPT")
    print("Error found!")
else:
    print("Inside ELSE")
    print(myfile.read())
finally:
    print("Inside FINALLY")



print("==========================EOF========================")
