def getspell(num):
    sum=0
    for x in num:
        sum+=int(x)
    return sum

def createpinyin(sum):
    list=[]
    for x in str(sum):
        if x=='1':
            list.append("yi")
        elif x=='2':
            list.append('er')
        elif x=='3':
            list.append('san')
        elif x=='4':
            list.append('si')
        elif x=='5':
            list.append('wu')
        elif x=='6':
            list.append('liu')
        elif x=='7':
            list.append('qi')
        elif x=='8':
            list.append('ba')
        elif x=='9':
            list.append('jiu')
        elif x=='0':
            list.append('ling')
    return list

def main():
    num=input()
    sum=getspell(num)
    list=createpinyin(sum)
    for x in list[:-1]:
        print(x,end=' ')
    print(list[-1])


main()