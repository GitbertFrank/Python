def ft_str_is_printable(str):
    for i in str:
        if not(chr(32) <=i <= chr(126)):
            return 0
    return 1

print(ft_str_is_printable("111111111111111111111"))