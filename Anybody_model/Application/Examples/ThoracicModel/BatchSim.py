# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 10:01:44 2023

@author: jolas
"""

#%%FirstBatchProcessing = rigid instrumentation => We run the data once to collect the l0 of the rectus abdominis and the reaction forces of the instrumentation.
#This is the condition I call "Reac", with completely rigid instrumentation.

import os
import time
from anypytools.abcutils import AnyPyProcess
from anypytools.abcutils import getsubdirs
from anypytools import macro_commands as mc, AnyMacro

#Change the path depending on where the model is
path_Model="C:/Users/acaimi/Desktop/AMMR4-Beta-ammr4-beta/Application/Examples/ThoracicModel"
os.chdir(path_Model)
listd=os.listdir(path_Model+"/Setup/InputAlignment/PythonSim")
cwd = os.getcwd()
print('Current Working Directory is: ', cwd)

abp = AnyPyProcess(num_processes = 2,
                   anybodycon_path = os.path.join('C:/Program Files/AnyBody Technology/AnyBody.8.0','AnyBodyCon.exe'),
                   #anybodycon_path = os.path.join('C:/Users/acaimi/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Rendering & Modelling/AnyBody 7.4.0','AnyBodyCon.exe'),
                   disp = True)


#Retrieve anyfiles in dataframe

sagittal_alignment = [x for x in listd if x.endswith('.any') and not x.startswith('Coronal')]
#coronal_alignment = [x for x in listd if x.endswith('.any') and x.startswith('Coronal')]

sagittal_alignment.sort()
#coronal_alignment.sort()

for i in range(0, len(sagittal_alignment)):
    name=sagittal_alignment[i]
    index = name.find('.')
    sagittal_alignment[i] = name[0:index]
sagittal_alignment = ['"' + item + '"' for item in sagittal_alignment]

#for i in range(0, len(coronal_alignment)):
 #   name=coronal_alignment[i]
  #  index = name.find('.')
   # coronal_alignment[i] = name[0:index]
#coronal_alignment = ['"' + item + '"' for item in coronal_alignment]



macro = []



for i in range(0,len(sagittal_alignment)):
    macro_list =[
         #mc.Load("Thoracic.main.any", defs = {'"PatientID"' : sagittal_alignment[i], '"CoronalPatientID"' : coronal_alignment[i]}), 
         mc.Load("Thoracic.main.any", defs = {'"PatientID"' : sagittal_alignment[i]}), 
         mc.OperationRun("Main.RunApplication"),        
         ]
    macro.append(macro_list)
         
print(macro)              

#Run batch-processing
output = abp.start_macro(macro)
