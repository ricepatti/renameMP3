# -*- coding: utf-8 -*-
"""
Rename all my MP3 files.
"""

from mutagen.easyid3 import EasyID3
import os
import glob

# Enter the main folder that contains your music files.
mainFolder = r"F:\test"



# Here are the functions that the code uses.
def getmusicfiles(folder):
    """
    Returns all files.
    """    
    all_entries = os.listdir(folder)
    allfiles = [entry for entry in all_entries if os.path.isfile(os.path.join(folder, entry))]
    return [entry for entry in allfiles if os.path.splitext(allfiles)[1] == ".mp3"]

def get_mp3_files_glob(directory_path):
    """
    Returns a list of MP3 files in the specified directory.
    """
    return glob.glob(f"{directory_path}/*.mp3")

def has_subfolders_listdir(folder):
    """
    Checks if a directory contains any subfolders using os.listdir() and os.path.isdir().
    """
    all_entries = os.listdir(folder)
    return [entry for entry in all_entries if os.path.isdir(os.path.join(folder, entry))]



# Here is the main body of the code.
folderList = has_subfolders_listdir(mainFolder)


for folder in folderList:
    fileList = get_mp3_files_glob(f"{mainFolder}\{folder}")
    for file in fileList:
        metadata = EasyID3(file)

    

# Code below for reference only.
curFile = r"F:\test\F41\POAF.mp3"
curPath = os.path.dirname(curFile)

audio = EasyID3(curFile)

artist = audio.get("artist")[0]
title = audio.get("title")[0]
album = audio.get("album")[0]

newName = f"{curPath}\{artist} - {title}.mp3"

os.rename(curFile,newName)

    
    
    
    