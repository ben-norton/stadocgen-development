from flask import Flask, render_template
from markupsafe import Markup, escape
import markdown2

app = Flask(__name__)

mdfile = 'md/tdwg/ac/index.md'

@app.route("/")
def read_file():
    marked_text = ''
    with open(mdfile) as f:
        marked_text = markdown2.markdown(f.read())
    return render_template('tests/md-render.html', my_html=Markup(marked_text))


if __name__ == "__main__":
    app.run(debug=True)