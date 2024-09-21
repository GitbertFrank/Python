def ft_str_is_numeric(str):
    for i in str:
        if not('0' <= i <= '9'):
            return False
    return True

print(ft_str_is_numeric("2"))