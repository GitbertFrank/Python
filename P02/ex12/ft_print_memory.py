def ft_print_memory(addr, size):
    if size == 0:
        return addr

    line_width = 16
    hex_width = 2
    for i in range(0, size, line_width):
        line_data = addr[i:i + line_width]
        address = i
        
        print(f"{address:08x}: ", end='')

        hex_part = ' '.join(f"{byte:02x}" for byte in line_data)
        hex_part = hex_part.ljust(line_width * (hex_width + 1) - 1)
        print(hex_part, end='')

        printable_part = ''.join(chr(byte) if 32 <= byte <= 126 else '.' for byte in line_data)
        print(f" {printable_part}")

    return addr

data = bytearray(
    b"Bonjour les amis.\nHere is some text.\nWith more lines and characters!"
)
ft_print_memory(data, len(data))