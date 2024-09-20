def ft_recursive_power(nb, power):
    if power < 0:
        return 0
    if power == 0:
        return 1
    return (nb * ft_recursive_power(nb, power - 1))

print(ft_recursive_power(-1, 2))
print(ft_recursive_power(-1, 3))
print(ft_recursive_power(0, 2))
print(ft_recursive_power(0, 0))
print(ft_recursive_power(-1, 0))
print(ft_recursive_power(2, 3))
print(ft_recursive_power(3, 3))