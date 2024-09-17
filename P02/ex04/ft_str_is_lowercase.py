def ft_str_is_lowercase(str):
    for i in str:
        if not('a' <= i <= 'z'):
            return 0
    return 1

print(ft_str_is_lowercase("elooo"))