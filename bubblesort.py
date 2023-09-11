import random


def bubblesort(lst,length):
    for i in range(0,length):
        for j in range(0,length-i-1):  #每执行这个循环一次就会将未排序序列最大值放到该序列最后
            if lst[j+1]<lst[j]:
                temp = lst[j+1]
                lst[j+1] = lst[j]
                lst[j] = temp

#生成一个长度为9的随机数列表
randomlst = [0]*9
for i in range(0,9):
    randomlst[i] = random.randint(1,9)

print(randomlst)
bubblesort(randomlst,len(randomlst))
print(randomlst)
