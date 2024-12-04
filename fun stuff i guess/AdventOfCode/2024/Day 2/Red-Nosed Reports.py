data = open(r"2024\Day 2\data.txt").readlines()
testdata = open(r"2024\Day 2\example.txt").readlines()
newdata = []
validlist = []
safecounter = 0
differencecounter = 0
for item in data:
    newdata.append(list(map(int, item.strip("\n").split())))

for item in newdata:
    if item == list((sorted((item)))) or item == list((sorted((item), reverse=True))):
        safecounter += 1
        validlist.append(item)
    else:
        for i, Item in enumerate(item):
            if Item != list((sorted((item))))[i] or Item != list((sorted((item), reverse=True)))[i]: differencecounter += 1
            if differencecounter < 2:
                item.remove(Item)
                if item == list((sorted((item)))) or item == list((sorted((item), reverse=True))):
                    safecounter += 1
                    validlist.append(item)
            else: break
        
    differencecounter = 0


differencecounter = 0
        
for item in validlist:
    for i, Item in enumerate(item):
        if i < len((item))- 1:
            difference = abs(Item - item[i + 1])
        if difference > 3:
            differencecounter += 1
            if differencecounter > 1: 
                safecounter -= 1
                break
    differencecounter = 0
print(safecounter)
