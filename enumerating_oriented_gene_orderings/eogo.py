import os
from itertools import product, permutations

def answ(n):
    w =[[a*sign for a,sign in zip(i,j)]
        for i in permutations(list(range(1,n+1)))#(6, 5, 4, 3, 1, 2),(6, 5, 4, 3, 2, 1) ...
        for j in product([-1,1], repeat=len(list(range(1, n+1)))) ]#(1, 1, -1, 1, -1, -1),(1, 1, -1, 1, -1, 1).. and rest of possibilities,

    with open(os.path.join(os.getcwd(), 'eogoout.txt'), 'w') as fin:
        fin.write(str(len(w)) + '\n')
        for el in w:
            fin.write(f"{' '.join([str(elm) for elm in el])}\n")
    return 0
