import math
import bubble_sort
default_size=5
def bucketSort(mylist,bucketSize=default_size):
    if(len(mylist)==0):
        print('you don\'t have any elements in array')
    minValue=mylist[0]
    maxValue=mylist[0]
    for i in range(len(mylist)):
        if mylist[i]<minValue:
            minValue=mylist[i]
        elif mylist[i]>maxValue:
            maxValue=mylist[i]

    bucketCount=math.floor((maxValue-minValue)/bucketSize)+1
    buckets=[]
    for i in range(bucketCount):
        buckets.append([])

    for i in range(len(mylist)):
        buckets[math.floor((mylist[i]-minValue)/bucketSize)].append(mylist[i])

    sortedArray=[]
    for i in range(len(buckets)):
        bubble_sort.bubble_sort(buckets[i])
        for j in range(len(buckets[i])):
            sortedArray.append(buckets[i][j])
    return sortedArray


if __name__ == '__main__':
    sortedArray=bucketSort([12, 23, 4, 5, 3, 2, 12, 81, 56, 95])
    print(sortedArray)