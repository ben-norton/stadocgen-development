# Specifications
Stadocgen generates documentation pages based on a standardized set of CSV Markdown files. 
In order for users to generate content, they must follow a set of specification required for operation of the application. CSV and Markdown files must adhere to a naming convention and organized in a specific manner.
These conventions and procedures are provided below for both CSV vocabulary and Markdown content files.

### Website Structure and Markdown
The standards documentation websites are comprised of a specific set of html pages, two are required. Each page is assigned a url slug for programmatic use.

| Page Title      | [slug]           | Description                        | Example                    | Is Required |
|-----------------|------------------|------------------------------------|----------------------------|-------------|
| Home            | [home]           | The documentation website homepage | https://tdwg.github.io/ltc | Yes         |
| Terms List      | [terms-list]     | Normative terms list               |                            | Yes         |
| Quick Reference | [quick-reference] | Non-normative documentation        |                            | No          |
| Resources       | [resources]      | Support documentation and diagrams |                            | No          |

The markdown files are source of webpage content, mainly at the top of each page. 
The naming convention is [page slug]-[block].md
Where page slug is the URL slug for the specific page and the block refers to the location of the content on the page.
#### Blocks
* Content - Main Body
* Header - Page Header

The app can be configured to parse additional blocks and slugs.
### Markdown Files
home-content.md
quick-reference-header.md
resources-header.md
sssom-reference.md
termlist-header.md

## CSV Files
The CSV workflow transforms the source set of CSV files (see list below) and generates a target set for publishing on the web using a set of python transformation scripts

Source CSV Folders
[source] \ltc\source\terms
[rs.tdwg] \ltc\source\rs.tdwg.org

Target CSV Folders
[docs] stadocgen\app\data\ltc\ltc-docs
[ltc-source] stadocgen\app\data\ltc\ltc-source

Copy
[rs.tdwg]\namespace.csv > [ltc-source]\ltc-namespaces.csv

Source Input Files
ltc/source/rs.tdwg.org
    namespace.csv > rename ltc-namespaces.csv
    ltc-namespaces.csv > data/ltc/ltc-docs/

