def ft_atoi_base(str, base):
    if len(base) < 2 or '+' in base or '-' in base or len(set(base)) != len(base) or any(char.isspace() for char in base):
        return None
    base_len = len(base)
    sign = 1
    index = 0
    if str[0] == '-':
        sign = -1
        index = 1
    elif str[0] == '+':
        index = 1

    result = 0
    while index < len(str):
        char = str[index]
        if char in base:
            result = result * base_len + base.index(char)
        else:
            return None
        index += 1

    return result * sign

def test_ft_atoi_base():
    print(ft_atoi_base("1010", "01"))  # Expected output: 10
    print(ft_atoi_base("123", "0123456789"))  # Expected output: 123
    print(ft_atoi_base("1A", "0123456789ABCDEF"))  # Expected output: 26
    print(ft_atoi_base("123", "01234567899"))  # Expected output: None
    print(ft_atoi_base("123", "01234 56789"))  # Expected output: None
    print(ft_atoi_base("-123", "0123456789"))  # Expected output: -123
    print(ft_atoi_base("+123", "0123456789"))  # Expected output: 123
    print(ft_atoi_base("123", "01234"))  # Expected output: None
    print(ft_atoi_base("17", "01234567"))  # Expected output: 15
    print(ft_atoi_base("!@#", "!@#$%^&*()"))  # Expected output: 2

# Run the test cases
test_ft_atoi_base()