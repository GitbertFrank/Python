def ft_iterative_power(nb, power):
    if power < 0:
        return 0
    if power == 0:
        return 1
    nbfactor = nb
    while power > 1:
        nb *= nbfactor
        power -= 1
    return nb

print(ft_iterative_power(-1, 2))
print(ft_iterative_power(-1, 3))
print(ft_iterative_power(0, 2))
print(ft_iterative_power(0, 0))
print(ft_iterative_power(-1, 0))
print(ft_iterative_power(2, 3))
print(ft_iterative_power(3, 3))




