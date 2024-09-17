def ft_putstr_non_printable(s):
    result = ''
    for char in s:
        if char.isprintable():
            result += char
        else:
            result += '\\' + format(ord(char), '02x')
    print(result)

ft_putstr_non_printable("Hello\tWorld\nGoodbye\r\x01\x02\x03\x04")