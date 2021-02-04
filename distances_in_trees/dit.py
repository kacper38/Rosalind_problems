import sys
import re



def nwck(tree, node1, node2):
    n1i = tree.find(node1)
    n2i = tree.find(node2)


    trav = [i for i in tree[min(n1i, n2i):max(n1i, n2i)] if i in [')','(',',']]
    bracket = ''

    for i in trav:
        bracket +=i

   # print(bracket)
    while '(,)' in bracket:
        bracket = bracket.replace('(,)', '')
        #print(bracket,'1')
    if bracket.count('(') == len(bracket):
        #print(bracket,'2')
        return len(bracket)
    elif bracket.count(')') == len(bracket):
        #print(bracket,'3')
        return len(bracket)
    elif bracket.count(',') == len(bracket):
        #print(bracket,'4')
        return 2
    else:
        #print(bracket,'5')
        return bracket.count(')') + bracket.count('(') + 2

#https://en.wikipedia.org/wiki/Newick_format#:~:text=In%20mathematics%2C%20Newick%20tree%20format,Maddison%2C%20Christopher%20Meacham%2C%20F.

if __name__ == "__main__":
    filep = sys.argv[1]
    with open(filep, 'rt') as din:
        trees = [x.strip().replace(':','') for x in din.readlines() if len(x.strip()) > 0]

    for it in range(0, len(trees), 2):
        tree = trees[it]
        n1, n2 = trees[it+1].split(' ')
        print(nwck(tree,n1,n2), end=' ')
       # print(n1,'  ' ,n2, '\n')
        #print(tree.find(n1))









