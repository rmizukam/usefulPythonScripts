#pip install dirsync

# will sync 
import os
from dirsync import sync
import platform

print(os.getcwd())
# onMac = '/Users/rmizu/LocalStorage/Repositories/Python/usefulPythonScripts'
# onPC = 'C:\Repositories\Python\usefulPythonScripts'

if platform.system() == 'Windows': 
    # Sync files from PC (at home) to CLOUD
    # HOME PC -> CLOUD
    dataAFMrmCloudPath = 'C:/Users/Rmizu/Documents/OneDrive - CSULB/RyanMizukami/RProject/dataAFMrm'
    dataAFMrmLocalPath = 'C:/Repositories/R/dataAFMrm'
elif platform.system() == 'Darwin':
    # Will Sync files Locally saved on mac to files save to CLOUD
    # MAC -> CLOUD
    dataAFMrmCloudPath = '/Users/rmizu/Library/CloudStorage/OneDrive-CSULB/RyanMizukami/RProject/dataAFMrm'
    dataAFMrmLocalPath = '/Users/rmizu/LocalStorage/Repositories/R/dataAFMrm'

choice_for_sync = input('Choose Option\n\
0) Difference Checker\n\
1) Source = Cloud, Destination = Local\n\
2) Source = Local, Destination = Cloud\n\
your choice here: ')

if choice_for_sync == '0':
    sync(dataAFMrmCloudPath, dataAFMrmLocalPath, "diff")
# elif choice_for_sync == '1':
#     sync(dataAFMrmLocalPath, dataAFMrmCloudPath, "sync")
# elif choice_for_sync == '2':
#     sync(dataAFMrmCloudPath, dataAFMrmLocalPath, "sync")
