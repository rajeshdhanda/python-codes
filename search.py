

# Search x in an unsorted array A.
# Return index i, A[i]=x
# If x does not belong to A, then return -1
# Linear search
def search(A, x):
    i = 0   # index

    while (A[i] != x):
        i += 1
        if (i == len(A)):   #i beyond A's size
            break

    if (i < len(A)):
        return i
    else:
        return -1


# Search x in an sorted array A.
# Return index i, A[i]=x
# If x does not belong to A, then return -1
# Binary search
def binsearch(A, x):
    n = len(A)
    lower = 0
    upper = n-1
    mid = (lower+upper)/2
    
    # if x is outside array, return -1
    if ((x < A[0]) | (x>A[-1])):
        return -1
    
    # Is x == A[mid]? If not search in the left or right
    while (A[mid] != x):
        if (lower == upper):
            break
        if (x<A[mid]):
            upper = mid-1
        else:
            lower = mid+1
        mid = (lower+upper)/2
    
    if (A[mid] == x):
        return mid
    else:
        return -1


# Search x in an sorted array A between A[lower:upper].
# Return index i, A[i]=x
# If x does not belong to A, then return -1
# Recursive binary search
def binsearch_recursive(A,lower,upper,x):
    mid = (lower+upper)/2
    if ((x < A[lower]) | (x>A[upper])):
        return -1
    elif ((lower==upper) & (A[mid] != x)):
        return -1
    else:
        if (A[mid] == x):
            ans = mid
        elif (x < A[mid]):
            ans = binsearch_recursive(A,lower,mid-1,x)
        else:
            ans = binsearch_recursive(A,mid+1,upper,x)
        return ans



