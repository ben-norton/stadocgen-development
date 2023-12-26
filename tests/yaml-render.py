from flask import Flask, render_template
import yaml
from jinja2 import Environment, FileSystemLoader
import markdown2
from markupsafe import Markup, escape


app = Flask(__name__)

@app.route("/")
def renderTemplate():
    ltcyaml = 'ltc-test.yml'

    with open(ltcyaml, mode="rt", encoding="utf-8") as y:
        yaml_data = yaml.safe_load(y)

    env = Environment(loader=FileSystemLoader('../tests'))
    template = env.get_template('templates/termlist-test.html')

    return render_template(template,
          params=yaml_data['doc_parameters']
    )






if (__name__ == "__main__"):
	app.run(port=5001, debug=True)
