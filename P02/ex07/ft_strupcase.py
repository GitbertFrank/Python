def ft_strupcase(str):
    newstr = ''
    for i in str:
        if 'a' <= i <= 'z': 
            newstr += chr(ord(i) - 32)
        else:
            newstr += i
    return newstr

print(ft_strupcase("hello"))
