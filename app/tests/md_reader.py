from flask import Flask, render_template
from markupsafe import Markup, escape
import markdown2
import os
import tests

template_dir = os.path.abspath('test_templates')
app = Flask(__name__, template_folder=template_dir)

mdfile = '../content/md/ltc/home_content.md'

@app.route("/")
def read_file():
    marked_text = ''
    with open(mdfile) as f:
        marked_text = markdown2.markdown(f.read())
    return render_template('md_render.html', my_html=Markup(marked_text))


if __name__ == "__main__":
    app.run(debug=True)