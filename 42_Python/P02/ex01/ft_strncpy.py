def ft_strncpy(dest, src, n):
    if len(dest) < n:
        dest = [''] * n
    
    for i in range(n):
        if i < len(src):
            dest[i] = src[i]
        else:
            dest[i] = ''
    return ''.join(dest)
print(ft_strncpy("Hi", "nigger", 0))