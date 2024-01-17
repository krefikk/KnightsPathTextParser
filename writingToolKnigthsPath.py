f1 = open("neededLines.txt", "r")
f2 = open("KP_EN.po", "r")

listOfAllTxtLines = f1.readlines()
listOfAllTrLines = f2.readlines() 
f1.close()
f2.close()

k = 0
for line in listOfAllTxtLines:
    line = line[:-1]
    line = 'msgstr "' + line + '"'
    line = line + "\n"
    listOfAllTxtLines[k] = line
    k += 1

j = 0
i = 0
for line in listOfAllTrLines:
    if "msgstr " in line:
        listOfAllTrLines[i] = listOfAllTxtLines[j]
        j += 1
    i += 1

f3 = open("KP_NEW.po", "w")
f3.close()

f4 = open("KP_NEW.po", "a")

for line in listOfAllTrLines:
    f4.write(line)

f4.close()

