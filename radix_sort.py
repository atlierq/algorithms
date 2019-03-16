def radix_sort(mylist):
    RADIX=10
    placement=1
    #获取最大值
    max_digit=max(mylist)

    while placement<max_digit:
        buckets=[list() for _ in range(RADIX)]
        for i in mylist:
            tmp=int((i/placement)%RADIX)
            buckets[tmp].append(i)
        a=0
        for b in range(RADIX):
            buck=buckets[b]
            for i in buck:
                mylist[a]=i
                a+=1
        #每次乘10到达更高位
        placement *=RADIX


a=[13,3,4,5,21,1,3]
radix_sort(a)
print(a)
