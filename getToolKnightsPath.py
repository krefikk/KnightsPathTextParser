f1 = open("KP_EN.po", "r")
f2 = open("neededLines.txt", "w")
f2.close()
f3 = open("neededLines.txt", "a")

listOfAllLines = f1.readlines() 
f1.close()

count = 0
for line in listOfAllLines:
    if "msgstr " in line:
        count += 1

i = 0
listOfNeededLines = ["None"] * count

for line in listOfAllLines:
    if "msgstr " in line:
        line = line.strip()
        line = line[8:]
        line = line[:-1]
        listOfNeededLines[i] = line
        i += 1

for line in listOfNeededLines:
    f3.write(line)
    f3.write("\n")

f3.close()



