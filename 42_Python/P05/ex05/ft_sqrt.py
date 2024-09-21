def ft_sqrt(nb):
    if nb < 1:
        return 0
    
    left, right = 1, nb
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == nb:
            return mid
        elif mid * mid < nb:
            left = mid + 1
        else:
            right = mid - 1
    
    return 0

print(ft_sqrt(4))    # Expected output: 2
print(ft_sqrt(10))   # Expected output: 0 (since 10 is not a perfect square)
print(ft_sqrt(0))    # Expected output: 0
print(ft_sqrt(-1))   # Expected output: 0
print(ft_sqrt(1))    # Expected output: 1
print(ft_sqrt(16))   # Expected output: 4
print(ft_sqrt(15))   # Expected output: 0 (since 15 is not a perfect square)
print(ft_sqrt(100))  # Expected output: 10
print(ft_sqrt(1000)) # Expected output: 0 (since 1000 is not a perfect square)
print(ft_sqrt(10000))# Expected output: 100
print(ft_sqrt(10**308))  # Expected output: 0 (since 10**308 is not a perfect square)
print(ft_sqrt(123456789012345678901234567890))  # Expected output: 0 (since it is not a perfect square)