import sys

filename = "user_names.txt"

while True:  #вечный цикл
    try:
        print("Inside TRY")
        myfile = open(filename, mode='r', encoding="utf_8")
    except Exception:
        print("Inside EXCEPT")
        print("Error found!")
        filename = input("Enter correct filename: ")
        sys.exit()
    else:
        print("Inside ELSE")
        print(myfile.read())
        sys.exit               #чтобы не получился вечный цикл - выйти из этой бибилотеки.
    finally:
        print("Inside FINALLY")



print("==========================EOF========================")
