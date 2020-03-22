cities = ['New York', 'Moscow', 'new dehli', 'Simferopol', 'Toronto']

print(cities)
print(len(cities))

print(cities[0]) # 1 city in list
print(cities[-2]) # 2 city from end
print(cities[2].upper())

cities[2] = 'Tula'
print(cities)

cities.append('Kursk') #add variable after all
cities.append('Yalta')
print(cities)

cities.insert(2, 'Feodosiya') #add new variable on 2 position


del cities[-1]  #del variable on 1 position from end
print(cities)

cities.remove('Tula') #search and delete this variable
print(cities)

deleted_city = cities.pop()   #find deleted variable
print("Deleted city is: " + deleted_city) #print deleted variable
print(cities)


cities.sort()
print(cities)

cities.sort(reverse=True)
print(cities)

cities.reverse()
print(cities)



