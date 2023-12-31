import os
from pathlib import Path
from datetime import date
import shutil
import glob
import urllib.request


ts = date.today()
current_dir = Path().absolute()
parent_dir = current_dir.parent

# Make Copies of Existing Markdown Files
namespace = 'ltc'
tspath = str(parent_dir)+'/archive/md/'+namespace+'/'+str(ts)
mdpath = str(parent_dir)+'/md/'+namespace

Path(tspath).mkdir(parents=True, exist_ok=True)
mdfiles = os.listdir(mdpath)
for filename in glob.glob(os.path.join(mdpath, '*.*')):
    shutil.copy(filename, tspath)
# Copy latest version from data standard repo
mdfiles = ['https://github.com/tdwg/ltc/blob/main/assets/md/home-content.md'
    'https://github.com/tdwg/ltc/blob/main/assets/md/quick-reference-header.md'
    'https://github.com/tdwg/ltc/blob/main/assets/md/resources-header.md'
    'https://github.com/tdwg/ltc/blob/main/assets/md/sssom-reference.md'
    'https://github.com/tdwg/ltc/blob/main/assets/md/terms-list-header.md']
for mdfile in mdfiles:
    response = urllib.request.urlopen(mdfile)
    urllib.request.urlretrieve(mdfile, mdpath)

