data = open(r"Day 8\data.txt").readlines()
testdata = open(r"Day 8\example.txt").readlines()

newdata = []
frequencies = []
sigmas = []
validfrequencies = []
antinodepos = []

newdata = [list(line.strip()) for line in testdata]

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
        if index_exists(x1 + 2 * (x2 - x1), y1 + 2 * (y2 - y1), newdata):
                if [y1 + 2 * (y2 - y1), x1 + 2 * (x2 - x1)] not in antinodepos:
                    antinodepos.append([y1 + 2 * (y2 - y1), x1 + 2 * (x2 - x1)])
        elif index_exists(x2 + 2 * (x1 - x2), y2 + 2 * (y1 - y2), newdata):
                if [y2 + 2 * (y1 - y2), x2 + 2 * (x1 - x2)] not in antinodepos:
                    antinodepos.append([y2 + 2 * (y1 - y2), x2 + 2 * (x1 - x2)])

print("Sigmas:", sigmas)
print("Valid Frequencies:", sorted(validfrequencies))
print("Antinode Positions:", sorted(antinodepos))
print("Number of Antinodes:", len(antinodepos))