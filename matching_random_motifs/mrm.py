import sys

def read_file(filepath):
    with open(filepath, 'rt') as din:
        ns, seq = [el.strip().split() for el in din.readlines()]
    return ns, seq



def gc_computer(seq):
    return seq.count('G')+seq.count('C')


def get_probability(N, s, seq):
    gc = gc_computer(seq)
    at = len(seq) -gc
    p1 = (s/2)**gc
    p2 = ((1-s) / 2 )**at
    prob_no = p1*p2
    prob = 1 - (1-prob_no)**N
    return prob


if __name__ == "__main__":
    try:
        attr, seq = read_file(sys.argv[1])
        print(f'{get_probability(int(attr[0]),float(attr[1]),*seq):.3f}')
    except:
        print(sys.exc_info()[0])

