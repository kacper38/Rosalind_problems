
import math


def partial_perm(n, k):
    return math.factorial(n)/math.factorial(n-k) % 1000000

print(int(partial_perm(21,7)))

with open('./rosalind_pper.txt', 'rt') as fin:
    nk = fin.read().strip()

print(int(partial_perm(int(nk[:2]), int(nk[3]))))