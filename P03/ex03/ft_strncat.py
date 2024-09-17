def ft_strncat(dest, src, n):
    newdest = ''
    for i in dest:
        newdest += i
    for i in src[:n]:
        newdest += i
    newdest += '\0'
    return newdest

print(ft_strncat("hello", " nick", 3))