# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:46:06 2020

@author: aryam
"""

import os

os.system('cmd /c "ffmpeg -i E:\GOL.mkv -x265-params crf=25 out.mp4"')