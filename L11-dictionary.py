#       (-----Item-----)
#       (key)    (value)

enemy = {
        'loc_x': 70,
        'loc_y': 50,
        'color': 'green',
        'health': 100,
        'name': 'trololo'

}

print(enemy)

print("Location X = " + str(enemy['loc_x']))
print("Location Y = " + str(enemy['loc_y']))
print("Enemy name: " + enemy['name'])

enemy['rank'] = 'General'
print(enemy)


del enemy['rank']
print(enemy)

enemy['loc_x'] = enemy['loc_x'] + 40
enemy['loc_y'] = enemy['loc_y'] + 20
enemy['health'] = enemy['health'] - 30
if enemy['health'] < 80:
    enemy['color'] = enemy['color'] = 'yellow'
    
print(enemy)
