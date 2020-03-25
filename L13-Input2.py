mylist = []
msg = ""


while msg != 'stop'.upper():  #не равен
    msg = input('Enter new item and STOP to finish:')
    mylist.append(msg)


print(mylist)



