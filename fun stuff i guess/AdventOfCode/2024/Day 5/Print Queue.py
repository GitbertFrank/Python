from random import shuffle 

data = open(r"2024\Day 5\data.txt").readlines()
testdata = open(r"2024\Day 5\example.txt").readlines()

firstnum = 0
secondnum = 0
newdata = []
orderingrules = []
pagestoproduce = []
correctlyordered = []
firstorder = True
firstrule = 0
secondrule = 0
firstruleindex = 0
secondruleindex = 0
unordered = []


def getorderandpages(list):
    for line in list:
        if "|" in line:orderingrules.append(line.strip().split("|"))
        else:pagestoproduce.append(line.strip().split(","))
    del pagestoproduce[0]

def checkrules(rules, line): 
    global firstruleindex, secondruleindex
    for lines in rules:
        firstrule = lines[0]
        secondrule = lines[1]
        if firstrule in line and secondrule in line:
            firstruleindex = line.index(firstrule)
            secondruleindex = line.index(secondrule)
            if firstruleindex > secondruleindex: return False
    return True

def getcorrectlyordered(rules, updates):
    for line in updates:
        if checkrules(rules, line) == False: unordered.append(line)
    
def orderunordered(rules, updates):
    global firstruleindex, secondruleindex
    for line in updates:
        while checkrules(rules, line) == False:
            firstitem = line.pop(firstruleindex)
            line.insert(secondruleindex, firstitem)
        correctlyordered.append(line)

def getsum(list):
    sum = 0
    for line in list:
        sum += int(line[len(line) // 2])
        print(sum)
    return sum

getorderandpages(data)
getcorrectlyordered(orderingrules, pagestoproduce)
orderunordered(orderingrules, unordered)

print("endsum: ", getsum(correctlyordered)) 

   
