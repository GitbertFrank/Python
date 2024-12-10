import itertools
import operator
data = open(r"Day 7\data.txt").readlines()
testdata = open(r"Day 7\example.txt").readlines()

nums = []
sums = []
validsums = []
invalidlines = []
invalidsums = []
newvalidsums = []

for line in data:
    parts = line.split()
    sums.append(int(parts[0].strip(":")))
    nums.append(parts[1:])

operators = {
    '+': operator.add, 
    '*': operator.mul,
    '||': operator.concat,
}

for i, eachsum in enumerate(sums):
    line = nums[i]
    Break = False
    linecombs = itertools.product(['+', '*'], repeat=len(line) - 1)
    for comb in linecombs:
        linesum = int(line[0])
        for j in range(len(comb)):
            linesum = operators[comb[j]](linesum, int(line[j + 1]))
            if linesum > eachsum: 
                Break = False
                break
            # print(linesum)  
        if int(linesum) == int(eachsum):
            print("valid")
            Break = True
            validsums.append(eachsum)
            break
    if not Break:
        invalidlines.append(nums[i])
        invalidsums.append(eachsum)


    
sumvalidsums = sum(validsums)
print(sumvalidsums)

for i, eachsum in enumerate(invalidsums):
    line = invalidlines[i]
    linecombs = itertools.product(['+', '*','||'] , repeat=len(line) - 1)
    for comb in linecombs:
        if '||' not in comb:continue
        linesum = line[0]
        for j in range(len(comb)):
            if comb[j] == '||':
                linesum = operators[comb[j]](str(linesum), str(line[j + 1]))
            else:
                linesum = operators[comb[j]](int(linesum), int(line[j + 1]))
            if int(linesum) > eachsum: 
                break
        if int(linesum) == int(eachsum):
            print("valid")
            newvalidsums.append(eachsum)
            break
        

print(newvalidsums)
print(sum(newvalidsums) + sumvalidsums)




