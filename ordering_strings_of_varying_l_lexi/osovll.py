import os
from itertools import product, chain

if __name__ == '__main__':

    def get_answ(file_name):

        with open(os.path.join(os.getcwd(), file_name), 'r') as fin:
            alphabet = [letter.strip() for letter in fin.readline() if letter.isalpha()]
            num = int(fin.readline())

        listt = []
        for i in range(1, num + 1):
            listt.append(["".join(p) for p in set(product(alphabet, repeat=i))])

        list_chain = list(chain(*listt))

        with open(os.getcwd() + '/answe.txt', 'w') as fout:
            for item in sorted(list_chain, key=lambda x: [alphabet.index(c) for c in x]):
                fout.write(item.strip())
                fout.write('\n')


    get_answ('rosalind_lexv.txt')
