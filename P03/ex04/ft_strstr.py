def ft_strstr(str, to_find):
    if to_find == "":
        return str
    
    str_len = len(str)
    to_find_len = len(to_find)
    
    for i in range(str_len - to_find_len + 1):
        if str[i:i + to_find_len] == to_find:
            return str[i:]
    
    return None

