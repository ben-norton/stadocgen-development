import pandas as pd
import shutil
from datetime import date
from pathlib import Path
import os

today = date.today()
ts = today.strftime("%Y%m%d")

namespace = 'mids'

# -------------------------------------------------------
# Paths
currentPath = Path().absolute()
projectPath = currentPath.parent.parent.parent
# Source Files Path
sourceFile = str(projectPath) + '/app/data/source/mids-repo/MIDS-levels-draft.csv'

# Timestamped output path
# Create timestamped folder for working files (works in progress)
targetPath = str(projectPath) + '/app/data/output/'+str(ts)
targetFile = str(targetPath) + '/mids-levels.csv'

# Create timestamped folder if it doesn't exist
if not os.path.isdir(targetPath):
    os.mkdir(targetPath)

# -------------------------------------------------------
# Create copies
# term_src > sourceFile
# term_csv > targetFile
shutil.copy(sourceFile, targetFile)

# -------------------------------------------------------
# Process
# ltc_df > target_df
# Read
df = pd.read_csv(targetFile, encoding="utf8")

# Rename
df.rename(columns={'level': 'term_local_name',
                    'prefLabel': 'alt_label',
                    'shortDescription': 'definition',
                    'longDescription': 'notes'
                   }, inplace=True)

# Revise term_local_name
df['term_local_name'] = df['term_local_name'].str.lower() # Lowercase
df['term_local_name'] = df['term_local_name'].str.replace('-','') # Remove Dash

# Create new preferred label
df['label'] = 'MIDS ' + df['term_local_name'].astype(str) + ' - ' + df['alt_label']
df['label'] = df['label'].str.replace('mids', 'Level ')

# RDF Type
df['rdf_type'] = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Class'

# Qualified Term
df['term_ns_name'] = 'mids:' + df['term_local_name']
df['namespace'] = 'mids:'

# Resave timestamped
df.to_csv(targetFile, index=False, encoding='utf8')
# Copy timestamped to parent folder for merge
outputPath = currentPath.parent
levelsFile = str(outputPath) + '/mids-levels.csv'
shutil.copy(targetFile,levelsFile)

