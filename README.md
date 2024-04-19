# StaDocGen - *Development*
**Development Version** of the Web-based Documentation Generator for TDWG Data Standards  
Built using Python Flask, the application transforms a set of CSV files into data standards documentation pages. This application is currently under active development. The current iteration of the application is being used to generate the docs here: [https://tdwg.github.io/ltc](https://tdwg.github.io/ltc). The main application is located under StaDocGen. Ltc is a legacy application that was migrated from the Latimer Core repository.

## Application Specifications

### Naming Conventions for Files
| Extension | Convention                              | Example              |
| --------- | --------------------------------------- | -------------------- |
| html      | Concepts are separated with hyphens     | quick-reference.html |
| py        | Concepts are separated with underscores | quick_reference.py   |
| md        | Concepts are separated with underscores | quick_reference.md   |
| (folder)  | Concepts are separated with underscores | app/quick_reference/ |
| csv       | Concepts are separated with hyphens     | quick-reference.csv  |

```
├───app
│   ├───build       | Static html files generated using Frozen Flask (https://pythonhosted.org/Frozen-Flask/)
│   ├───config      | Working standard-specific configuration files to populate standards level metadata (currently in development)
│   ├───data        | Source data files in csv format
│   │   ├───global
│   │   ├───ltc
│   │   │   ├───ltc-docs    | Source data post-transformation scripts
│   │   │   └───ltc-source  | Original source data files
│   │   │   └───ltc-source  | Tabular data schemas generated from the source CSV files (not part of the core stadocgen app)
│   ├───md          | Specific content blocks in markdown format 
│   │   └───ltc     | Markdown associated with Latimer Core Documentation
│   │   └───tdwg    | Latest versions of official TDWG documentation markdown content, these files are then customized for each standard
│   ├───static      | Static assets (css, js, icons)
│   │   └───assets  | Standard static assets (do not change)
│   │   └───images  | Stanard-specific custom imagery 
│   │   └───custom  | Customized CSS overrides and javascript files that extend and alter the standardized template files under assets.
│   ├───templates   | Jinja templates
│   ├───utils       | Data transformation utilities 
_init__.py
freeze.py   Frozen flask script to generate build files
routes.py   Dynamic flask script
```
 
### Commands
Testing
* Open a command prompt in the project root directory
* Enter *flask run*
* Open a browser to localhost:5000

Build Docs
* Open a command prompt in the app subdirectory (/app) 
* Enter *python freeze.py build*
* Copy the entire contents of the build directory (/app/build) to the docs folder in the target repository
* Publish changes using the appropriate GitHub workflow

In Windows, robocopy can be used to replace files in a target directory with a source. The following command will accomplish this task (before using, make sure to update the paths)  
robocopy C:\repos\stadocgen\app\build G:\repos\ltc\docs /mir
Once the new build is pushed to the target repo, continue the standard protocol for updating a repository (create new branch with updated docs > pull request > approve > merge).  

### Important Changes between routes.py and freeze.py
1. In freeze.py, all route names must be bound with both leading and trailing forward slashes.
2. When refreshing freeze.py with changes to routes.py, the leading 'app/' must be removed from every reference to an external files (e.g., markdown content files) 

LtC Pipeline
Source: https://github.com/ben-norton/stadocgen/tree/main/app/build
Target: https://github.com/tdwg/ltc/tree/main/docs

#### Contact
Ben Norton
michaenorton.ben@gmail.com
