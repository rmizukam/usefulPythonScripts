import os
import re
# import pandas
import platform
# ==============================================================
proj = 'CuPcAnnealing'
initials = 'RM'
tData = 'AFM'
folder_on_Desktop = "220915"
labComputer = False
# =============================================================
if os.path.exists("C:/Users/014443024/Desktop"):
    folder = "C:/Users/014443024/Desktop"
    folder = os.path.join(folder, folder_on_Desktop)
    saveFolder = 'C:/Users/014443024/OneDrive - CSULB/RyanMizukami/RAW'
elif os.path.exists("C:/Users/Rmizu/Desktop"):
    folder = "C:/Users/Rmizu/Desktop"
    folder = os.path.join(folder, folder_on_Desktop)
    saveFolder = 'C:/Users/Rmizu/Documents/OneDrive - CSULB/RyanMizukami/RAW'
elif os.path.exists('/Users/rmizu/desktop'):
    folder = '/Users/rmizu/desktop'
    folder = os.path.join(folder, folder_on_Desktop)
    saveFolder = '/Users/rmizu/Library/CloudStorage/OneDrive-CSULB/RyanMizukami/RAW'
# =============================================================
tdate = '20' + folder[-6:]
pRAW = os.listdir(folder)
for f in pRAW:
    if f.endswith('ibw') and f.startswith('RM'):
        sample = re.findall(r'[A-Z][A-Z]\d{6}[A-Z]{2}\d{2}[A-Z]*', f)[0]
        sampleName = sample[0:2] + '20' + sample[2:]
        endPhrase = re.findall(r'P[A-Za-z]{2,3}\d{2,}', f)
        prepost = re.findall(r'[A-Za-z]+', endPhrase[0])[0]
        if prepost == 'Pos':
            prepost = 'Post'
        imNum = re.findall(r'[^(A-Za-z)]+', endPhrase[0])[0][-2:]
        newName = "_".join([tdate, proj, initials, tData, sampleName, prepost, imNum]) + '.ibw'
        newName = os.path.join(saveFolder, newName)
        oldName = os.path.join(folder, f)
        print(f"Old Name: {oldName}")
        print(f"New Name: {newName}")
        os.rename(oldName, newName)
    # print(data.loc[:, "Sample"])

print("Files Have Been Renamed")
