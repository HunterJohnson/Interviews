# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 15:13:04 2016

@author: HJohnson


The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""

stop = 1

def collatz(n):
    seq = []
    seq.append(n)
    ans = next_collatz(n)
    while (ans != stop):
        seq.append(ans)
        ans = next_collatz(ans)
    seq.append(stop)
    return(len(seq))
    
    
def next_collatz(n):
    if (n % 2) == 0:
        return n / 2
    else:
        return (3 * n) + 1
        
def solve():
    i = 1
    longest = 0
    longest_num = 0
    while(i < 1000000):
        chain = collatz(i)
        if chain > longest:
            longest = chain
            longest_num = i
        i += 1
    print(longest)
    print(longest_num)

    

        




