import os
from itertools import product

if __name__ == '__main__':

    #jn = ["".join(p) for p in set(product(alphabet, repeat=num))]

    def get_ans(file_name):
        with open(os.getcwd() + '/'+file_name, 'r') as fin:
            alphabet = [letter.strip() for letter in fin.readline() if letter.isalpha()]
            num = int(fin.readline())

        #jn = ["".join(p) for p in set(product(alphabet, repeat=num))]

        with open(os.getcwd() + '/ans.txt', 'w') as fout:
            for item in sorted(["".join(p)
                                for p in set(product(alphabet, repeat=num))],
                               key=str):
                fout.write(item.strip())
                fout.write('\n')

    get_ans('rosalind_lexf.txt')


