def ft_range(min, max):
    if min >= max: return None
    intarr = []
    for item in range(min,max):
        intarr.append(item)
    return intarr

print(ft_range(1, 5))