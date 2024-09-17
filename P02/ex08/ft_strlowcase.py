def ft_strlowcase(str):
    newstr = ''
    for i in str:
        if 'A' <= i <= 'Z': 
            newstr += chr(ord(i) + 32)
        else:
            newstr += i
    return newstr

print(ft_strlowcase("211heWdWDAWdo"))