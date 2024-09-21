def ft_strjoin(size, strs, sep):
    if size == 0: return ""
    result = strs[0]
    for i in range(1, size):
        result += sep + strs[i]
    return result

strs = ["Hello", "World", "!"]
print(ft_strjoin(3, strs, " "))
