def ft_strlcat(dest, src, size):
    dest_len = len(dest)
    src_len = len(src)
    
    if size <= dest_len:
        return size + src_len
    
    space_left = size - dest_len - 1
    to_copy = min(space_left, src_len)
    
    new_dest = dest + src[:to_copy]
    
    return new_dest

print(ft_strlcat("ni", "nnoononono", 6))