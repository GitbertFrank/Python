data = open(r"C:\Users\Robert Frank\Desktop\Coding\Python\fun stuff i guess\AdventOfCode\2024\Day 1\data.txt").readlines()

similarityscore = 0
counter = 0
spacelessdata = []
string1 = ''
list1 = []
list2 = []
distance = 0

for item in data:
    spacelessdata.append(item.rstrip("\n"))

for item in spacelessdata:
    string1 += item + " "

listaftersplit = string1.split()

for i, item in enumerate(listaftersplit):
    list1.append(item) if i % 2 == 0 else list2.append(item)

list1.sort()
list2.sort()
for i, item in enumerate(list1):
    distance += int(item) - int(list2[i]) if int(item) > int(list2[i]) else int(list2[i]) - int(item)

print(distance)

for item in list1:
    similarityscore += list2.count(item) * int(item)
print(similarityscore)

