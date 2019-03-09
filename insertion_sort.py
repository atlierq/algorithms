def insertion_sort(mylist):
    for i in range(1,len(mylist)):
        while i >0 and mylist[i-1]>mylist[i]:
            mylist[i-1],mylist[i]=mylist[i],mylist[i-1]
            i-=1


    return mylist

list=[4,3,2,1]
a=insertion_sort(list)
print(a)