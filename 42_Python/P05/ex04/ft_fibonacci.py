def ft_fibonacci(index):
    if index < 0:
        return -1
    if index == 0:
        return 0
    if index == 1:
        return 1
    return ft_fibonacci(index - 1) + ft_fibonacci(index -2)

print(ft_fibonacci(2))
print(ft_fibonacci(3))
print(ft_fibonacci(2))
print(ft_fibonacci(0))
print(ft_fibonacci(-1))
print(ft_fibonacci(3))
print(ft_fibonacci(3))