
import json
filename = "user_settings.txt"
myfile = open(filename, mode='w', encoding='utf_8')

player1 = {
    'PlayerName': "Barak Obama",
    'Score': 345,
    'awards': ["OR", "NV", "NY"]
}


player2 = {
    'PlayerName': "Clinton Hillary",
    'Score': 346,
    'awards': ["WT", "TX", "MI"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

#---------------------SAVE by JSON--------------------

json.dump(myplayers, myfile)
myfile.close

#--------------------LOAD by JSON--------------------

myfile = open(filename, mode='r', encoding='utf_8')
json_data = json.load(myfile)

for user in json_data:
    print("Player Name is: " + str(user['PlayerName']))
    print("Player Score is: " + str(user['Score']))
    print("Player Award N1: " + str(user['awards'][0]))
    print("Player Award N2: " + str(user['awards'][1]))
    print("Player Award N3: " + str(user['awards'][2]))
    print("------------------------------------\n\n")