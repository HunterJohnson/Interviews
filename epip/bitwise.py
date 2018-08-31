# Bitwise operators in Python

# XOR

# fast way to clear the lowermost set bit

# set the lowermost 0

# get index of lowermost 0

# signedness & implications to shifting

# e.g...

6 & 4

1 | 2

8>>1

-16>>2

1<<10

~0

15^x

# there's no concept of an unsigned shift in Python since ints have inf. precision

# parity checks - remember parity of a binary word is 1 if # of 1's in the word is odd; otherwise 0

def parity(x):  # time complexity is O(n) where n is the word size, bruteforce algo
  result = 0
  while x:
    result ^= x & 1
    x >>= 1
  return result

# x &(x-1) equals x w/ its lowest set bit erased
# e.g. x = (00101100); x-1 = (00101011), so x&(x-1) = (00101000)
# likewise, x & ~(x-1) extracts the lowest set bit of x

# --> Let k be the n of bits set to 1 in a word. 
# time complexity of this upgraded algorithm is O(k)

def parity(x):
  result = 0
  while x:
    result ^= 1
    x &= x - 1
  return result
  
# the XOR of a group of bits is its parity
# eg. parity of (11010111) is parity of (1101) XOR w/ (0111) --> (1010) --> (10) XOR (10) --> (00) -- (0) XOR (0) --> 0

#  bitmask

# problem --> Implement code that takes as input a 64bit int & swaps the bits @ indices i & j
# if bits to be swapped don't differ, the swap doesn't change the value

def swap_bits(x,i,j):
  if (x >> i) & 1 != (x >> j) & 1:
    bit_mask = (1 << i) | (1 << j)
    x ^= bit_mask
  return x


#reverse bits

# write a program that takes a 64b unsigned int & returns the 64b unsigned int consisting of the bits of the
# input in reverse order (hint: use lookup table)

def reverse_bits(x):
  MASK_SIZE = 16
  BIT_MASK = 0xFFFF
  return "x"
  
# find closest integer w/ same weight
# "weight" = # of bits set to 1 in binary (eg weight of 92 [1011100] = 4)
# solution: swap the rightmost consecutive bits that differ

def closest_int_same_bitcount(x): # O(n) time complexity where n is int width
  NUM_UNSIGNED_BITS = 64
  for i in range(NUM_UNSIGNED_BITS - 1):
    if (x >> i) & 1 != (x >> (i + 1)) & 1:
      x ^= (1 << i) | (1 << (i + 1)) # swaps bit-i & bit-(i+1)
      return x
  raise ValueError('All bits are 0 or 1')











  
