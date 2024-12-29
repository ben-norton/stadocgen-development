# Data README
This directory contains all original source csv files and the transformed versions as part of StaDocGen for presentation purposes.

## Source Files
| File | Path | URL |
| -- | -- | -- |
| term_versions.csv | app/data/source/term_versions.csv | https://raw.githubusercontent.com/tdwg/dwc/refs/heads/master/vocabulary/term_versions.csv |
| dwcore.csv | app/data/source/dwcore.csv | https://github.com/tdwg/rs.tdwg.org/blob/master/dwcore/dwcore.csv |
| dwcore-versions.csv | app/data/source/dwcore-versions.csv | https://github.com/tdwg/rs.tdwg.org/blob/master/dwcore-versions/dwcore-versions.csv 
| term_versions_revised.csv | app/data/source/term_versions_revised.csv | app/data/source/term_versions.csv (see notes) |

## Notes
1. Source term_versions.csv has encoding issues and contained multiple versions of the same term. All duplicate records were dropped, leaving only the most recent in term_versions_revised.csv.
2. 