import sys
from itertools import product


def read_fasta(fp):
    name, seq = None, []
    for line in fp:
        line = line.rstrip()
        if line.startswith(">"):
            if name: yield (name, ''.join(seq))
            name, seq = line, []
        else:
            seq.append(line)
    if name: yield (name, ''.join(seq))



def fastaf_file(filepath):
    with open(filepath ,'rt') as din:
        header, seq = read_fasta(din).__next__()
    return header, seq


def count_substr(seq, sub):
    cnt = 0
    for i in range(len(seq)-4):
        if seq[i:i+4] == sub:
            cnt +=1
    return cnt


def occ_list(filepath):
    _, seq = fastaf_file(filepath)
    alphabet = 'ACGT'
    kmers = []
    pr = product(alphabet, repeat=4)
    for i, j in enumerate(list(pr)):
        kmer = ''
        for item in j:
            kmer += str(item)
        kmers.append(kmer)

    import re
    A = []
    for k in kmers:
        occ = 0
        pattern = re.compile(r'(?=(' + k + '))')
        for l in re.findall(pattern, seq):
            occ +=1
        A.append(occ)
    return A


if __name__ == "__main__":
    print(*occ_list('rosalind_kmerkc.txt'), sep=' ')
