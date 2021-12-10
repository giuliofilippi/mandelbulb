import math

def factor(n):
    if n==1:
        return []
    else:
        for i in range(2,n+1):
            if n%i==0:
                return [i] + factor(n//i)


def f(n):
    factors = factor(n)
    sorted_factors = sorted(factors)
    string = ''

    for x in sorted_factors:
        string += str(x)

    return int(string)


def prime_test(p):
    k=0
    for i in range(2,int(math.ceil(math.sqrt(p)))+1):
        if (p%i)==0:
            k+=1

    if k==0:
        return True
    else:
        return False


def iterate(start):
    while prime_test(start)==False:
        print (start)
        start = f(start)




iterate(8)





