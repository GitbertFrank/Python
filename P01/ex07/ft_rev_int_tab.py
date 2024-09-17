def ft_rev_int_tab(arr):
    first = 0
    last = len(arr) - 1
    while first < last:
        arr[first], arr[last] = arr[last], arr[first]
        first+=1
        last-=1
    return arr

print(ft_rev_int_tab([1, 2, 3]))
    