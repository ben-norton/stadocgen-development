from app import app
from flask import Flask, render_template
from flask_frozen import Freezer
from markupsafe import Markup
import sys
import markdown2
import pandas as pd
from flask_flatpages import FlatPages, pygmented_markdown, pygments_style_defs

freezer = Freezer(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('tango'), 200, {'Content-Type': 'text/css'}

# Homepage with content stored in markdown file
@app.route('/')
def home():
    home_mdfile = 'md/ltc/home-content.md'
    marked_text = ''
    with open(home_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read())
    return render_template('home.html',
                           homemd=Markup(marked_text),
                           title='Home',
                           slug='home')


@app.route('/resources/')
def ltcResources():
    header_mdfile = 'md/ltc/resources-header.md'
    marked_text = ''
    with open(header_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read(), extras=["tables", "fenced-code-blocks"])

    sssom_mdfile = 'md/ltc/sssom-reference.md'
    marked_sssom = ''
    with open(sssom_mdfile, encoding="utf8") as f:
        marked_sssom = markdown2.markdown(f.read(), extras=["tables", "fenced-code-blocks"])

    return render_template('resources.html',
                           headerMarkdown=Markup(marked_text),
                           sssomRefMarkdown=Markup(marked_sssom),
                           pageTitle='Latimer Core Resources',
                           title='Resources',
                           slug='ltc-resources'
    )


@app.route('/terms/')
def terms():
    header_mdfile = 'md/ltc/terms-list-header.md'
    marked_text = ''
    with open(header_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read(), extras=["tables", "fenced-code-blocks"])

    # Terms
    terms_csv = 'data/ltc/ltc-docs/ltc-terms-list.csv'
    terms_df = pd.read_csv(terms_csv, encoding='utf8')

    skoscsv = 'data/ltc/ltc-docs/ltc-skos.csv'
    skos_df = pd.read_csv(skoscsv, encoding='utf8')

    sssomcsv = 'data/ltc/ltc-docs/ltc-sssom.csv'
    sssom_df = pd.read_csv(sssomcsv, encoding='utf8')

    terms_skos_df1 = pd.merge(
        terms_df, skos_df[['term_uri', 'skos_mappingRelation', 'related_termName']], on=['term_uri'], how='left'
    )
    terms_skos_df = pd.merge(
        terms_skos_df1, sssom_df[['compound_name', 'predicate_label', 'object_id', 'object_category', 'object_label', 'mapping_justification' ]],
        on=['compound_name'], how='left'
    )

    terms = terms_skos_df.sort_values(by=['class_name'])
    terms['examples'] = terms['examples'].str.replace(r'"', '')
    terms['definition'] = terms['definition'].str.replace(r'"', '')
    terms['usage'] = terms['usage'].str.replace(r'"', '')
    terms['notes'] = terms['notes'].str.replace(r'"', '')

    # Unique Class Names
    ltcCls = terms_df["class_name"].dropna().unique()

    # Terms by Class
    grpdict2 = terms_df.groupby('class_name')[['term_ns_name', 'term_local_name', 'namespace', 'compound_name']].apply(
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
                           pageTitle='Latimer Core Terms',
                           title='Terms List',
                           slug='terms-list'
    )

@app.route('/quick-reference/')
def quickReference():
    header_mdfile = 'md/ltc/quick-reference-header.md'
    marked_text = ''
    with open(header_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read())

    # Quick Reference Main
    df = pd.read_csv('data/ltc/ltc-docs/ltc-terms-list.csv', encoding='utf8')
    df['examples'] = df['examples'].str.replace(r'"', '')
    df['definition'] = df['definition'].str.replace(r'"', '')
    df['usage'] = df['usage'].str.replace(r'"', '')
    df['notes'] = df['notes'].str.replace(r'"', '')

    # Group by Class
    grpdict = df.fillna(-1).groupby('class_name')[['namespace', 'term_local_name', 'label', 'definition',
                                                   'usage', 'notes','examples', 'rdf_type', 'class_name',
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
                           pageTitle='Latimer Core Quick Reference Guide',
                           title='Quick Reference',
                           slug='quick-reference'
    )


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        freezer.run(debug=True,port=8000)