def ft_sort_int_tab(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)- i -1):
            if(arr[j] > arr[j + 1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(ft_sort_int_tab([1, 4 ,56, 2, 23]))

