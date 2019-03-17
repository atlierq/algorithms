from CESHI import test


def radix_sort(mylist):
    RADIX = 10
    placement = 1
    # 获取最大值
    max_digit = max(mylist)

    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]
        for i in mylist:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                mylist[a] = i
                a += 1
        # 每次乘10到达更高位
        placement *= RADIX
    return mylist


def divde_sort(list):
    list1 = []
    list2 = []
    for i in list:
        if i >= 0:
            list1.append(i)
        else:
            list2.append(-i)

    list1_1 = radix_sort(list1)
    print(list1_1)
    list2_2 = radix_sort(list2)
    print(list2_2)
    return [-i for i in reversed(list2_2)] + list2_2


test(divde_sort)
