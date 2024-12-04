import re

data = open(r"2024\Day 4\data.txt").readlines()
testdata = open(r"2024\Day 4\example.txt").readlines()

xmascounter = 0
nospacedata = []
for item in data:
    nospacedata.append(item.strip("\n"))

def Indexexists(index, list):
    return True if 0 <= index < len(list) else False


for i, line in enumerate(nospacedata):
    for j, item in enumerate(line):
        if item == "X":
            if Indexexists(j + 1, line): # check down
                if Indexexists(j + 2, line):
                    if Indexexists(j + 3, line):
                        if line[j + 1] == "M" and line[j + 2] == "A" and line[j + 3] == "S": xmascounter += 1
            if Indexexists(i + 1, nospacedata): # check right down
                if Indexexists(j + 1, nospacedata[i + 1]):
                    if Indexexists(i + 2, nospacedata):
                        if Indexexists(j + 2, nospacedata[i + 2]):
                            if Indexexists(i + 3, nospacedata):
                                if Indexexists(j + 3, nospacedata[i + 3]):
                                    if nospacedata[i + 1][j + 1] == "M" and nospacedata[i + 2][j + 2] == "A" and nospacedata[i + 3][j + 3] == "S": xmascounter += 1
            if Indexexists(i + 1, nospacedata): # check down
                if Indexexists(i + 2, nospacedata):
                    if Indexexists(i + 3, nospacedata):
                        if nospacedata[i + 1][j] == "M" and nospacedata[i + 2][j] == "A" and nospacedata[i + 3][j] == "S": xmascounter += 1
            if Indexexists(i + 1, nospacedata): # check left down
                if Indexexists(j - 1, nospacedata[i + 1]):
                    if Indexexists(i + 2, nospacedata):
                        if Indexexists(j - 2, nospacedata[i + 2]):
                            if Indexexists(i + 3, nospacedata):
                                if Indexexists(j - 3, nospacedata[i + 3]):
                                    if nospacedata[i + 1][j - 1] == "M" and nospacedata[i + 2][j - 2] == "A" and nospacedata[i + 3][j - 3] == "S": xmascounter += 1
            if Indexexists(j - 1, line): # check left
                if Indexexists(j - 2, line):
                    if Indexexists(j - 3, line):
                        if line[j - 1] == "M" and line[j - 2] == "A" and line[j - 3] == "S":xmascounter += 1
            if Indexexists(i - 1, nospacedata): # check left up
                if Indexexists(j - 1, nospacedata[i - 1]):
                    if Indexexists(i - 2, nospacedata):
                        if Indexexists(j - 2, nospacedata[i - 2]):
                            if Indexexists(i - 3, nospacedata):
                                if Indexexists(j - 3, nospacedata[i - 3]):
                                    if nospacedata[i - 1][j - 1] == "M" and nospacedata[i - 2][j - 2] == "A" and nospacedata[i - 3][j - 3] == "S": xmascounter += 1
            if Indexexists(i - 1, nospacedata): # check up
                if Indexexists(i - 2, nospacedata):
                    if Indexexists(i - 3, nospacedata):
                        if nospacedata[i - 1][j] == "M" and nospacedata[i - 2][j] == "A" and nospacedata[i - 3][j] == "S": xmascounter += 1
            if Indexexists(i - 1, nospacedata): # check right up
                if Indexexists(j + 1, nospacedata[i - 1]):
                    if Indexexists(i - 2, nospacedata):
                        if Indexexists(j + 2, nospacedata[i - 2]):
                            if Indexexists(i - 3, nospacedata):
                                if Indexexists(j + 3, nospacedata[i - 3]):
                                    if nospacedata[i - 1][j + 1] == "M" and nospacedata[i - 2][j + 2] == "A" and nospacedata[i - 3][j + 3] == "S": xmascounter += 1

print(xmascounter)
