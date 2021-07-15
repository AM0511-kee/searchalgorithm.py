#binary search works only on sorted value
#mid value is created now if target is less than midvalue then then end =mid.p-1
#the list should be sorted
def binary_search(lst,target,low=None,high=None):
    if low is None:
        low=0
    if high is None:
        high=len(lst)-1
    if high<low:
        return (-1)

    mid_point=(low + high)//2

    if l[mid_point]==target:
        return(mid_point)
    elif l[mid_point] > target :
        return binary_search(lst,target,low,mid_point-1)
    elif l[mid_point] < target :
        return binary_search(lst,target,mid_point+1,high)

if __name__ == '__main__':
    l=[40,1,90,21,82,99,50,70]
    l=sorted(list(l))
    tar=70
    print(binary_search(l,tar))
