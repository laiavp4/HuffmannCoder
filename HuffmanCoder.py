# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 23:29:21 2018

@author: laia
"""

import collections
import codecs
from time import *
#from bitstring import BitArray

start=time()

fileName = 'quijote.txt'

# CHARACTERS DIVISION
# OJO avoid codification problems of special characters.

with codecs.open(fileName,"r",encoding='utf-8') as f:

    c = collections.Counter(list(f.read()))


freq= []
total =sum(c.values())
for element in sorted(c.items(),key=lambda pair: pair[1], reverse=True):
    freq.append((element[0],element[1]/total))
#    print('valor: ', element[0], 'frecuencia; ', element[1])
    
    print('num. caracters distints: ', len(c))
print('num. total de caracters  ', total)
#print(freq)
probab=dict(freq)
print('Total probabilitat',sum(probab.values()))

def lowest_prob_pair(p):
    '''Return pair of symbols from distribution p with lowest probabilities.'''
    assert(len(p) >= 2) # Ensure there are at least 2 symbols in the dist.

    sorted_p = sorted(p.items(), key=lambda pair:pair[1])
    return sorted_p[0][0], sorted_p[1][0]


def huffman(p):
    '''Return a Huffman code for an ensemble with distribution p.'''
#    print(sum(p.values()))
#    assert(sum(p.values()) == 1.0 ) # Ensure probabilities sum to 1

    # Base case of only two symbols, assign 0 or 1 arbitrarily
    if(len(p) == 2):
        return dict(zip(p.keys(), ['0', '1']))

    # Create a new distribution by merging lowest prob. pair
    p_prime = p.copy()
    a1, a2 = lowest_prob_pair(p)
    p1, p2 = p_prime.pop(a1), p_prime.pop(a2)
    p_prime[a1 + a2] = p1 + p2

    # Recurse and construct code on new distribution
    c = huffman(p_prime)
    ca1a2 = c.pop(a1 + a2)
    c[a1], c[a2] = ca1a2 + '0', ca1a2 + '1'
#    print (c)
    return c

dictionary = huffman(dict(freq))

#Writing the list of characters of the file read with its encoding ordered by the length of the encoding:

with open('compressed.txt','w',encoding='utf-8') as fout:
    fout.write('Key table:')
    fout.write('\n')
#    for element in sorted(dictionary.items()):
    for element in sorted(dictionary.items(),key=lambda pair: len(pair[1]), reverse=False):
        freq.append((element[0],element[1]))

        fout.write('\'')
        if element[0] == '\n':
            fout.write('CR')
        else:
            fout.write(element[0])
        fout.write('\'')
        fout.write(': ')
        fout.write(element[1])        
        fout.write('\n')
     
    fout.write('\n')  
    fout.write('Quijote codified')
    fout.write('\n')

#Llegim el fitxer i el codificam:

    with open(fileName,'r',encoding='utf-8') as fin:
        byteArray = bytearray()
        NameOutFile = 'QuijoteCompressed.bin'
    
        with open (NameOutFile,'wb') as fbytes:
            codelist=list(fin.read())
            charlist = ''
            for i in range (len(codelist)):
                codelist[i] = dictionary[codelist[i]]
                fout.write(codelist[i])
                
                for j in range (len(codelist[i])):
                    charlist += (str(codelist[i][j]))
            print(charlist)        
            for j in range (0,len(charlist),8): #From str to bytes
                byteArray.append(int(charlist[i:i+8],2))
                fbytes.write(bytes(byteArray))
                
                
fout.close()
fin.close()



end=time()
print ("time coding=", end-start)

