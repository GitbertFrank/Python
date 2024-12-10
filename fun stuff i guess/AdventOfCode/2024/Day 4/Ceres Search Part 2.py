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
        if item == "A":
            if Indexexists(i - 1, nospacedata): # check if top line exists
                if Indexexists(j + 1, nospacedata[i - 1]): # check if top right exists
                    if Indexexists(i + 1, nospacedata): # check if bottom line exists
                        if Indexexists(j + 1, nospacedata[i + 1]): # check if bottom right exists
                            if Indexexists(j - 1, nospacedata[i + 1]): # check if bottom left exists
                                if Indexexists(j - 1, nospacedata[i - 1]): # check if top left exists
                                    if nospacedata[i - 1][j - 1] == "M":# check top left for M
                                        if nospacedata[i - 1][j + 1] == "S": # check top right for S
                                            if nospacedata[i + 1][j + 1] == "S":# check bottom right for S
                                                if nospacedata[i + 1][j - 1] == "M": # check bottom left for M
                                                    xmascounter += 1
                                        if nospacedata[i - 1][j + 1] == "M":# check top right for M
                                            if nospacedata[i + 1][j + 1] == "S":# check bottom right for S
                                                if nospacedata[i + 1][j - 1] == "S":# check bottom left for S
                                                    xmascounter += 1
                                    if nospacedata[i - 1][j - 1] == "S":# check top left for S
                                        if nospacedata[i - 1][j + 1] == "M": # check top right for M
                                            if nospacedata[i + 1][j + 1] == "M":# check bottom right for M
                                                if nospacedata[i + 1][j - 1] == "S": # check bottom left for S
                                                    xmascounter += 1
                                        if nospacedata[i - 1][j + 1] == "S":# check top right for S
                                            if nospacedata[i + 1][j + 1] == "M":# check bottom right for M
                                                if nospacedata[i + 1][j - 1] == "M":# check bottom left for M
                                                    xmascounter += 1
print(xmascounter)
