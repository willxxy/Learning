# --- tail recursion

def TR(n, a):
    if n ==0 or n == 1:
        return a
    else:
        return TR(n-1, n*a)


# --- problem

def foo(n, r):
    if n>0:
        return ((n%r) + foo(round(n/r), r))
    else:
        return 0

if __name__ == "__main__":

    print(foo(345, 10))
