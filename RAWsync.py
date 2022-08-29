import os
import platform
from dirsync import sync
from functions import choice_for_sync

lab2Personal = True  # set as true if local folder is behind cloud folder

if platform.system() == 'Darwin':
    # CLOUD -> MAC
    RAWCloudPath = '/Users/rmizu/Library/CloudStorage/OneDrive-CSULB/RyanMizukami/RAW'
    RAWLocalPath = '/Users/rmizu/LocalStorage/Repositories/RAW'
elif platform.system() == 'Windows':
    # CLOUD -> HOME PC
    RAWCloudPath = 'C:/Users/Rmizu/Documents/OneDrive - CSULB/RyanMizukami/RAW'
    RAWLocalPath = 'C:/Repositories/RAW'

choice = choice_for_sync()

if choice_for_sync == '0':
    sync(RAWCloudPath, RAWCloudPath, "diff")
elif choice_for_sync == '1':
    sync(RAWCloudPath, RAWCloudPath, "sync")
elif choice_for_sync == '2':
    sync(RAWCloudPath, RAWCloudPath, "sync")
