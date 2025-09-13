# -*- coding: utf-8 -*-
"""
I have a bunch of folders with arbitrary names from an old Ipod. 
This script gets the artist metadata, creates a folder for each unique artist,
and moves the files into that folder.
It also renames the MP3s at the end, but that part is commented out.
"""

from mutagen.easyid3 import EasyID3
import os
import glob
import shutil
from pathvalidate import sanitize_filepath

# Enter the main folder that contains your music files.
mainFolder = r"F:\PLEX_MEDIA\Music\Other_Backup"



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

def validFilename(s):
    """
    Changes a string into a valid filename.
    """
    return "".join(x for x in s if x.isalnum())

def renamefile(curFile):
    try:
        audio = EasyID3(curFile)
        artist = audio.get("artist")[0]
        title = audio.get("title")[0]
        curPath = os.path.dirname(curFile)
        newName = f"{curPath}\{artist} - {title}.mp3"
        os.rename(curFile,newName)
    except:
        print("Artist and title not found. Skipping file.")   
    try:
        audio['albumartist'] = artist
        audio.save()
    except:
        pass
        
def getartistinfo(fileList):
    # This function returns a dictionary of artists from a list of mp3 files
    artistInfo = {}
    for curFile in fileList:
        try:
            audio = EasyID3(curFile)
            artist = audio.get("artist")[0]
            artist = sanitize_filepath(artist)
            artistInfo[curFile] = artist
        except:
            #print("Artist not found. Skipping file.")  
            pass
            
    return artistInfo


# Here is the main body of the code.
# Get a list of all the folders
folderList = has_subfolders_listdir(mainFolder)

# Create blank dictionary that artist names will be stored in
artistInfo = {}
# Create list of all files
allfiles = []
# Get all artists in my folders
for folder in folderList:
    fileList = get_mp3_files_glob(f"{mainFolder}\{folder}")
    allfiles.extend(fileList)
    artistInfo.update(getartistinfo(fileList))
    
# Get unique artist names
allArtists = set(artistInfo.values()) 

# Create all the artist folders
for artist in allArtists:
    folder_path = mainFolder + "\\" + artist
    os.makedirs(folder_path, exist_ok=True)
    
# Move files to new artist folder
for curFile in allfiles:
    try:
        newlocation = mainFolder + "\\" + artistInfo[curFile]
    except: 
        pass
    try:
        shutil.move(curFile,newlocation)
    except:
        pass

# The block of code below renames files. I already did it so it's comented.
# # If there are no subfolders, then search the main folder
# if not folderList:
#     fileList = get_mp3_files_glob(f"{mainFolder}")
#     for curFile in fileList:
#         renamefile(curFile)    
# # If there are subfolders, search subfolders        
# for folder in folderList:
#     fileList = get_mp3_files_glob(f"{mainFolder}\{folder}")
#     for curFile in fileList:
#         renamefile(curFile)
            
