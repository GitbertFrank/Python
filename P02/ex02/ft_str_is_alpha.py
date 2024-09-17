def ft_str_is_alpha(str):
    for i in str:
        if not('a' <= i <= 'z' or 'A' <= i <= 'Z'):
            return False
    return True

print(ft_str_is_alpha("Hel2ooo"))