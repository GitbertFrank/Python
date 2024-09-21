def ft_ultimate_range(range1, min, max):
    if min >= max: range1 = None; return 0
    intarr = []
    for item in range(min, max):
        intarr.append(item)
        print(intarr)
    for item in intarr:
        range1 += 1
    range1 -= 1
    return range1

print(ft_ultimate_range(1, 3, 9))