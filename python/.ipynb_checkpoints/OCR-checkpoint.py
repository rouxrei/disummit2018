# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 14:17:12 2018

@author: rouxrei
"""
import os
import subprocess

# define input path
project_wd = os.getcwd()
extracted_img_dir = os.path.join(project_wd, 'data', 'medicine', 'hiv_and_aids_act_parts')
target_file = os.path.join(project_wd, 'data', 'medicine', 'hiv_and_aids_act.txt')

# to make following code a little simpler, change working directory to image folder
os.chdir(extracted_img_dir)
for filename in os.listdir(extracted_img_dir):
    basename = filename[:-4]
    pngname = basename + '.png'
    # call 3rd party tools 'convert' and 'tesseract'
    subprocess.check_output(['convert.exe', filename, pngname], shell=True)
    subprocess.check_output(['tesseract.exe', pngname, basename], shell=True)
    
# return to project working directory    
os.chdir(project_wd)

# concat different txt files into a single file
with open(target_file, 'ab') as target_txt:
    for filename in os.listdir(extracted_img_dir):
        if filename[-4:] == '.txt':
            with open(os.path.join(extracted_img_dir, filename), 'rb') as part_txt:
                target_txt.write(part_txt.read())