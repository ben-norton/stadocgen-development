from flask import render_template, request, jsonify
from app import app
from markupsafe import Markup
import markdown2
import pandas as pd
from flask_flatpages import pygmented_markdown, pygments_style_defs
@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}

# Homepage with content stored in markdown file
@app.route('/')
def home():
    home_mdfile = 'app/content/md/ltc/home_content.md'
    marked_text = ''
    with open(home_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read())
    return render_template('home.html',
                           homemd=Markup(marked_text),
                           title='Home',
                           slug='home')



@app.route('/terms')
def terms():
    header_mdfile = 'app/content/md/ltc/terms_list_header.md'
    marked_text = ''
    with open(header_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read(), extras=["tables", "fenced-code-blocks"])

    # Terms
    terms_csv = 'app/data/ltc/ltc_docs/ltc-terms-list.csv'
    terms_df = pd.read_csv(terms_csv, encoding='utf8')
    terms = terms_df.sort_values(by=['class_name'])
    terms['examples'] = terms['examples'].str.replace(r'"', '')
    terms['definition'] = terms['definition'].str.replace(r'"', '')

    sssomcsv = 'app/data/ltc/ltc_docs/ltc_sssom.csv'
    sssom = pd.read_csv(sssomcsv, encoding='utf8')


    # Unique Class Names
    ltcCls = terms["class_name"].dropna().unique()

    # Terms by Class
    grpdict2 = terms_df.groupby('class_name')[['term_ns_name', 'term_local_name']].apply(
        lambda g: list(map(tuple, g.values.tolist()))).to_dict()
    termsByClass = []
    for i in grpdict2:
        termsByClass.append({
            'class': i,
            'terms': grpdict2[i]
        })

    return render_template('terms.html',
                           headerMarkdown=Markup(marked_text),
                           ltcCls=ltcCls,
                           terms=terms,
                           termsByClass=termsByClass,
                           sssom=sssom,
                           title='Terms List',
                           slug='terms-list'
    )

@app.route('/quick-reference')
def quickReference():
    header_mdfile = 'app/content/md/ltc/quick_reference_header.md'
    marked_text = ''
    with open(header_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read())

    # Quick Reference Main
    df = pd.read_csv('app/data/ltc/ltc_docs/ltc-terms-list.csv', encoding='utf8')
    df['examples'] = df['examples'].str.replace(r'"', '')
    df['definition'] = df['definition'].str.replace(r'"', '')

    # Group by Class
    grpdict = df.fillna(-1).groupby('class_name')[['namespace', 'term_local_name', 'label', 'definition',
                                                   'usage', 'notes', 'examples', 'rdf_type', 'class_name',
                                                   'is_required', 'is_repeatable', 'compound_name',
                                                   'datatype', 'term_ns_name']].apply(
        lambda g: list(map(tuple, g.values.tolist()))).to_dict()
    grplists = []
    for i in grpdict:
        grplists.append({
            'class': i,
            'terms': grpdict[i]
        })

    return render_template('quick-reference.html',
                           headerMarkdown=Markup(marked_text),
                           grplists=grplists,
                           title='Quick Reference',
                           slug='quick-reference'
    )


