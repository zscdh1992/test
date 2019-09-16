# def mySort(list1):
# list1=[5,8,2,3,9]
# if list1[0]< list1[1]

newlist=[]
alist = [18, 39, 11, 34, 51, 100, 69, 71, 92, 88, 5, 75]
min = alist[0]  # 最小值是第一个元素
while len(alist)>0:
    for num in alist:
        if min>num:
            min=num
            print(alist.index(min))
    # alist.pop(1)
    newlist.append(min)
print(newlist)






