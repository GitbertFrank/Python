data = open(r"Day 8\data.txt").readlines()
testdata = open(r"Day 8\example.txt").readlines()

newdata = []
frequencies = []
sigmas = []
validfrequencies = []
antinodepos = []

newdata = [list(line.strip()) for line in data]

def index_exists(y, x, newdata):
    return 0 <= y < len(newdata) and 0 <= x < len(newdata[0])

for y, column in enumerate(newdata):
    for x, char in enumerate(column):
        if char.isalnum():
            frequencies.append([char, y, x])
print(frequencies)
for freq in sorted(frequencies):
    sigmas.append(freq[0])

sigmas = [item for item in sigmas if sigmas.count(item) > 1]

for freq in frequencies:
    if freq[0] in sigmas:
        validfrequencies.append(freq)

for i, (freq, x1, y1) in enumerate(validfrequencies):
    for j, (freq2, x2, y2) in enumerate(validfrequencies):
        if i == j or freq != freq2:
            continue
        newx1,newx2,newy1,newy2 = x1,x2,y1,y2
        while True:
            if index_exists(newx1 + (x2 - x1), newy1 + (y2 - y1), newdata):
                    newx1 += (x2 - x1)
                    newy1 += (y2 - y1)
                    if [newy1, newx1] not in antinodepos:
                        antinodepos.append([newy1, newx1])
            else: break
        while True:
            if index_exists(newx2 + (x1 - x2), newy2 + (y1 - y2), newdata):
                    newx2 += (x1 - x2)
                    newy2 += (y1 - y2)
                    if [newy2, newx2] not in antinodepos:
                        antinodepos.append([newy2, newx2])
            else: break

print("Sigmas:", sigmas)
print("Valid Frequencies:", sorted(validfrequencies))
print("Antinode Positions:", sorted(antinodepos))
print("Number of Antinodes:", len(antinodepos))