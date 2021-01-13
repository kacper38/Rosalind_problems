import sys
import os
import itertools
import numpy as np

sys.path.append('/home/kacper/PycharmProjects/Rosalind_problems/finding_spliced_motif')

from spliced_motif_finder import read_fasta
float_formatter = "{:.4f}".format
np.set_printoptions(formatter={'float_kind':float_formatter})


def fasta_parse(filepath):
    with open(filepath, 'rt') as fin:
        faiter = (x[1] for x in itertools.groupby(fin, lambda line: line[0] == '>'))
        for header in faiter:
            header = header.__next__()[1:].strip()
            seq = "".join(seq.strip() for seq in faiter.__next__())
            yield header, seq

def multiple_fasta_parser(filepath):
    return [fasta for fasta in fasta_parse(filepath)]


def p_dist(seq1, seq2):
    assert len(seq1) == len(seq2)
    odp = sum([1 for i in range(len(seq1)) if seq1[i] != seq2[i]])/len(seq1)
    return odp

def gen_matrix(list_of_seq):
    ll = len(list_of_seq)
    matrix = np.zeros((ll,ll), float)
    for i in range(ll):
        for j in range(ll):
            matrix[i][j] = p_dist(list_of_seq[i][1], list_of_seq[j][1])
    return matrix

if __name__ == "__main__":
    try:
        fasta_list = multiple_fasta_parser(sys.argv[1])
        matrix = gen_matrix(fasta_list)
        with open('odp.txt', 'wt') as dout:
            for row in matrix:
                dout.write(np.array2string(row, precision=4, separator=' ')[1:-1]+'\n' )
        print('odp written with succes!')
    except:
        e = sys.exc_info()[0]
        print(e)
















