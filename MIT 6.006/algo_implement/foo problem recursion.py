# -- problem

def foo(n, r):
    if n > 0:
        return ((n%r) + foo(int(n/r), r))
    else:
        return 0
