import sys


s1 = 'AACCTTGG'
s2 = 'ACACTGTGA'

#check if there's a needle in a haystack
#it = iter(s1)
#print(all(x in it for x in o1))


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

def lcs(seq1, seq2):

    x,y = len(s1), len(s2)

    lens = [[ 0 for j in range(y + 1)] for i in range(x + 1)]

    for i, cs1 in enumerate(s1):
        for j, cs2 in enumerate(s2):
            if cs1 == cs2:
                lens[i+1][j+1] = lens[i][j] + 1
            else:
                lens[i+1][j+1] = max(lens[i+1][j], lens[i][j+1])


    sm = ''
    while x*y != 0:
        if lens[x][y] == lens[x-1][y]:
            x -=1
        elif lens[x][y] == lens[x][y-1]:
            y -=1
        else:
            sm = s1[x-1] + sm
            x -=1
            y -=1


    return sm

if __name__ == "__main__":
    fasta_path = sys.argv[1]
    with open(fasta_path, 'rt') as din:
        seqs =[ seq for (_,seq) in read_fasta(din)]
        s1 = max(seqs)
        s2 = min(seqs)
        #print(s1)
        #print(s2)
        out = lcs(s1,s2)
        print(out)
#algo from -> https://www.programiz.com/dsa/longest-common-subsequence#:~:text=The%20longest%20common%20subsequence%20(LCS,positions%20within%20the%20original%20sequences.
