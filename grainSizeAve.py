import math

sizesmm = [1, 2.5, 1, 1.3, 1.4, 1.7, 2.0, 0.8, 2.5, 2.4, 1.3, 2, 0.3, 1.6, 1.2, 0.4, 0.3, 1, 1, 1.4]  # mm
sizesmicro = list()

for x in range(0, len(sizesmm)):
    sizesmicro.append(sizesmm[x]/23*1000)

averageSize = sum(sizesmicro)/len(sizesmicro)
print(sizesmicro)
print(averageSize)
