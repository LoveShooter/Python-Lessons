#       (-----Item-----)
#       (key)    (value)

enemy = {
        'loc_x': 70,
        'loc_y': 50,
        'color': 'green',
        'health': 100,
        'name': 'trololo',
        'image': ['image1.jpg', 'image2.jpg', 'image3.jpg']

}

all_enemies = []   #все враги и равны нашему массиву

for x in range(0, 10):                    #add 10 new enemies
        all_enemies.append(enemy.copy())  #copy enemy from dictionary

for ene in all_enemies:
        print(ene)

all_enemies[5]['health'] = 30             #-30 health  = 5 enemy
all_enemies[8]['name'] = "asshole"
all_enemies[2]['loc_x'] += 10


print("-------------------------------")


for ene in all_enemies:
        print(ene)
