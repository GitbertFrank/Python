def ft_iterative_factorial(nb):
    if nb == 0:
        return 1
    if nb > 0:
        factorial = nb - 1
        while factorial > 1:
            nb *= factorial
            factorial-= 1
        return nb
    else:
        return 0

print(ft_iterative_factorial(-1))
print(ft_iterative_factorial(0)) 
print(ft_iterative_factorial(1)) 
print(ft_iterative_factorial(2)) 
print(ft_iterative_factorial(3)) 
print(ft_iterative_factorial(4))         
print(ft_iterative_factorial(5)) 
print(ft_iterative_factorial(6)) 
print(ft_iterative_factorial(7)) 