import numpy as np
import sys
from scipy import stats



def readlines(fname):
    lines = []
    with open(fname) as f:
        lines = f.readlines()
        for l in range(len(lines)):
            lines[l] = [int(i) for i in list(lines[l].strip())]
            
    matrix = np.array(lines)
    return matrix
    

print(stats.mode(readlines(sys.argv[1])))

