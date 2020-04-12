inputfile = "../user_names.txt"

myfile = open(inputfile, mode='r', encoding='utf_8')

for num, line in enumerate(myfile, 1):
    if "Bosch" in line:                                      # look for 'Bosch' in user_names.txt file
        print("Line # " + str(num) + " : " + line.strip())


password_tolookfor = "petya"    # find pass with 'petya'


inputfile = "../passwords.txt"
outputfile = "../mypasswords.txt"

myfile1 = open(inputfile, mode='r', encoding='latin_1')
myfile2 = open(outputfile, mode='a', encoding='latin_1')   # if key "w" - write always new file. If key "a" -append, add to already exists file 

for num, line in enumerate(myfile1, 1):
    if password_tolookfor in line:
        print("Line # " + str(num) + " : " + line.strip())
        myfile2.write("Found password: " + line)




myfile1.close()
myfile2.close()
