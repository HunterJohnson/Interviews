"""
given an input array containing a researcher's papers (# of citations),
find the researcher's h-index
"""

# to solve this problem, we first sort the array
# then, we iterate until the citation count of arr[i] is greater than the # of remaining papers
# at this point, the h-index is len(arr) - i 
# the complexity of this algorithm is O(n log n) w/ space complexity O(1)

papers = [1,4,1,3,2,1,3,5,6]


def h_index(arr):
  arr.sort()
  x = len(arr)
  i = 0
  while(i < x):
    if(arr[i] >= (x - i)):
      return x - i
    else:
        i += 1
  return 0

# this approach is better for an interview because it uses enumerate() fn
def h_index2(arr):
    arr.sort()
    n = len(arr)
    for i, c in enumerate(arr):
        if c >= n-i:
            return n-i
    return 0

print(h_index(papers2))

    
 
    
