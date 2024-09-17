def ft_strlcpy(dest, src, size):
    if size > 0:
        dest = src[:size - 1] + '\0' if len(src) >= size else src[:size]
    else:
        dest = ''
    
    return len(src), dest
source = "Hello, World!"
dest_size = 6
length_of_source, destination = ft_strlcpy('', source, dest_size)
print(length_of_source, destination)