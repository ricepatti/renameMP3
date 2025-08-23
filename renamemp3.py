# -*- coding: utf-8 -*-
"""
Rename all my MP3 files.
"""

from mutagen.easyid3 import EasyID3

curFile = r"F:\test\F41\ABXA.mp3"

audio = EasyID3(curFile)

artist = audio.get("artist")[0]
title = audio.get("title")[0]
album = audio.get("album")[0]