def ft_strncmp(str1, str2, n):
    for i in range(n):
        if i >= len(str1) and i >= len(str2):
            return 0
        if i >= len(str1):
            return -ord(str2[i])
        if i >= len(str2):
            return ord(str1[i])
        if str1[i] != str2[i]:
            return ord(str1[i]) - ord(str2[i])
    return 0

print(ft_strncmp("HI", "HIe", 3))