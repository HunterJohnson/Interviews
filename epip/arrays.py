# array: a contiguous block of memory
# retrieving & updating A[i] takes O(1) time

# deleting an element at A[i] from arr of length n is O(n-i), same is true for inserting a new element

def even_odd(A):  # reorder array into evens & odds (evens first)... time complexity O(n); space O(1)
  next_even, next_odd = 0, len(A) - 1
  while next_even < next_odd:
    if A[next_even] % 2 == 0:
      next_even += 1
    else:
      A[next_even], A[next_odd] = A[next_odd], A[next_even]
      next_odd -= 1

# python - arrays are also called lists; tuples are similar but immutable

# basic pythonic operations are len(A) ; A.append(40) ; A.remove(2) ; A.insert(3,28)
"""
other methods; min/max(A) ; bisect.bisect(A,n) ; bisect.bisect_left/right; A.reverse(); A.sort()
               reversed(A) --> returns iterator ; sorted(A) --> returns copy ; del A[i] ; del A[i:j]
          
            slicing : A[::-1] reverses A ; A[k:] + A[:k] rotates A by k to the left
                      B = A[:] shallow copies A into B
"""
# check if value present: a in A  .....  O(n) complexity 
# copy.copy vs copy.deepcopy
# 
