import csv
from config import get_project_root
import pandas as pd
import urllib.request
import shutil

root = get_project_root()

# Mapping source files are stored as *.tsv (tab-delimited). StaDocGen parses CSV when generating documentation. This script converts the source tsv to source csv.
# Files:
dwc_filestem = 'sssom_mids_dwc_biology_02'
dwc_repofile = 'https://raw.githubusercontent.com/tdwg/mids/refs/heads/main/sssom-mapping/dwc/biology/sssom_mids_dwc_biology_02.sssom.tsv'
dwc_localtsv = str(root) + '/mids/app/data/source-files/mids-repo/mappings/' + dwc_filestem + '.tsv'
dwc_localcsv = str(root) + '/mids/app/data/source-files/mids-repo/mappings/' + dwc_filestem + '.csv'
dwc_sssomfile = str(root) + '/mids/app/data/output/mids-dwc-sssom.csv'
dwc_uniquecsv = str(root) + '/mids/app/data/source-files/mids-repo/mappings/dwc_unique_class_property_pairs.csv'

abcd_filestem = 'sssom_mids_abcd_biology_02'
abcd_repofile = 'https://raw.githubusercontent.com/tdwg/mids/refs/heads/main/sssom-mapping/abcd/biology/sssom_mids_abcd_biology_02.sssom.tsv'
abcd_localtsv = str(root) + '/mids/app/data/source-files/mids-repo/mappings/' + abcd_filestem + '.tsv'
abcd_localcsv = str(root) + '/mids/app/data/source-files/mids-repo/mappings/' + abcd_filestem + '.csv'
abcd_sssomfile = str(root) + '/mids/app/data/output/mids-abcd-sssom.csv'
abcd_uniquecsv = str(root) + '/mids/app/data/source-files/mids-repo/mappings/abcd_unique_class_property_pairs.csv'

def download(url, localfile):
    urllib.request.urlretrieve(url, localfile)

def convert_tsv_to_csv(source, target):
    with open(source, 'r') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        with open(target, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in reader:
                if row:
                    writer.writerow(row)

# Download both Mapping Files
download(dwc_repofile, dwc_localtsv)
download(abcd_repofile, abcd_localtsv)

# Convert Files
convert_tsv_to_csv(dwc_localtsv, dwc_localcsv)
convert_tsv_to_csv(abcd_localtsv, abcd_localcsv)

# Generate Unique Class-Property Pairs for DWC
df_dwc = pd.read_csv(dwc_localcsv, encoding="utf8")
df1 = df_dwc[['sssom:subject_category','sssom:subject_id']].drop_duplicates()
df1.rename(columns={'sssom:subject_id': 'qualified_term',
                    'sssom:subject_category': 'class_name'
                   }, inplace=True)
df1['term_local_name'] = df1['qualified_term'].str.replace('mids:', '')
df1.to_csv(dwc_uniquecsv, index=False, encoding='utf8')

# Generate Unique Class-Property Pairs for ABCD
df_abcd = pd.read_csv(abcd_localcsv, encoding="utf8")
df2 = df_abcd[['sssom:subject_category','sssom:subject_id']].drop_duplicates()
df2.rename(columns={'sssom:subject_id': 'qualified_term',
                    'sssom:subject_category': 'class_name'
                   }, inplace=True)
df2['term_local_name'] = df2['qualified_term'].str.replace('mids:', '')
df2.to_csv(abcd_uniquecsv, index=False, encoding='utf8')

# Create copies of both mappings files in output directory
shutil.copy(dwc_localcsv, dwc_sssomfile)
shutil.copy(abcd_localcsv, abcd_sssomfile)