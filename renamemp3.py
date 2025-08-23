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
    for curFile in fileList:
        audio = EasyID3(curFile)
        try:
            artist = audio.get("artist")[0]
            title = audio.get("title")[0]
            curPath = os.path.dirname(curFile)
            newName = f"{curPath}\{artist} - {title}.mp3"
            os.rename(curFile,newName)
        except:
            print("Artist and title not found. Skipping file.")
            
