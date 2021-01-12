import os

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


with open(os.path.join(os.getcwd(),'speeding_up_motif_search/rosalind_kmpp.txt' ), 'rt') as din:
    header, seq = read_fasta(din.readlines()).__next__()
#%%
#pseudocode
#https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
def kmp_table(seq):
    pos = -1
    T = [pos]

    for i, c in enumerate(seq):
        while pos >=0 and seq[pos] != c:
            pos = T[pos]
        pos +=1
        T.append(pos)
    return T[1:]

#%%

with open(os.path.join(os.getcwd(),'speeding_up_motif_search/odpv1.txt' ), 'wt') as fout:
    fout.write(" ".join(map(str, kmp_table(seq))))





