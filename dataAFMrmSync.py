#pip install dirsync
import os
from dirsync import sync

# print(os.getcwd())
onMac = '/Users/rmizu/LocalStorage/Repositories/Python/usefulPythonScripts'
onPC = ''

if os.getcwd() == onMac:
    # Will Sync files Locally saved on mac to files save to CLOUD
    # MAC -> CLOUD
    dataAFMrmCloudPath = '/Users/rmizu/Library/CloudStorage/OneDrive-CSULB/RyanMizukami/RProject/dataAFMrm'
    dataAFMrmLocalPath = '/Users/rmizu/LocalStorage/Repositories/R/dataAFMrm'
elif os.getcwd() == onPC:
    # Sync files from PC (at home) to CLOUD
    # HOME PC -> CLOUD
    dataAFMrmCloudPath = ''
    dataAFMrmLocalPath = ''

sync(dataAFMrmLocalPath, dataAFMrmCloudPath, "sync")
