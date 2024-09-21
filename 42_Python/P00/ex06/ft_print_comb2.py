def print_comb2():
    combinations = []
    
    for i in range(100):
        for j in range(i + 1, 100):
            combination = f"{i:02d} {j:02d}"
            combinations.append(combination)
    
    print(', '.join(combinations))

print_comb2()