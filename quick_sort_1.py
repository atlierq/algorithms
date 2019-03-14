def quick_sort(mylist):
    length = len(mylist)
    if length <= 1:
        return mylist
    else:
        middle = mylist[0]
        left_half = [i for i in mylist[1:] if i < middle]
        right_half = [i for i in mylist[1:] if i >= middle]
        return quick_sort(left_half) + [middle] + quick_sort(right_half)


list = [4, 2, 5, 6, 7, 1, 3, 123125, -1, 2]
print(quick_sort(list))
