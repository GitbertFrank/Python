def ft_ultimate_div_mod(a, b):
    tmp = a
    a /= b
    b = tmp % b
    return a, b

print(ft_ultimate_div_mod(12, 5))