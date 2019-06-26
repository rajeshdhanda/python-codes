
import numpy as np
n = 4
  
# This function determines if ith and jth row queens are conflicting. 
def conflict(i,j,pos):
    if (pos[i]==pos[j]):
        return True
    elif (abs((pos[i]-pos[j])) == abs(i-j)):
        return True
    else:
        return False    
            

pos = np.zeros(n)
for i0 in range(n):
    pos[0]=i0
    for i1 in range(n):
        pos[1]=i1
        if not(conflict(0,1,pos)):   
            for i2 in range(n):
                pos[2]=i2
                if not((conflict(0,2,pos) or conflict(1,2,pos))):
                    for i3 in range(n):
                        pos[3]=i3
                        if not((conflict(0,3,pos) or conflict(1,3,pos) or conflict(2,3,pos))):
                            print i0,i1,i2,i3
                
                   
                   
