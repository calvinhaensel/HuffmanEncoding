from priorityqueue import *
from collections import Counter

class Node:
    def __init__(self, freq, char, left, right):
        self.freq = freq
        self.char = char
        self.left = left
        self.right = right

    def __cmp__(self, other):
        return cmp(self.freq, other.freq)

    def __str__(self):
        return "({0}, {1})".format(self.char, self.freq)

    def __repr__(self):
        return self.__str__()

def huffman(X):
    Q = PriorityQueue()
    frequencies = Counter(X) 
    visitedfreq = []
    for c in frequencies:
        N = Node(frequencies[c], c, None, None)
        visitedfreq.append(N.freq)
        if frequencies[c] in visitedfreq:
            for k in frequencies:
                if frequencies[k] == frequencies[c] and k != c:
                    #print('collision of' , c, k)
                    n = min(ord(k), ord(c))
                    frequencies[chr(n)] -= .01
                    N.freq = frequencies[chr(n)]
        for i in frequencies:
            for j in frequencies:
                if frequencies[i] == frequencies[j] and i != j: 
                    m = min(ord(i), ord(j))
                    frequencies[chr(m)]-= .01
                    N.freq = frequencies[chr(m)]
        #print(N.char, N.freq)
    print(frequencies)
    for v in frequencies:
        N = Node(frequencies[v], v, None, None)
        print(N)
        Q.enqueue(N.char, 1.0/N.freq)
        
    while Q.items.numItems > 1:
        n1 = Q.dequeue()
        n2 = Q.dequeue() 
        print(n1, n2)
        if type(n1) == str:
            if type(n2) == Node:
                n3  = Node(frequencies[n1], n1, None, None)
                N = Node(n3.freq + n2.freq, '*', n3, n2)
            else:    
                n3 = Node(frequencies[n1], n1, None, None)
                n4 = Node(frequencies[n2], n2, None, None)
                N = Node(n3.freq + n4.freq, '*',n3, n4)
        elif type(n2) == str:
            n3 = Node(frequencies[n2], n2, None, None)
            N =Node(n1.freq + n3.freq, '*', n1, n3)
        elif type(n1) and type(n2) == Node:
            '''for item in Q:
                if type(item) == str and type(n2)!= str:
                    print(n1.freq//1, frequencies[item]//1, item)
                    if n1.freq//1 == frequencies[item]//1:
                        
                        n2 = Node(frequencies[item], item, None, None)
                        print('thing')
                        N = Node(n1.freq+ n2.freq, '*', n1, n2)
                        break
                else:'''
                    
            N = Node(n1.freq + n2.freq, '*', n1, n2)
                        
        print(N.left, N.right)
        if N.left.freq > N.right.freq and N.left.char != N.right.char:
            N.left, N.right = N.right, N.left
        if N.left.freq == N.right.freq and ord(N.right.char) < ord(N.left.char):
            N.left, N.right = N.right, N.left
        Q.enqueue(N, 1.0/N.freq)
        print( 'this is Q')
        print_queue(Q)
        print(N)
    N = Q.dequeue()
    

    return N




def get_huffman_code(char, root):
    if root.char is None:
        return
    code = ''
    codedict = {}
    get_code_helper(char, root, root, code, codedict)
    return codedict[char]
        
def get_code_helper(char, tree, root, code, codedict):
    if tree:
        if tree.char == char:
            print('found')
            print(code)
            codedict[char] = code
            return
        get_code_helper(char, tree.left, root, code + '0', codedict)
        get_code_helper(char, tree.right, root, code + '1', codedict)
        


def main():
    sent = 'StringTeessttt'
    root = huffman(sent)
    print(get_huffman_code('t', root))
    p = PriorityQueue()
    
    
if __name__=='__main__':
    main()