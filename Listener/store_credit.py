__author__ = 'xxdpavelxx'

def credit():
    a = input("Please type how much credit here: ")
    print a

def items():
    b = input("Input how many items you have in the store: ")
    print b


def store_cred(N):

    for x in range(N):
        print "Case #%s" %(x+1)
        credit()
store_cred(5)
