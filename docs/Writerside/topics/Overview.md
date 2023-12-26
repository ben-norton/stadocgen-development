# Overview
StaDocGen = Data Standards Documentation Generator


## Architecture
Stadocgen is built using Python 3.11 and the Flask Framework.



## Folders
Repo Folders
app - Main Application Folder
app\data - Source and Target Data Files
app\data\ltc - Latimer Core data files
app\data\ltc\ltc-docs - Target for transformed source files for use to generate webpages
app\data\ltc\ltc-source - Source files copied from source github repository, these files are preserved in their original source state.
app\data\ltc\schemas - Table schemas generated from csv files (see w3c table schemas)
