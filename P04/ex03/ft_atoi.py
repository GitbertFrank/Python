def ft_atoi(str):
    strint = 0
    sign = 1
    i = 0
    for item in str:
        if item == ' ' or item == '\n' or item == '\t' or item == '\v' or item == '\f' or item == '\r':
            i += 1
        elif item == '+' or item == '-':
            if item == '-':
                sign = -sign
            i += 1
        elif '0' <= item <= '9':
            strint = strint * 10 + (ord(item) - ord('0'))
            i += 1
        else:
            break
        
    return strint *sign


print(ft_atoi("            --1234wda"))   