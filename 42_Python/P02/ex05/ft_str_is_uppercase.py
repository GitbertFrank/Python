def ft_str_is_uppercase(str):
    for i in str:
        if not('A' <= i <= 'Z'):
            return 0
    return 1

print(ft_str_is_uppercase("HELOOOOOOOO"))