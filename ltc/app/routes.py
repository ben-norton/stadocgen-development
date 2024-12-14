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
@app.route('/terms')
def terms():
    header_mdfile = 'app/md/termlist-header.md'

    with open(header_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read(), extras=["tables", "fenced-code-blocks"])

    # Terms
    terms_csv = 'app/data/output/ltc-termlist.csv'
    terms_df = pd.read_csv(terms_csv, encoding='utf8')

    sssom_csv = 'app/data/output/ltc-sssom.csv'
    sssom_df = pd.read_csv(sssom_csv, encoding='utf8')

    terms_df['examples'] = terms_df['examples'].str.replace('"', '')
    terms_df['definition'] = terms_df['definition'].str.replace('"', '')
    terms_df['usage'] = terms_df['usage'].str.replace('"', '')
    terms_df['notes'] = terms_df['notes'].str.replace('"', '')

    terms_skos_df = pd.merge(
        terms_df, sssom_df[['compound_name', 'predicate_label', 'object_id', 'object_category', 'object_label', 'mapping_justification' ]],
        on=['compound_name'], how='left'
    )

    terms = terms_skos_df.sort_values(by=['class_name','term_local_name'])

    # Unique Class Names
    ltcCls = terms_df['class_name'].dropna().unique()

    # Generate Unique Terms List
    # uniqueTerms = terms_df.drop_duplicates('term_local_name').sort_values('term_local_name')
    # selectCols = ['class_name','term_ns_name','term_local_name','term_iri','term_modified','term_version_iri','label','definition','usage','notes','examples','datatype','is_required','is_repeatable','rdf_type']
    # groupCols = ['term_ns_name','term_local_name','term_iri','term_modified','term_version_iri','label','definition','usage','notes','examples','datatype','is_required','is_repeatable','rdf_type']
    # unique_terms_df = terms_df[selectCols].groupby(groupCols)['class_name'].agg([('class_name', ', '.join)]).reset_index()
    # uniqueTerms = unique_terms_df.drop_duplicates('term_local_name').sort_values('term_local_name')

    # Terms by Class
    grpdict2 = terms_df.groupby('class_name')[['term_ns_name', 'term_local_name', 'namespace', 'compound_name','term_version_iri','term_modified']].apply(
        lambda g: list(map(tuple, g.values.tolist()))).to_dict()
    termsByClass = []

    for i in grpdict2:
        termsByClass.append({
            'class': i,
            'termlist': grpdict2[i]
        })

    return render_template('term-list.html',
                           headerMarkdown=Markup(marked_text),
                           ltcCls=ltcCls,
                           terms=terms,
                           sssom=sssom_df,
                           termsByClass=termsByClass,
                           uniqueTerms=terms,
                           pageTitle='Home',
                           title=meta['title'],
                           acronym=meta['acronym'],
                           landingPage=meta['documentation-landing-page'],
                           githubRepo=meta['github-repo'],
                           slug='term-list'
    )


@app.route('/quick-reference')
def quickReference():
    header_mdfile = 'app/md/quick-reference-header.md'
    marked_text = ''
    with open(header_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read())

    # Quick Reference Main
    df = pd.read_csv('app/data/output/ltc-termlist.csv', encoding='utf8')
    df['examples'] = df['examples'].str.replace(r'"', '')
    df['definition'] = df['definition'].str.replace(r'"', '')
    df['usage'] = df['usage'].str.replace(r'"', '')
    df['notes'] = df['notes'].str.replace(r'"', '')

    # Group by Class
    grpdict = df.fillna(-1).groupby('class_name')[['namespace', 'term_local_name', 'label', 'definition',
                                                   'usage', 'notes', 'examples', 'rdf_type', 'class_name',
                                                   'is_required', 'is_repeatable', 'compound_name',
                                                   'datatype', 'term_ns_name', 'term_iri', 'term_version_iri','term_modified']].apply(
        lambda g: list(map(tuple, g.values.tolist()))).to_dict()
    grplists = []
    for i in grpdict:
        grplists.append({
            'class': i,
            'termlist': grpdict[i]
        })

    # Required values
    terms_df = df[['namespace', 'term_local_name', 'label', 'class_name',
                   'is_required', 'rdf_type', 'compound_name']].sort_values(by=['class_name'])

    required_df = terms_df.loc[(terms_df['is_required'] == True) &
                               (terms_df['rdf_type'] == 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Property')]

    required_classes_df = terms_df.loc[(terms_df['is_required'] == True) &
                           (terms_df['rdf_type'] == 'http://www.w3.org/2000/01/rdf-schema#Class')]


    return render_template('quick-reference.html',
                           headerMarkdown=Markup(marked_text),
                           grplists=grplists,
                           requiredTerms=required_df,
                           requiredClasses=required_classes_df,
                           pageTitle='Home',
                           title=meta['title'],
                           acronym=meta['acronym'],
                           landingPage=meta['documentation-landing-page'],
                           githubRepo=meta['github-repo'],
                           slug='quick-reference'
    )

@app.route('/resources')
def docResources():
    header_mdfile = 'app/md/resources-header.md'
    marked_text = ''
    with open(header_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read(), extras=["tables", "fenced-code-blocks"])

    sssom_mdfile = 'app/md/sssom-reference.md'
    marked_sssom = ''
    with open(sssom_mdfile, encoding="utf8") as f:
        marked_sssom = markdown2.markdown(f.read(), extras=["tables", "fenced-code-blocks"])

    return render_template('resources.html',
                           headerMarkdown=Markup(marked_text),
                           sssomRefMarkdown=Markup(marked_sssom),
                           pageTitle='Home',
                           title=meta['title'],
                           acronym=meta['acronym'],
                           landingPage=meta['documentation-landing-page'],
                           githubRepo=meta['github-repo'],
                           slug='resources'
    )