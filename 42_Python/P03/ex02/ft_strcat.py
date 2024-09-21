def ft_strcat(dest, src):
    newdest = ''
    for i in dest:
        newdest += i
    for i in src:
        newdest += i
    newdest += '\0'
    return newdest

print(ft_strcat("hello", " nick"))