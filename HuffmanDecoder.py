# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 17:19:55 2018

@author: laia
"""

import collections
import codecs
from time import *
import os as os


start=time()

fileName = 'quijote - original.bin'

with open(fileName,'rb') as fin:
    file = fin.read()
    fin.seek(0)
    extrazeros=ord(fin.read(1)) #Search added zeros.
 
    bits=''
    dictionary={}
    l_bits=int(bin(ord(fin.read(1)))[2:].rjust(8,'0')+bin(ord(fin.read(1)))[2:].rjust(8,'0'),2)
    l_bytes=int(bin(ord(fin.read(1)))[2:].rjust(8,'0'),2)
    l=int((l_bits)/(l_bytes+2))
    larchiv=len(file)-1-l_bits-3
    for i in range(l):
        chain=''
        letra=chr(ord(fin.read(1)))
        len_chain=ord(fin.read(1))
        for j in range(l_bytes):
            chain+=bin(ord(fin.read(1)))[2:].rjust(8,'0')
        dictionary[chain[-len_chain:]]=letra
    with open('ultimo.txt','w') as ultimo:
        for i in range(larchiv):
            ultimo.write(bin(ord(fin.read(1)))[2:].rjust(8,'0'))


with open('ultimo.txt','r') as f:
    c=f.read()
    l=len(c)-extrazeros
    chain=''
    f.seek(0)
    nombre2=fileName+'_decoded.txt'
    with open(nombre2,'w') as dcompressed2:
#    with open('quijote_decoded.txt','w') as dcompressed2:
        for i in range(l):
            chain+=f.read(1)
            if chain in dictionary:
                dcompressed2.write(dictionary[chain])
                chain=''

os.remove('ultimo.txt')
end=time()
print("time decoding=", end-start)
    
    
