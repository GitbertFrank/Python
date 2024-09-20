def ft_is_prime(nb):
    if nb <= 1:
        return 0
    if nb <= 3:
        return 1
    if nb % 2 == 0 or nb % 3 == 0:
        return 0
    i = 5
    for i in range(5, int(nb**0.5) + 1, 6):
        if nb % i == 0 or nb % (i + 2) == 0:
            return 0
    return 1

# Test cases
print(ft_is_prime(2))    # Expected output: True
print(ft_is_prime(3))    # Expected output: True
print(ft_is_prime(4))    # Expected output: False
print(ft_is_prime(5))    # Expected output: True
print(ft_is_prime(10))   # Expected output: False
print(ft_is_prime(11))   # Expected output: True
print(ft_is_prime(1))    # Expected output: False
print(ft_is_prime(0))    # Expected output: False
print(ft_is_prime(-1))   # Expected output: False
print(ft_is_prime(17))   # Expected output: True
print(ft_is_prime(18))   # Expected output: False
print(ft_is_prime(19))   # Expected output: True