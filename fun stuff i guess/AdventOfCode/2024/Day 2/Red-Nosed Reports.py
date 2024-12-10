data = open(r"2024\Day 2\data.txt").readlines()
testdata = open(r"2024\Day 2\example.txt").readlines()
newdata = []
errorcounterDecrease = 0
errorcounter = 0
safecounter = 0
tempdata = []


for item in data:
    newdata.append(list(map(int, item.strip("\n").split())))

def Linesafe(line):
    isdecreasing = True
    isincreasing = True
    for i in range(len(line) - 1):
        if line[i] > line[i + 1] and 0 < abs(line[i] - line[i + 1])< 4:
            if isdecreasing == True:
                isdecreasing = True
        else: isdecreasing = False
        if line[i] < line[i + 1] and 0 < abs(line[i] - line[i + 1])< 4 and isdecreasing == False:
            if isincreasing == True:
                isincreasing = True
        else: isincreasing = False
    if isincreasing == False and isdecreasing == False: return False
    return True

for line in newdata:
        for i, item in enumerate(line):
            tempdata.append(item)
            print(line)
            del line[i]
            print(line)
            if Linesafe(line):
                safecounter += 1
                line.insert(i, tempdata[0])
                tempdata.clear()
                print(safecounter)
                break
            line.insert(i, tempdata[0])
            tempdata.clear()

print(safecounter)
        
