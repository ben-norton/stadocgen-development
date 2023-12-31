import os
from pathlib import Path
from datetime import date
import shutil
import glob
import urllib.request
import yaml
import pandas as pd

namespace = 'ltc'
csvname = namespace+"-vocab-sourcePaths.csv"

today = date.today()
ts = today.strftime("%Y%m%d")
current_dir = Path().absolute()
parent_dir = current_dir.parent

config_dir = str(current_dir.parent)+'/config'

destinationPath = str(parent_dir)+'/archive/'+namespace+'/'+str(ts)
targetPath = str(parent_dir)+'/data/'+namespace+'/ltc-source'

if not os.path.isdir(targetPath):
    os.mkdir(targetPath)

if os.path.isdir(destinationPath):
    shutil.rmtree(destinationPath)

dest = shutil.move(targetPath, destinationPath)

# Copy new versions
srcRepo = os.path.abspath("G:/repos/ltc/source/terms")
target = str(parent_dir)+'/data/'+namespace+'/ltc-source'

if os.path.exists(targetPath):
    shutil.rmtree(targetPath)
shutil.copytree(srcRepo, targetPath)







