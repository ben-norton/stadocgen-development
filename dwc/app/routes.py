from app import app
from flask import render_template
from markupsafe import Markup
import markdown2
import pandas as pd
import yaml

with open('app/meta.yml') as metadata:
    meta = yaml.safe_load(metadata)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html',
                           pageTitle='404 Error'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html',
                           pageTitle='500 Unknown Error'), 500


'''
@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}
'''

# Homepage with content stored in markdown file
@app.route('/')
def home():
    home_mdfile = 'app/md/home-content.md'
    with open(home_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read())
    return render_template('home.html',
                           home_markdown=Markup(marked_text),
                           pageTitle='Home',
                           title=meta['title'],
                           acronym=meta['acronym'],
                           landingPage=meta['documentation-landing-page'],
                           githubRepo=meta['github-repo'],
                           slug='home'
                           )
