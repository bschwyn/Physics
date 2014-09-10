#Monte Carlo Simulation of 2D Ising model
#using Metropolis Algorithm

import math
import random

size = 10   #Width of square lattice
T = 2.5     #Temperature in units of e/K
sample = 100

#initialize

for row in range(1,size):
    for col in range(1,size):
       # s(row,col)


#def s(row,col):
#    if rand.random()<.5:
#        s = 1
#    else:
#        s = -1
#    return s
#end s

print("test finished");

#initialize
'''
for row in range(1,size):
    for col in range(1,size):
        s(row,col)
        colorsquare(row,col,s)
#end loops 

        

for i in range(1,sample*size^2):
   row = random.randrange(1,10)
   col = random.randrange(1,10)
   Ediff = deltaU(row,col)
   if Ediff <=0:
        #####?????
       s(row,col)=-s(row,col)
      colorsuqre(row,col)

    elif rand < math.exp(-Ediff/T):
            ###?>???
            s(row,col)=s(row,col)
            colorsquare(i,j)
    #endif
#end loop

def deltaU(row, col):
    #compute deltaU of flippling a dipole
    #periodic boundary conditions
    if row = 1:
        top = s(size,col)
    else:
        top = s(row-1,col)
        
    if row=size:
        bottom = s(1,col)
    else:
        bottom = s(row,col-1)
        
    if col = 1:
        left = s(row,size)
    else:
        left = s(row,col-1)
        
    if col = size:
        right = s(row,1)
    else:
        right = s(row,col+1)

    Ediff = 2*s(i,j)*(top+bottom+left+right)
    return Ediff
#end deltaU

'''

    
        
