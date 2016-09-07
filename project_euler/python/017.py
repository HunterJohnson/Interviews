# -*- coding: utf-8 -*-
"""
Created on Sun Sep 04 23:37:10 2016

@author: Hunter

Problem 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five,
 then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out
 in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""


number = {
    1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',
    8:'eight',9:'nine',10:'ten',11:'eleven',12:'twelve',13:'thirteen',
    14:'fourteen',15:'fifteen',16:'sixteen',17:'seventeen',
    18:'eighteen',19:'nineteen',20:'twenty',30:'thirty',40:'forty',
    50:'fifty',60:'sixty',70:'seventy',80:'eighty',90:'ninety',
    100:'hundred',1000:'thousand'}

tally = 0
for n in range(1,1001):
    x = str(n)    
    if len(str(n)) == 1:
        # The first 9 numbers are 1 digit -- in the dictionary
        k = len(number[n])
        print "n= %s k= %s" %(n,k)
        
    elif len(str(n)) == 2:
        x1 = x[0:1]
        x2 = x[1:2]
        if n < 20:
            # The numbers under 20 -- in the dictionary
            k = len(number[n])
            print "n= %s k= %s" %(n,k)
        else:
            if x2 == '0':
                # The numbers under 100 and greater than 19 -- in the 
                # dictionary ending in '0', (20, 30, 40 ....)
                k = len(number[n])
                print "n= %s k= %s" %(n,k)
            else:
                # The other numbers under 100 greater than 19 
                x1a = str(x1 + '0')
                k = len(number[int(x1a)]) + len(number[int(x2)])
                print "n1= %s k1= %s" %(n,k)
                
                
    elif len(str(n)) == 3:
        # add 3 for 'and' i.e. -- two-hundred and ten
        x1 = x[0:1]
        x2 = x[1:2]
        x3 = x[2:3]
        x1a = str(x2 + '0')
        x1aa = str(x2 + x3)
        if x1 == '1' and x2 == '0' and x3 == '0':
            # 100 -- in the dictionary
            k = len(number[1]) + len(number[100])
            print "n= %s k= %s" %(n,k)
        elif x2 == '0' and x3 == '0':
            # Consider 200, 300, 400, 500, 600, 700, 800, and 900
            k = len(number[int(x1)]) + len(number[100])
            print "n= %s k= %s" %(n,k)
        elif x2 == '0' and x3 != '0':
            # Consider 101, 102 ... 109, 201, 202, ... 209 etc.
            k = 3 + len(number[int(x1)]) + len(number[100]) \
                + len(number[int(x3)])
            print "n= %s k= %s" %(n,k)
        elif x2 != '0' and x3 == '0':
            # Consider 110, 120, ... 190, 210, 220, ... 290 etc.
            k = 3 + len(number[int(x1)]) + len(number[100]) \
                + len(number[int(x1a)])
            print "n= %s k= %s" %(n,k)
        elif x2 == '1' and x3 != '0':
            # Consider the teens 111, 112, ... 119, 211, 212, ... 219 etc.
            k = 3 + len(number[int(x1)]) + len(number[100]) \
                + len(number[int(x1aa)])
            print "n= %s k= %s" %(n,k)
        else:
            # Consider all the other numbers
            k = 3 + len(number[int(x1)]) + len(number[100]) \
                + len(number[int(x1a)]) + len(number[int(x3)])
            print "n= %s k= %s" %(n,k)
            
    else:
        # 1000 -- two parts (one and thousand) -- in the dictionary
        k = len(number[1]) + len(number[1000])
        print "n= %s k= %s" %(n,k)

    tally = tally + k
print "Tally = %s" % tally
        
        