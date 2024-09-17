from itertools import combinations

def ft_print_combn(n):
    if n <= 0 or n >= 10:
        raise ValueError("n must be between 1 and 9")

    digits = '0123456789'
    
    combs = combinations(digits, n)
    
    results = []
    for comb in combs:
        result = ''.join(comb)
        results.append(result)
    
    print(', '.join(results))

ft_print_combn(9)
