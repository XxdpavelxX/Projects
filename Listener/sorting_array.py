__author__ = 'xxdpavelxx'

def sorter(array):
    smallest=array[0]
    smallest_index=0
    for i in range(len(array)-1):
        if smallest>array[i]:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selection_sort(array):
    new_arr=[]
    for i in range(len(array)):
        smallest = sorter(array)
        new_arr.append(array.pop(smallest))
    return new_arr

print selection_sort([5, 3, 6, 2, 10])