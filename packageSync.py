#pip install dirsync
import os
from dirsync import sync
import platform
from functions import choice_for_sync, choice_for_package

if platform.system() == 'Windows':
    if os.path.exists('C:/Users/014443024/Desktop/Repositories/'):
        LocalPath = 'C:/Users/014443024/Desktop/Repositories/'
        CloudPath = 'C:/Users/014443024/OneDrive - CSULB/RyanMizukami/'
        print('You are logged in on the LAB WINDOWS COMPUTER')
    elif os.path.exists('C:/Repositories/'):
        LocalPath = 'C:/Repositories/'
        CloudPath = 'C:/Users/Rmizu/Documents/OneDrive - CSULB/RyanMizukami/'
        print('You are logged in on the PERSONAL WINDOWS COMPUTER')
    else:
        print('Path for R Folder is not found!\nExiting')
        exit()
elif platform.system() == 'Darwin':
    CloudPath = '/Users/rmizu/Library/CloudStorage/OneDrive-CSULB/RyanMizukami/'
    LocalPath = '/Users/rmizu/LocalStorage/Repositories/'
    print('You are logged in on the PERSONAL MAC LAPTOP')
    print('----------------------------------------------------------------------')

rPackage = choice_for_package()

if rPackage == '0':
    LocalPath = LocalPath + 'RAW'
    CloudPath = CloudPath + 'RAW'
elif rPackage == '1':
    LocalPath = LocalPath + 'R/dataAFMrm/'
    CloudPath = CloudPath + 'R/dataAFMrm/'
elif rPackage == '2':
    LocalPath = LocalPath + 'R/cpaAnalysis/'
    CloudPath = CloudPath + 'R/cpaAnalysis/'
elif rPackage == '3':
    LocalPath = LocalPath + 'R/nanoscopeAFM/'
    CloudPath = CloudPath + 'R/nanoscopeAFM/'
elif rPackage == '4':
    LocalPath = LocalPath + 'R/SOP-collection/'
    CloudPath = CloudPath + 'R/SOP-collection/'

choice = choice_for_sync()

if choice == '0':
    print('Source: ', CloudPath)
    print('Target: ', LocalPath)
    sync(CloudPath, LocalPath, "diff")
elif choice == '1':
    print('Source: ', LocalPath)
    print('Target: ', CloudPath)
    sync(CloudPath, LocalPath, "sync")
elif choice == '2':
    print('Source: ', CloudPath)
    print('Target: ', LocalPath)
    sync(LocalPath, CloudPath, "sync")
