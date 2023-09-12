import random


## 选择排序的思想：在每次循环中找到最小的那个元素的索引，将它与该次循环
## 的最开始位置的元素交换即依次将最小、次小、次次小的元素往前排
## O(n^2)选择排序是稳定的排序

def selectionsort(lst,length):
    for i in range(0,length):
        min_index = i  #将i先视作未排序序列的最小值的索引
        for j in range(i,length-1):
            if lst[j+1]<lst[min_index]:
                min_index = j+1  #将最小值与为排序元素逐一比较找到最小值的索引
        #将最小值与索引为i的值交换
        temp = lst[i]
        lst[i] = lst[min_index]
        lst[min_index] = temp
#生成一个含九个元素的列表
randomlst = [0]*9
for k in range(0,9):
    randomlst[k] = random.randint(1,9)
print(randomlst)

selectionsort(randomlst,len(randomlst))
print(randomlst)