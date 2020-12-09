from itertools import groupby

def fasta_parser ( f_name ) :
    
    with open(f_name) as fh:
        fait = (x[1] for x in groupby( fh, lambda line: line[0] == ">"))

        for header in fait:
            #no need for header / optional
            #headerStr = header.__next__()[1:].strip()
            seq = "".join(s.strip() for s in fait.__next__())
            yield (seq) # if with header, go (headerStr, seq)
            
def to_cod(RNA_string):
    
    rna_codons = {"UUU":"F","UUC":"F","UUA":"L","UUG":"L",
                  "UCU":"S","UCC":"S","UCA":"S","UCG":"S",
                  "UAU":"Y","UAC":"Y","UAA":"","UAG":"",
                  "UGU":"C","UGC":"C","UGA":"","UGG":"W",
                  "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
                  "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                  "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                  "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
                  "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
                  "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                  "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                  "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
                  "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
                  "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                  "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                  "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
    
    protein_strings = []
    
    for mer in range (0, len(RNA_string), 3):
        if RNA_string[mer:mer+3] in rna_codons:
            protein_strings.append(RNA_string[mer:mer + 3])
        
    protein_string = ''.join([rna_codons[codon] for codon in protein_strings ] )
    
    return protein_string


def to_rna(seq):
    tab = str.maketrans("T","U")
    return seq.translate(tab)

def splice_and_translate(path):
    lsq = [x for x in fasta_parser(path)]
    s1 = lsq.pop(0)
    
    for intron in lsq:
        s1 = s1.replace(intron, '')
    return to_cod(to_rna(s1))

def main():
    with open("odp2.txt",'w') as dane_out:
        dane_out.write(splice_and_translate("rosalind_splc.txt"))
    
if __name__ == "__main__":
    main()    
