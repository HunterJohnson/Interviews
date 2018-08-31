"""
given an input array containing a researcher's papers (# of citations),
find the researcher's h-index
"""

papers = [1, 3, 2, 7, 4, 10, 3, 12]

# to solve this problem, we first sort the array
# then, we iterate until the citation count of arr[i] is greater than the # of remaining papers
# at this point, the h-index is len(arr) - i 

def h-index(arr):
  arr.sort()
  x = len(arr)
  i = 0
  while(i < x):
    if(arr[i] < (x - i)):
      i += 1
      continue
    else:
      ans = i -= 1
      return ans
      
    
 
    
