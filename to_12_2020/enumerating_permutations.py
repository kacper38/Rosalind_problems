"""
Problem
A permutation of length n is an ordering of the positive integers {1,2,…,n}. For example, π=(5,3,2,1,4) is a permutation of length 5.

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).

Sample Dataset
3
Sample Output
6
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1
"""

"""
Created on Sun Sep  6 13:04:43 2020

@author: kacper
"""
import math
from itertools import permutations


def prod_perm(x):
    with open("odp.txt", 'w') as out_d:
        out_d.write(str(math.factorial(x)))
        ans1 = permutations(range(1,x+1))
        out_d.write('\n')
        for item in ans1:
            out_d.write(' '.join(map(str, item)))
            out_d.write('\n')
