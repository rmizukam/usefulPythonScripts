import os
from dirsync import sync

lab2Personal = True  # set as true if local folder is behind cloud folder

# print(os.getcwd())
onMac = '/Users/rmizu/LocalStorage/Repositories/Python/usefulPythonScripts'
onPC = ''

if os.getcwd() == onMac:
    # CLOUD -> MAC
    RAWCloudPath = '/Users/rmizu/Library/CloudStorage/OneDrive-CSULB/RyanMizukami/RAW'
    RAWLocalPath = '/Users/rmizu/LocalStorage/Repositories/RAW'
elif os.getcwd() == onPC:
    # CLOUD -> HOME PC
    RAWCloudPath = ''
    RAWLocalPath = ''

sync(RAWCloudPath, RAWLocalPath, 'diff')

