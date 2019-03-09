def cocktail_shaker_sort(mylist):
    for i in range(len(mylist)-1,0,-1):
        # print(i)
        swapped=False
        for i in range(i,0,-1):
            if mylist[i]<mylist[i-1]:
                mylist[i],mylist[i-1]=mylist[i-1],mylist[i]
                swapped=True
        for j in range(i):
            if mylist[j]>mylist[j+1]:
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
                swapped=True
        if not swapped:
            return mylist
        #

mylist=[1,2,3,4,12,421,421,31,-234,543]
a=cocktail_shaker_sort(mylist)
print(a)