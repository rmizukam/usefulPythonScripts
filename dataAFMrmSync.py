#pip install dirsync
# will sync 
import os
from dirsync import sync
import platform
from functions import choice_for_sync

# print(os.getcwd())
# onMac = '/Users/rmizu/LocalStorage/Repositories/Python/usefulPythonScripts'
# onPC = 'C:\Repositories\Python\usefulPythonScripts'
inLab = True

if platform.system() == 'Windows': 
    if inLab == True:
        dataAFMrmCloudPath = 'C:/Users/014443024/OneDrive - CSULB/RyanMizukami/RProject/dataAFMrm'
        dataAFMrmLocalPath = 'C:/Users/014443024/Desktop/Repositories/R/dataAFMrm'
    else:
        # Sync files from PC (at home) to CLOUD
        # HOME PC -> CLOUD
        dataAFMrmCloudPath = 'C:/Users/Rmizu/Documents/OneDrive - CSULB/RyanMizukami/RProject/dataAFMrm'
        dataAFMrmLocalPath = 'C:/Repositories/R/dataAFMrm'
elif platform.system() == 'Darwin':
    # Will Sync files Locally saved on mac to files save to CLOUD
    # MAC -> CLOUD
    dataAFMrmCloudPath = '/Users/rmizu/Library/CloudStorage/OneDrive-CSULB/RyanMizukami/RProject/dataAFMrm'
    dataAFMrmLocalPath = '/Users/rmizu/LocalStorage/Repositories/R/dataAFMrm'


choice = choice_for_sync()

if choice == '0':
    sync(dataAFMrmCloudPath, dataAFMrmLocalPath, "diff")
elif choice == '1':
    sync(dataAFMrmLocalPath, dataAFMrmCloudPath, "sync")
elif choice == '2':
    sync(dataAFMrmCloudPath, dataAFMrmLocalPath, "sync")
