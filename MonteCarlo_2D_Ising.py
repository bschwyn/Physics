#Monte Carlo Simulation of 2D Ising model
#using Metropolis Algorithm

import math
import random
import numpy
import matplotlib

my_array = numpy.diag([1,1,1,2,2,2,3,3,3])
print my_array


cmap = matplotlib.colors.ListedColormap(['#E0E0E0', '#FF8C00', '#8c00FF', '00FF8C'])
numpy.pcolor(my_array,cmap=cmap,norm=NoNorm())

size = 10
T = 2.5
sample = 100

def s(row,col):
    if random.random()<.5:
        s = 1
    else: s = -1
    return s

for row in range(1,size):
    for col in range(1,size):
        orientation = s(row,col)
        print '%3d' %(orientation),
    print("\n")




print("end program")
