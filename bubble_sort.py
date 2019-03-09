def bubble_sort(collection):
    length = len(collection)
    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            # print(j)

            # print(str(collection[j])+"--"+str(collection[j+1]))
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
            # print(swapped)
        # print(swapped)
        if not swapped:
            # print('a')
            break
    return collection


def main(list):
    sorted_list = bubble_sort(list)
    print(sorted_list)


list = [1, 234,2,3,2]
if __name__ == '__main__':
    main(list)
