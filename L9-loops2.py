cars = ['bmw', 'vw', 'seat', 'skoda', 'lada']

for x in cars:
    print(x.upper())


for x in range (1, 6):
    print(x)

mynumber_list = list(range(0, 10))
print(mynumber_list)
print("==============================================")

for x in mynumber_list:
    x = x * 2
    print(x)

mynumber_list.sort(reverse=True)
print(mynumber_list)