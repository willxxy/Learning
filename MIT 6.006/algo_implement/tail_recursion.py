# --- tail recursion

def TR(n, a):
    if n ==0 or n == 1:
        return a
    else:
        return TR(n-1, n*a)
