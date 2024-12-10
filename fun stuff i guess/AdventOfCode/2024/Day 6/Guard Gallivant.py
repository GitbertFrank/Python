data = open(r"Day 6\data.txt").readlines()
testdata = open(r"Day 6\example.txt").readlines()

looppositions = 0
newdata = []
for line in data:
    linedata = []
    for char in line:
        if char != "\n":
            string = char.strip()
            linedata.append(string)
    newdata.append(linedata)

def Indexexists(index, list):
    return True if 0 <= index < len(list) else False

moved = False
isvalid = True
positions = []
while isvalid:
    if isvalid == False: break
    moved = False
    for i, line in enumerate(newdata):
        if isvalid == False or moved: break
        moved = False
        for j, item in enumerate(line):
            if isvalid == False or moved: break
            moved = False
            if item not in "^><v": continue
            currpos = [i, j]
            if currpos not in positions:
                positions.append(currpos)
            if item == "^":
                if Indexexists(i - 1, newdata):
                    if Indexexists(j, newdata[i - 1]):
                        if newdata[i - 1][j] == "#":
                            newdata[i][j] = ">"
                            moved = True
                            break
                        else:
                            newdata[i - 1][j] = "^"
                            newdata[i][j] = "."
                            moved = True
                            break
                    else: 
                        isvalid = False 
                        newdata[i][j] = "."
                        break
                else: 
                    isvalid = False 
                    newdata[i][j] = "."
                    break
            elif item == ">":
                if Indexexists(j + 1, line): 
                    if line[j + 1] == "#":
                        newdata[i][j] = "v"
                        moved = True
                        break
                    else:
                        newdata[i][j + 1] = ">"
                        newdata[i][j] = "."
                        moved = True
                        break
                else: 
                    isvalid = False 
                    newdata[i][j] = "."
                    break
            elif item == "v":
                if Indexexists(i + 1, newdata):
                    if Indexexists(j, newdata[i + 1]):
                        if newdata[i + 1][j] == "#":
                            newdata[i][j] = "<"
                            moved = True
                            break
                        else:
                            newdata[i + 1][j] = "v"
                            newdata[i][j] = "."
                            moved = True
                            break
                    else:
                        isvalid = False 
                        newdata[i][j] = "."
                        break
                else: 
                    isvalid = False 
                    newdata[i][j] = "."
                    break
            elif item == "<":
                if Indexexists(j - 1, line):
                    if line[j - 1] == "#":
                        newdata[i][j] = "^"
                        moved = True
                        break
                    else:
                        newdata[i][j - 1] = "<"
                        newdata[i][j] = "."
                        moved = True
                        break
                else: 
                    isvalid = False 
                    newdata[i][j] = "."
                    break 

newdata[positions[0][0]][positions[0][1]] = "^"
for p, position in enumerate(positions):
    y = position[0]
    x = position[1]
    if newdata[y][x] == ".":
        newdata[y][x] = "O"
    else: continue
    visitedpositions = []
    isvalid = True
    while isvalid:
        if isvalid == False: break
        moved = False
        for i, line in enumerate(newdata):
            if isvalid == False or moved: break
            for j, item in enumerate(line):
                if item not in "^>v<":
                    continue
                if item == "^":
                    if Indexexists(i - 1, newdata):
                        if Indexexists(j, newdata[i - 1]):
                            if newdata[i - 1][j] == "#" or newdata[i - 1][j] == "O":
                                position = [i, j, item]
                                if position in visitedpositions:
                                    isvalid = False
                                    looppositions += 1
                                    newdata[i][j] = "."
                                    break
                                visitedpositions.append(position)
                                newdata[i][j] = ">"
                                moved = True
                                break
                            else:
                                newdata[i - 1][j] = "^"
                                newdata[i][j] = "."
                                moved = True
                                break
                        else: 
                            isvalid = False 
                            newdata[i][j] = "."
                            break
                    else: 
                        isvalid = False 
                        newdata[i][j] = "."
                        break
                elif item == ">":
                    if Indexexists(j + 1, line): 
                        if line[j + 1] == "#" or line[j + 1] == "O":
                            position = [i, j, item]
                            if position in visitedpositions:
                                isvalid = False
                                looppositions += 1
                                newdata[i][j] = "."
                                break
                            visitedpositions.append(position)
                            newdata[i][j] = "v"
                            moved = True
                            break
                        else:
                            newdata[i][j + 1] = ">"
                            newdata[i][j] = "."
                            moved = True
                            break
                    else: 
                        isvalid = False 
                        newdata[i][j] = "."
                        break
                elif item == "v":
                    if Indexexists(i + 1, newdata):
                        if Indexexists(j, newdata[i + 1]):
                            if newdata[i + 1][j] == "#" or newdata[i + 1][j] == "O":
                                position = [i, j, item]
                                if position in visitedpositions:
                                    isvalid = False
                                    looppositions += 1
                                    newdata[i][j] = "."
                                    break
                                visitedpositions.append(position)
                                newdata[i][j] = "<"
                                moved = True
                                break
                            else:
                                newdata[i + 1][j] = "v"
                                newdata[i][j] = "."
                                moved = True
                                break
                        else:
                            isvalid = False 
                            newdata[i][j] = "."
                            break
                    else: 
                        isvalid = False 
                        newdata[i][j] = "."
                        break
                elif item == "<":
                    if Indexexists(j - 1, line):
                        if line[j - 1] == "#" or line[j - 1] == "O":
                            position = [i, j, item]
                            if position in visitedpositions:
                                isvalid = False
                                looppositions += 1
                                newdata[i][j] = "."
                                break
                            visitedpositions.append(position)
                            newdata[i][j] = "^"
                            moved = True
                            break
                        else:
                            newdata[i][j - 1] = "<"
                            newdata[i][j] = "."
                            moved = True
                            break
                    else: 
                        isvalid = False 
                        newdata[i][j] = "."
                        break  
    newdata[y][x] = "."
    newdata[positions[0][0]][positions[0][1]] = "^"
    print(looppositions)
