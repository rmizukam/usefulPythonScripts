import csv
import os
import platform

fileName = 'ListOfRAWFiles'  + '.txt'

if platform.system() == 'Windows':  # windows OS
    folderRAW =  ''
elif platform.system() == 'Darwin':  # macOS
    folderRAW = '/Users/rmizu/Library/CloudStorage/OneDrive-CSULB/RyanMizukami/RAW'

if os.path.exists(folderRAW + '/.DS_Store'):
    os.remove(folderRAW + '/.DS_Store')

fRAW = os.listdir(folderRAW)

with open(fileName, 'w', newline='') as f:
    writer = csv.writer(f)
    for fNAME in fRAW:
        writer.writerow([fNAME])
