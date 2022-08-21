#---recursion
import math
import time

def f(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * f(n-1)

def dosomething(n):
    if n<=2:
        return 1
    else:
        return (dosomething(math.floor(math.sqrt(n)))) + n

if __name__  == '__main__':
    start_time = time.time()

    print(dosomething(70000))
    print()
    print("--- %s seconds ---" % (time.time() - start_time))


    
