def ft_strcmp(str1, str2):
    if str1 < str2:
        return -1
    elif str1 > str2:
        return 1
    return 0

print(ft_strcmp("HI", "HI"))