__author__ = 'xxdpavelxx'

#x = 0
#for letter in string:
#    if letter not in list:
#        list.append(letter)
#    elif letter in list:
#        list.remove(letter)

#print list
def interview1():
    string = "Find the first non-repeating Fu character"
    list1 = []
    dict2 = {}
    dict = {}
    for letter in string:
        if letter not in dict:
            dict[letter]=1
        else:
            dict[letter]+=1
    #print dict
    for a in string:
        if dict[a]==1:
            print a
            break

def interview2(n):
    prime = [2,3,5,7]
    for x in range(2,n):
        if x>1 and x%2!=0 and x%3!=0 and x%5!=0 and x%7!=0:
            prime.append(x)
    print prime


def interview2a(n):
    y=0
    numbers=[]
    for x in range(2,n):
        numbers.append(x)
    for x in numbers:
        if x%numbers[y]== 0:
            numbers.remove(x)
    y=y+1
    for x in numbers:
        if x%numbers[y]==0:
            numbers.remove(x)
    y=y+1
    for x in numbers:
        if x%numbers[y]==0:
            numbers.remove(x)
    y=y+1
    for x in numbers:
        if x%numbers[y]==0:
            numbers.remove(x)
    print numbers


interview2a(100)







# O(n)