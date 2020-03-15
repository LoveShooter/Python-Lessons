for x in range(0, 100 + 1):
    print (x)
    print ("****")
    print ("---------")

for x in range(10, 100, 2):  ## step 2
    print (x)
    print ("Number x = " + str(x))   ## x = *
    if x == 50:
        break  ## break on 50

print ("---------EndOfFile--------")


x = 1
while True:
    print (x)
    x = x + 1    ## бесконечно идет счет
    if x == 100: 
        break    ## break if 99 (счет с 0)