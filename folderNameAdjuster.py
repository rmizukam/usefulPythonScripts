import os

rawFolder = '/Users/rmizu/Library/CloudStorage/OneDrive-CSULB/RyanMizukami/RAW'

pRAW = os.listdir(rawFolder)

for fname in pRAW:
    if 'SI' in fname: 
        fname_updated = fname.replace('SI', 'Si')
    elif 'GL' in fname:
        fname_updated = fname.replace('GL', 'Gl')
    
    oldName = os.path.join(rawFolder, fname)
    newName = os.path.join(rawFolder, fname_updated)
    
    print(f"Old Name: {oldName}")
    print(f"New Name: {newName}")
    
    # os.rename(oldName, newName)

