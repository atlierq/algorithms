def merge_sort(collection):
    length = len(collection)
    if length > 1:
        midpoint = length // 2
        left_half = merge_sort(collection[:midpoint])
        right_half = merge_sort(collection[midpoint:])
        i, j, k = 0, 0, 0
        left_length = len(left_half)
        right_length = len(right_half)
        while i < left_length and j < right_length:
            if left_half[i] < right_half[j]:
                collection[k] = left_half[i]
                # print(collection)
                i += 1
            else:
                collection[k] = right_half[j]
                j += 1
            k += 1

        while i < left_length:
            collection[k] = left_half[i]
            i += 1
            k += 1
        while j < right_length:
            collection[k] = right_half[j]
            j += 1
            k += 1
    return collection


list=[5,4,2,1,1,3,5,7]
print(merge_sort(list))