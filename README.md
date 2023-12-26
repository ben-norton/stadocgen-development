# stadocgen
Generator of Web-based Documentation for TDWG Data Standards  
Built using Python Flask, the application transforms a set of CSV files into data standards documentation pages. This application is currently under active development. The current iteration of the application is being used to generate the docs here: [https://tdwg.github.io/ltc](https://tdwg.github.io/ltc). The main application is located under stadocgen. Ltc is a legacy application that was migrated from the Latimer Core repository.

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
|   ├───archive     | Timestamped copies of csv and markdown files 
│   ├───build       | Static html files generated using Frozen Flask (https://pythonhosted.org/Frozen-Flask/)
│   ├───data        | Source data files in csv format
│   │   ├───global
│   │   ├───ltc
│   │   │   ├───ltc-docs    | Source data post-transformation scripts
│   │   │   └───ltc-source  | Original source data files
│   ├───md          | Specific content blocks in markdown format 
│   │   └───ltc     | Markdown associated with Latimer Core Documentation
│   ├───static      | Static assets (css, js, icons)
│   ├───templates   | Jinja templates
│   ├───tests       | Assorted testing scripts used to develop the application (not unit tests)
│   ├───utils       | Data transformation utilities 
_init__.py
config.py   Standard python configuration file (not currently in use)
freeze.py   Frozen flask script to generate build files
ltc.yml     YAML configuration file for the Latimer Core Standard
routes.py   Dynamic flask script
```

### Commands
* To launch dev server, for testing run *flask run* then open a browser to localhost:5000
* To build documentation webpages, change to app directory then run *python freeze.py build*

#### Contact
Ben Norton
michaenorton.ben@gmail.com
