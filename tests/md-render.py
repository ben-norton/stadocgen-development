from flask import Flask, render_template
import yaml
from jinja2 import Environment, FileSystemLoader, PackageLoader
import markdown2
from flask import Flask, render_template
import yaml

# Testing conversion of Markdown file to Jinja to populate dynamically with yaml variables

app = Flask(__name__)

ltcyaml = 'ltc-test.yml'

@app.route("/")
def renderTemplate():

    # Load YAML
    with open(ltcyaml, mode="rt", encoding="utf-8") as y:
        yaml_data = yaml.safe_load(y)
        params = yaml_data['doc_parameters']

    # Load Template
    env = Environment(loader=FileSystemLoader('../tests'))
    template = env.get_template('templates/termlist-test.html')

    # Render Template
    return render_template(template,
       params=params
       )


if (__name__ == "__main__"):
	app.run(port=5001, debug=True)
