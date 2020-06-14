factorial_memo = {}

def factorial(k):
    
    if k < 2: 
        return 1
    
    if not k in factorial_memo:
        factorial_memo[k] = k * factorial(k-1)
        
    return factorial_memo[k]

print (factorial(4))

############## memoization using class ###################

def factorial2(k):
    if k <= 1: 
        return 1
    return k * factorial(k - 1)

class Memoize:
    def __init__(self, i):
        self.i = i
        self.mem = {}
    def __call__(self, *args):
        if not args in self.mem:
            self.mem[args] = self.i(*args)
        return self.mem[args]

print (Memoize(factorial2)(4))
