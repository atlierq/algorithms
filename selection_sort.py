import CESHI
def selection_sort(mylist):
    length=len(mylist)
    for i in range(length-1):
        least=i
        for k in range(i+1,length):
            if mylist[k] < mylist[least]:
                least=k
            mylist[least],mylist[i]=mylist[i],mylist[least]
    return mylist

CESHI.test(selection_sort)