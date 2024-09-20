def ft_recursive_factorial(nb):
    if nb == 0:
        return 1
    if nb > 0:
        return (nb * ft_recursive_factorial(nb - 1))
    else:
        return 0
    
print(ft_recursive_factorial(-1))
print(ft_recursive_factorial(0)) 
print(ft_recursive_factorial(1)) 
print(ft_recursive_factorial(2)) 
print(ft_recursive_factorial(3)) 
print(ft_recursive_factorial(4))         
print(ft_recursive_factorial(5)) 
print(ft_recursive_factorial(6)) 
print(ft_recursive_factorial(7)) 