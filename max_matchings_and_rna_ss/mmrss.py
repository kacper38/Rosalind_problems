from collections import defaultdict
from math import factorial
from itertools import groupby




def fasta_parser(f_name):
    with open(f_name) as fh:
        fait = (x[1] for x in groupby(fh, lambda line: line[0] == ">"))

        for header in fait:
            # no need for header / optional
            # headerStr = header.__next__()[1:].strip()
            seq = "".join(s.strip() for s in fait.__next__())
            yield (seq)  # if with header, go (headerStr, seq)


def count_perm(rna):
    npr = lambda n,r: factorial(n) // factorial(n-r)

    cd = {'A':0,'U':0,'C':0,'G':0}
    for base in rna : cd[base] +=1
    A,U,C,G = cd.values()

    if A > U :
        AU = npr(A,U)
    else :
        AU = npr(U,A)

    if C > G:
        CG = npr(C,G)
    else :
        CG = npr(G,C)
    return int(AU*CG)


from os.path import dirname

seq = [x for x in fasta_parser(dirname(__file__) + "/rosalind_mmch.txt")]

c1 = count_perm(seq[0])
