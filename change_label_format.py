# -*- coding: utf8 -*-
import sys
import os

new_fn = sys.argv[1].split('.')
new_fn[0] = new_fn[0]+ ".nlab"

w = open(new_fn[0], mode='w', encoding='UTF-8')

with open(sys.argv[1], mode='r', encoding='UTF-8') as file:
    lines = file.readlines()    
    i = 0
    while i < len(lines):    	
    	lines[i] = lines[i].strip()
    	a = 2
    	while a < 7:    	    
    	    #print(lines[i] + "[%d]"%(a))
    	    w.write(lines[i] + '[%d]'%(a) + '\n')    	    
    	    a += 1
    	i += 1

w.close()
    
    
        
        
        
        
