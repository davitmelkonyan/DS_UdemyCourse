#iterative
def fib_iter(n):
    a, b = 0, 1
    for i in range(n):
        a,b = b, a+b
    return a

print (fib_iter(10))

#recursive
def fib_rec(n):
    if n==0 or n==1:
        return n
    else:
        return fib_rec(n-1)+fib_rec(n-2)

print (fib_iter(10))

#memoization
n = 10 #need to be = to whatever running for
cache = [None]*(n+1)
def fib_dyn(n):
    if n==0 or n==1:
        return n
    if cache[n]!=None:
        return cache[n]
    cache[n] = fib_dyn(n-1) + fib_dyn(n-2)
    return cache[n]
