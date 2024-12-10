import itertools
import operator
data = open(r"Day 7\data.txt").readlines()
testdata = open(r"Day 7\example.txt").readlines()

linesum = 0
nums = []
sums = []
validsums = []
for line in data:
    parts = line.split()
    sums.append(int(parts[0].strip(":")))
    nums.append(parts[1:])

operators = {
    '+': operator.add, 
    '*': operator.mul,
}

for i, eachsum in enumerate(sums):
    for comb in itertools.product(['+', '*'], repeat=len(nums[i]) - 1):
        linesum = int(nums[i][0])
        for j in range(len(comb)):
            linesum = operators[comb[j]](linesum, int(nums[i][j + 1]))
            if linesum > eachsum: break
            # print(linesum)  
        if int(linesum) == int(eachsum):
            print("valid")
            validsums.append(eachsum)
            break        

print(sum(validsums))
print()
print("should be this for puzzle input:")
print("3351424677624")
3351433339626
