#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'buildString' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER a
#  2. INTEGER b
#  3. STRING s
#

def buildString(a, b, s):
    s= s.strip()
    result=""
    i=0
    cost=0
    while s != result:
        out=""
        for j in range(len(result)):
            sub =s[i:i+j+1]
            sub = sub.strip() 
            if result.count(sub)>0 and len(out) < len(sub):
                out = sub
        l= len(out)    
        if l>0 and a*l > b:
            cost += b
            i += l
            result += out
        else:
            cost += a
            result += s[i]
            i +=1
    #print(cost)
    print(cost)


if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        a = int(first_multiple_input[1])

        b = int(first_multiple_input[2])

        s = input()

        result = buildString(a, b, s)



