def ft_swap(a, b):
    tmp = a
    a = b
    b = tmp
    return a, b

print(ft_swap(10, 15))