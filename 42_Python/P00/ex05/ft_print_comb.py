from itertools import combinations

def print_comb():
    digits = '0123456789'
    combs = combinations(digits, 3)
    
    results = []
    for comb in combs:
        result = ''.join(comb)
        results.append(result)
    
    print(', '.join(results))

print_comb()