import os
import platform
from dirsync import sync
from functions import choice_for_sync

inLab = False

if platform.system() == 'Darwin':
    # CLOUD -> MAC
    RAWCloudPath = '/Users/rmizu/Library/CloudStorage/OneDrive-CSULB/RyanMizukami/RAW'
    RAWLocalPath = '/Users/rmizu/LocalStorage/Repositories/RAW'
elif platform.system() == 'Windows':
    if inLab == True:
        RAWCloudPath = 'C:/Users/014443024/OneDrive - CSULB/RyanMizukami/RAW'
        RAWLocalPath = 'C:/Users/014443024/Desktop/Repositories/RAW'
    else:
        # CLOUD -> HOME PC
        RAWCloudPath = 'C:/Users/Rmizu/Documents/OneDrive - CSULB/RyanMizukami/RAW'
        RAWLocalPath = 'C:/Repositories/RAW'

choice = choice_for_sync()

if choice == '0':
    # sync(source, target)
    sync(RAWCloudPath, RAWLocalPath, "diff")
elif choice == '1':
    sync(RAWCloudPath, RAWLocalPath, "sync")
elif choice == '2':
    sync(RAWLocalPath, RAWCloudPath, "sync")
