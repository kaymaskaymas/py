import numpy as np
import csv

data =  np.loadtxt("in.txt",usecols=range(1,4),delimiter=",")
print("marks data\n",data)

avg=np.array([])
for marks in data:
    avg=np.append(avg,round(np.mean(marks),2))
    
print("Averages are:")
for mks in avg:
    print(mks)
    
with open("in.txt") as inf:
    with open("out.txt",'w') as out:
        r=csv.reader(inf)
        i=0
        for line in r:
            out.write(line[4]+','+str(avg[i])+'\n')
            i=i+1

print("Class topper has scored avg marks:",np.max(avg))

            
