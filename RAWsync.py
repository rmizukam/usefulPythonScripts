import os
import platform
from dirsync import sync

lab2Personal = True  # set as true if local folder is behind cloud folder


if platform.system() == 'Darwin':
    # CLOUD -> MAC
    RAWCloudPath = '/Users/rmizu/Library/CloudStorage/OneDrive-CSULB/RyanMizukami/RAW'
    RAWLocalPath = '/Users/rmizu/LocalStorage/Repositories/RAW'
elif platform.system() == 'Windows':
    # CLOUD -> HOME PC
    RAWCloudPath = 'C:/Users/Rmizu/Documents/OneDrive - CSULB/RyanMizukami/RAW'
    RAWLocalPath = 'C:/Repositories/RAW'

sync(RAWCloudPath, RAWLocalPath, 'sync')

