#in navie search we iterate through the list
#and compare the element in list with target
#if element in list == target return true else keep loooking
lst1=[2,5,7,9,10,13,15,18]
tar=24
def navie_search(lst,target):
    for i in range (len(lst)-1):
        if lst[i] == target:
            return (i)

    return('target not in list')




print(navie_search(lst1,tar))
