import os
import re
# import pandas
import platform
# ==============================================================
proj = 'CuPcAnnealing'
initials = 'RM'
tData = 'AFM'
folder_on_Desktop = "220816"
# =============================================================
if platform.system() == 'Windows':
    folder = "C:/Users/Rmizu/Desktop"
    folder = os.path.join(folder, folder_on_Desktop)
    saveFolder = 'C:/Users/Rmizu/Documents/OneDrive - CSULB/RyanMizukami/RAW'
    pNotesAnnealing = '../../R/dataAFMrm/csv/NotesForRM20220701GL0XXSeries.csv'
elif platform.system() == 'Darwin':
    folder = '/Users/rmizu/desktop'
    folder = os.path.join(folder, folder_on_Desktop)
    saveFolder = '/Users/rmizu/Library/CloudStorage/OneDrive-CSULB/RyanMizukami/RAW'
    pNotesAnnealing = '/Users/rmizu/LocalStorage/Repositories/R/dataAFMrm/csv/NotesForRM20220701GL0XXSeries.csv'
# =============================================================
tdate = '20' + folder[-6:]
pRAW = os.listdir(folder)
# data = pandas.read_csv(pNotesAnnealing)
for f in pRAW:
    if f.endswith('ibw') and f.startswith('RM'):
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
# print(data)
# 20220803_CuPcAnnealing_RM_AFM_RM20220701GL02B_Post_13
