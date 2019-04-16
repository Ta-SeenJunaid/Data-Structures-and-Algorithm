# -*- coding: utf-8 -*-

def fib(n,lookup):
    
    if n==0 or n==1 :
        lookup[n] = n
        
    if lookup[n] is None:
        lookup[n] = fib(n-1,lookup) + fib(n-2,lookup)
        
    return lookup[n]
        
def main():
    n=int(input("Enter a number: "))
    #n=45
    lookup = [None]*(101)
    
    print("Fibonacci Number is " , fib(n, lookup))
    
if __name__=="__main__":
    main()

