__author__ = 'xxdpavelxx'

mylist=[1,3,5,7,9]
def binary_search(list,item):
    low = 0
    high = len(list)-2
    while low <= high:
        mid = (high + low)/2
        if item == list[mid]:
            return item

        if item <= list[mid]:
            high = mid - 1

        else:
            low = mid + 1
    return None

print binary_search(mylist,5)
print binary_search(mylist,0)


