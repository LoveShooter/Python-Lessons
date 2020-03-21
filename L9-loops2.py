##________0______1_____2________3________4_____
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

for x in cars:
    print(x.upper())  ## all upper letters


for x in range (1, 6):
    print(x)            ## from 1 to 5 

mynumber_list = list(range(0, 10))
print(mynumber_list)
print("==============================================")   

for x in mynumber_list:
    x = x * 2
    print(x)    ## loop numbers from 0-9 and *2

mynumber_list.sort(reverse=True)
print(mynumber_list)     ## revers number list

print("Max number is: " + str(max(mynumber_list)))    #max number from list
print("Min number is: " + str(min(mynumber_list)))    #min number from list
print("Sum of list is: " + str(sum(mynumber_list)))   #summary list numbers



##________0______1______2_______3________4_____
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

mycars = cars[1:4]   ## range of list
print(mycars)        

mycars = cars [:4]  ## from 0 to 4
print(mycars)

mycars = cars [-3:-1]  ## ?
print (mycars)


##________0______1_____2________3________4_____
cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']
mycars = cars [:]   ## all range
print(mycars)