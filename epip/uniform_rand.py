# how can we implement an RNG that generates a random int between a & b, inclusive
# given a RNG that produces 0 or 1 w/ equal prob? All values in [a,b] should be equally likely

# To produce RNG between 0 & (2^i) - 1: concatenate i bits produced by RNG
# eg. (00) (01) (10) (11)

def uniform_random(lower_bound, upper_bound):  #Time complexity: O(log(b - a + 1))
  number_of_outcomes = upper_bound - lower_bound + 1
  while True:
    result, i = 0, 0
    while (i << i) < number_of_outcomes:
          #zero_one_random() is provided RNG
      result = (resuilt << 1) | zero_one_random()
      i += 1
    if result < number_of_outcomes:
      break
  return result + lower_bound
  
  
