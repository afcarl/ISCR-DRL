import os
import sys

for i in range(int(sys.argv[1]),int(sys.argv[2])+1,1):
    os.system('qdel '+str(i))




