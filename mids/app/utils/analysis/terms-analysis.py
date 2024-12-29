import pandas as pd
import shutil
import numpy as np
from datetime import date
from pathlib import Path

# Specify the target of inspection: original source files (sources) or output from transformations (transformations)
sourceType = 'sources'

# Set source and target filenmames
sourceFilename = 'ltc-termlist.csv'
workingFilename = 'ltc-termlist-working.csv'

today = date.today()
ts = today.strftime("%Y%m%d")

# Paths
currentPath = Path().absolute()
projectPath = currentPath.parent.parent.parent

# Source Files Path
sourcePath = str(projectPath) + '/app/data/source'

# Timestamped output path
targetPath = str(currentPath)+'/analysis/'+str(ts)

# -------------------------------------------------------
# Read CSV and Create Dataframes
sourceFile = str(sourcePath)+'/output/' + sourceFilename
targetFile = str(targetPath)+'/working/' + workingFilename
shutil.copy(sourceFile, targetFile)

ltc_df = pd.read_csv(targetFile, encoding="utf8")

# ------------------------------------
# Analysis
