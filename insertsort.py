import random

## 插入排序的思想：从数组的第二项也就是arr[1]开始，将该元素前面所有的
## 大于该元素的部分整体想该元素的位置移动，最后将该元素插入前面最后移动
## 的那个元素的位置，插入排序是稳定的排序算法（相同值的元素的相对位置不会变）

def insertsort(lst,length):

    for i in range(1,length):
        temp = lst[i]    #lst[i]为待插入值
        j = 0 #这里是初始化j方便后面在j的循环外使用j的值
        for j in range(i,0,-1):
            if lst[j-1] > temp: #将前面的所有比待插入值大的向右移动
                lst[j] = lst[j-1]
                print(j)
            elif lst[j-1] <= temp: #因为是i是从0开始，所以只要待插入值比
                print(j)
                break              #前面的那个元素大就肯定比前面所有的都大
                                   #就不用再继续往前循环判断下去了
            lst[j-1] = temp        

randomlst = [0]*9
for k in range(0,9):
    randomlst[k] = random.randint(1,9)
print(randomlst)

insertsort(randomlst,len(randomlst))
print(randomlst)


            

