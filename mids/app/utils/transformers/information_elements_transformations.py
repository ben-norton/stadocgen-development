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
sourceFile = str(projectPath) + '/app/data/source/mids-repo/mids_information_elements_draft.csv'

# Timestamped output path
# Create timestamped folder for working files (works in progress)
targetPath = str(projectPath) + '/app/data/output/'+str(ts)
targetFile = str(targetPath) + '/mids-information-elements.csv'

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
df.rename(columns={'informationElement_localName': 'term_local_name',
                   'tdwgutility_required': 'is_required',
                   'tdwgutility_repeatable': 'is_repeatable',
                    'usage': 'purpose',
                    'recommendations': 'usage',
                    'term_status': 'editorial_note',
                   }, inplace=True)

# Boolean Columns
df['is_required'] = df['is_required'].str.replace('Yes', 'true')
df['is_required'] = df['is_required'].str.replace('No', 'false')
df['is_repeatable'] = df['is_repeatable'].str.replace('Yes', 'true')
df['is_repeatable'] = df['is_repeatable'].str.replace('No', 'false')

# Move required scope to new scope_note column
regex = r'\((.*)\)'
df['scope_note'] = df['is_required'].str.extract(regex)
df['scope_note'] = df['scope_note'].str.replace('all','All')
df['scope_note'] = df['scope_note'].str.replace('&','and')
# Cleanup is_required
df['is_required'] = df['is_required'].str.replace(r" \(.*?\)", "", regex=True)

# RDF Type
df['rdf_type'] = 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Property'

# Qualified Term
df['term_ns_name'] = 'mids:' + df['term_local_name']

# Drop misused columns (columns related to ratification
df.drop(columns=['term_added','term_modified'], inplace=True)


# Resave
df.to_csv(targetFile, index=False, encoding='utf8')
