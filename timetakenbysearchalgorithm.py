import random
import time

def navie_search(lst,target):
    for i in range (len(lst)-1):
        if lst[i] == target:
            return (i)

    return('target not in list')

def binary_search(lst,target,low=None,high=None):
    if low is None:
        low=0
    if high is None:
        high=len(lst)-1
    if high<low:
        return (-1)

    mid_point=(low + high)//2

    if sorted_list[mid_point]==target:
        return(mid_point)
    elif sorted_list[mid_point] > target :
        return binary_search(lst,target,low,mid_point-1)
    elif sorted_list[mid_point] < target :
        return binary_search(lst,target,mid_point+1,high)


if __name__ == '__main__':
    #l=[40,1,90,21,82,99,50,70]
    #l=sorted(list(l))
    #tar=70
    #print(binary_search(l,tar))
    #print(navie_search(lst1,tar))
    length = 1000
    sorted_list=set()
    while len(sorted_list)<length:
        sorted_list.add(random.randint(-2*length,2*length))
    sorted_list=sorted(list(sorted_list))

    start=time.time()
    for target in sorted_list:
        navie_search(sorted_list,target)
    end=time.time()
    print('navie_search timing:',(end-start)/length,'second')


    start=time.time()
    for target in sorted_list:
        binary_search(sorted_list,target)
    end=time.time()
    print('binary_search timing:',(end-start)/length,'second')
