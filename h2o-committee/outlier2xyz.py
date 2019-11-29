import json
from ipi.utils.io import read_file_raw
import numpy as np
import math


def dotproduct(v1, v2):
    return sum((a*b) for a, b in zip(v1, v2))

def length(v):
    return math.sqrt(dotproduct(v, v))

def angle(v1, v2):
    angle_rad=math.acos(dotproduct(v1, v2)/ (length(v1)*length(v2)))
    return angle_rad/np.pi * 180




#get atom species list
initfile = open('init.pdb')
species = read_file_raw('pdb', initfile)['names']
print(type(species))

filename="simulation.extra_0"



# open function is just pointer, process file step by step
fr=open("simulation.extra_0", 'r')
fw=open("conversion.xyz", 'w')
for idx, line in enumerate(fr.readlines()):
    if (idx%2 == 0):
        continue
#        print(line.split())
    else:
        info=json.loads(line)
        #load cell info and reshape
        cell_tmp=info["cell"]
        cell_tmp=np.reshape(cell_tmp, (3,3))
        print(cell_tmp)
        #load position info and reshape
        pos_tmp=info["position"]
#        cmt_tmp=info["committee"]
#        print cmt_tmp
        num_atoms=len(pos_tmp)/3
        pos_tmp=np.reshape(pos_tmp,(num_atoms,3))
#        print(num_atoms)
#        print(pos_tmp.shape)
        fw.write(str(num_atoms)+"\n")
        fw.write("# CELL(abcABC):")
        for i in range(3):
            tmp=length(cell_tmp[i])
            fw.write("    %5.5f"%(tmp))
        for i in range(3):
            for j in range(i):
                tmp=angle(cell_tmp[i],cell_tmp[j])
                fw.write("    %5.5f"%(tmp))
        #for furture use
        fw.write("  Step:           0  Bead:       0 positions{atomic_unit}  cell{atomic_unit}\n")
        for i in zip(list(species), list(pos_tmp)):
            fw.write("%5s   %5.5e   %5.5e   %5.5e\n"%(i[0],i[1][0],i[1][1],i[1][2]))
fr.close()
