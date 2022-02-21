def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    n = len(A)
    current = 1 #length of longest increasing subarray ending at A[i-1]
    length = 1  #length of longest increasign subarray in A[:1]
    count = 1   # number of longest increasing subarray in A[:i]

    for i in range(1,n):

        if A[i-1] < A[i]:

            current += 1

        else:

            current = 1

        if current == length:

            count += 1

        elif current > length:

            length = current

            count = 1
            


    
    return count
