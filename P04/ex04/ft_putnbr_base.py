def ft_putnbr_base(nbr, base):
    if len(base) < 2 or '+' in base or '-' in base or len(set(base)) != len(base):
        return
    
    if nbr == 0:
        print('0')
        return
    
    sign = ''
    if nbr < 0:
        sign = '-'
        nbr = -nbr
    
    base_len = len(base)
    result = []
    while nbr > 0:
        remainder = nbr % base_len
        result.append(base[remainder])
        nbr //= base_len
    
    if sign:
        result.append(sign)
    
    print(''.join(reversed(result)))

ft_putnbr_base(1234, "0123456789")  
ft_putnbr_base(1234, "01")         
ft_putnbr_base(1234, "01234567")    
ft_putnbr_base(1234, "0123456789ABCDEF")  
ft_putnbr_base(-1234, "0123456789ABCDEF") 
ft_putnbr_base(1234, "poneyvif")    