import os
import re
import pandas
import platform
# ==============================================================
proj = 'CuPcAnnealing'
initials = 'RM'
tData = 'AFM'
folder_on_Desktop = "220810"
# =============================================================
if platform.system() == 'Windows':
    folder = "C:/Users/Rmizu/Desktop"
    folder = os.path.join(folder, folder_on_Desktop)
elif platform.system() == 'Darwin':
    folder = '/users/rmizu/Desktop'
    folder = os.path.join(folder, folder_on_Desktop)
# =============================================================
tdate = '20' + folder[-6:]
pRAW = os.listdir(folder)
pNotesAnnealing = '../../R/dataAFMrm/csv/NotesForRM20220701GL0XXSeries.csv'
data = pandas.read_csv(pNotesAnnealing)
for f in pRAW:
    if f.endswith('ibw') and f.startswith('RM'):
        sample = re.findall(r'[A-Z]{2}\d{6}[A-Z]{2}\d{2}', f)
        sampleName = sample[0][0:2] + '20' + sample[0][2:]
        prepost = re.findall(r'P[a-z]{2,3}', f)
        imNum = re.findall(r'\d{4}', f)[-1][-2:]
        newName = [tdate, proj, initials, tData, sampleName, prepost[0], imNum]
        newName = '_'.join(newName)
        newName = newName + '.ibw'
        newName = os.path.join(folder, newName)
        oldName = os.path.join(folder, f)
        print("Old Name: {oldName}")
        print("New Name: {newName}")
        os.rename(oldName, newName)
    # print(data.loc[:, "Sample"])

# 20220803_CuPcAnnealing_RM_AFM_RM20220701GL02B_Post_13
