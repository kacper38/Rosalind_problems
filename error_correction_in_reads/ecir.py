import sys
from collections import defaultdict


def reverse_complement(seq):
    tab = str.maketrans("ACTG","TGAC")
    return (seq.translate(tab)[::-1])


def read_fasta(fasta):
    name, seq = None, []
    for line in fasta:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))


def hamming_dist(seq1, seq2):
    dist = 0
    for i in range(len(seq2)):
        if seq1[i] != seq2[i]:
            dist +=1
    return dist


def fasta_dict(filepath):
    with open(filepath, 'rt') as din:
        fasta_dict = {header : seq for (header,seq) in read_fasta(din)}
    return fasta_dict



def ndt(fastadict):
    right = []
    wrong = []
    els = list(fastadict.values())
    for i,seq in enumerate(els):
        rseq = reverse_complement(seq)
        for j in range(i+1, len(fastadict)):
            if seq == els[j] or rseq == els[j]:
                if seq not in right and rseq not in right:
                    right.append(seq)
                    right.append(rseq)
    for seq in els:
        if seq not in right:
            wrong.append(seq)


    with open('odp.txt', 'wt') as dot:

        for inc in wrong:
            for corr in right:
                if hamming_dist(inc, corr) == 1:
                    dot.write(f'{inc}->{corr}\n')
                    #print(inc,'->',corr, sep='', file=dot)





if __name__ == "__main__":


    ndt(fasta_dict(sys.argv[1]))













