import os.path
import PySimpleGUI as sg
import re

source_folder_column = [
    [
        sg.Text("Source Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(key="-SOURCEFOLDER-"),
    ]
]

target_folder_column = [
    [
        sg.Text("Target Folder"),
        sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),
        sg.FolderBrowse(key="-TARGETFOLDER-"),
    ]
]

project_name = [
    sg.Text('Project Name'),
    sg.Input(key="-PROJECTNAME-")
]

user_initials = [
    sg.Text('User Initials'),
    sg.Input(key="-USERINITIALS-")
]

instrument_used = [
    sg.Text('Instrument Used'),
    sg.Input(key="-INSTRUMENTUSED-")
]

additional_information = [
    sg.Text('Additional Information'),
    sg.Input(key="-ADDITIONALINFORMATION-")
]

# ----- Full layout -----
layout = [
    [source_folder_column],
    [target_folder_column],
    [user_initials],
    [project_name],
    [instrument_used],
    [additional_information],
    [sg.Button('Rename Folder')]
]

window = sg.Window("Gredig Lab File Renamer", layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "Rename Folder":
        folder = values["-SOURCEFOLDER-"]
        saveFolder = values["-TARGETFOLDER-"]
        proj = values["-PROJECTNAME-"]
        initials = values["-USERINITIALS-"]
        type_Data = values["-INSTRUMENTUSED-"]
        additonal_Info_FromWindow = values["-ADDITIONALINFORMATION-"]

        date = "20" + folder[-6:]
        pRAW = os.listdir(folder)
        
        for f in pRAW:
            if f.endswith('.ibw'):
                split_Str_FileExt = f.split('.')
                fileExt = split_Str_FileExt[1]
                split_Str_sampleName = split_Str_FileExt[0].split('_')
                sampleName = split_Str_sampleName[0][0:2] + str(20) + split_Str_sampleName[0][2:]
                additonal_Info_FromName = re.findall(r'[(A-za-z)]+', split_Str_sampleName[1])[0]
                image_number = re.findall(r'\d+', split_Str_sampleName[1])[0][-2:]    
                
                # New Name Construction
                if additonal_Info_FromWindow == '':
                    nameArray = [date, proj, initials, type_Data, sampleName, additonal_Info_FromName, image_number]
                else:
                    nameArray = [date, proj, initials, type_Data, sampleName, additonal_Info_FromName, additonal_Info_FromWindow, image_number]

                newName = "_".join(nameArray) + '.' + fileExt

                newName = os.path.join(saveFolder, newName)
                oldName = os.path.join(folder, f)
                print(f"Old Name: {oldName}")
                print(f"New Name: {newName}")
                os.rename(oldName, newName)


window.close()