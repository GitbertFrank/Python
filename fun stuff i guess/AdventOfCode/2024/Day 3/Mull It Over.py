import re
data = open(r"2024\Day 3\data.txt").read()
testdata = open(r"2024\Day 3\example.txt").read()


list = []
result = 0
firstnum = 0
secondnum = 0
firstlist = []
secondlist = []
ison = True
boolsecondnum = False
j = 0

list= re.findall("do\(\)|mul\(\d+,\d+\)|don't\(\)", data)
print(list)
for Item in list:
    if Item == "don't()" : 
        ison = False
    if ison and Item[0] == "m":
        for item in Item:
            if item.isdigit() and boolsecondnum == False:
                firstlist.append(item)
            if item == ",": 
                boolsecondnum = True
            if item.isdigit() and boolsecondnum == True:
                secondlist.append(item)
            print(firstlist)
            if item == ")":
                firstnum = int(''.join(map(str, firstlist)))
                secondnum = int(''.join(map(str, secondlist)))
                result += firstnum * secondnum
                firstlist.clear()
                secondlist.clear()
                boolsecondnum = False
    if Item == "do()": 
        ison = True
    print(result)


# lastattemp : 18039252
               