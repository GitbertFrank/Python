def ft_find_next_prime(nb):
    if ft_is_prime(nb):
        return nb
    return ft_find_next_prime(nb + 1)

def ft_is_prime(nb):
    if nb <= 1:
        return 0
    if nb <= 3:
        return 1
    if nb % 2 == 0 or nb % 3 == 0:
        return 0
    for i in range(5, int(nb**0.5) + 1, 6):
        if nb % i == 0 or nb % (i + 2) == 0:
            return 0
    return 1

# Test cases
print(ft_find_next_prime(10))  # Expected output: 11
print(ft_find_next_prime(14))  # Expected output: 17
print(ft_find_next_prime(17))  # Expected output: 17
print(ft_find_next_prime(18))  # Expected output: 19
print(ft_find_next_prime(20))  # Expected output: 23