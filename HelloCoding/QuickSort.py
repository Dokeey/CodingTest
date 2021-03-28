def quick_sort(x: list, reverse=False):
    if x:
        pivot = x.pop()
        lt_list = []
        big_list = []
        for num in x:
            if pivot < num:
                big_list.append(num)
            else:
                lt_list.append(num)
        if reverse:
            return quick_sort(big_list, reverse=True) + [pivot] + quick_sort(lt_list, reverse=True)
        return quick_sort(lt_list) + [pivot] + quick_sort(big_list)
    return []


print(quick_sort([2, 5, 3, 8, 2]))
print(quick_sort([2, 5, 3, 8, 2], reverse=True))
print(quick_sort([2, 5, 3, 8, 2, 2, 5, 3, 8, 2, 2, 5, 3, 8, 2]))
print(quick_sort([5, 3]))
print(quick_sort([3]))
