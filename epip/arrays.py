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

def dutch_flag_partition(pivot_index, A): # O(n^2) time
  pivot = A[pivot_index]
  # 1st pass --> group elements smaller than pivot
  for i in range(len(A)):
    for j in range(i+1, len(A)):
      if A[j] < pivot:
        A[i], A[j] = A[j], A[i]
        break
  # 2nd pass --> group elements larger than pivot
  for i in reversed(range(len(A))):
    for j in reversed(range(i)):
      if A[j] > pivot:
        A[i], A[j] = A[j], A[i]
        break

def dutch_flag_partition(pivot_index, A): # O(n) time; O(1) space
  pivot = A[pivot_index]
  #1st pass : group elements smaller than pivot
  smaller = 0
  for i in range(len(A)):
    if A[i] < pivot:
      A[i], A[smaller] = A[smaller], A[i]
      smaller += 1
  #2nd pass group elements larger than pivot
  larger = len(A) - 1
  for i in reversed(range(len(A))):
    if A[i] > pivot:
      A[i], A[larger] = A[larger], A[i]
      larger -= 1
  
  
  # write a program which takes as input an array of digits encoding a non-negative integer
  # & updates the array to represent the int D+1 eg [1,2,9] --> [1,3,0]
  
  def plus_one(A): # time complexity O(n), where n = len(A)
    A[-1] += 1
    for i in reversed(range(1, len(A))):
      if A[i] != 10:
        break
      A[i] = 0
      A[i-1] += 1
    if A[0] == 10:
      A[0] = 1
      A.append(0)
    return A
       
