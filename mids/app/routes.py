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
                           landingPage=meta['links']['landing_page'],
                           githubRepo=meta['links']['github_repository'],
                           slug='home'
                           )

@app.route('/information-elements')
def information_elements():
    home_mdfile = 'app/md/information-elements-header.md'
    with open(home_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read())

    information_elements_csv = 'app/data/output/mids-master-list.csv'
    information_elements_df = pd.read_csv(information_elements_csv, encoding='utf8')

    mappings_csv = 'app/data/output/mids-mappings.csv'
    mappings_df = pd.read_csv(mappings_csv, encoding='utf8')


    information_elements_mapped_df = pd.merge(information_elements_df,
        mappings_df[['term_local_name','sssom_object_category','sssom_object_id','object_source_version','sssom_subject_category']],
        on=['term_local_name'], how='left'
    )
    print(information_elements_mapped_df)

    terms = information_elements_mapped_df.sort_values(by=['term_local_name'])

    levels_csv = 'app/data/output/mids-levels.csv'
    levels_df = pd.read_csv(levels_csv, encoding='utf8')

    informationElements = information_elements_mapped_df.sort_values(by=['class_name', 'term_local_name'])
    levels = levels_df.sort_values(by=['term_local_name'])

    grpdict2 = information_elements_df.groupby('class_name')[
        ['term_ns_name', 'term_local_name', 'namespace', 'compound_name', 'term_version_iri', 'term_modified']].apply(
        lambda g: list(map(tuple, g.values.tolist()))).to_dict()
    informationElementsByLevel = []

    for i in grpdict2:
        informationElementsByLevel.append({
            'class': i,
            'informationElementList': grpdict2[i]
        })

    return render_template('information-elements.html',
                           home_markdown=Markup(marked_text),
                           pageTitle='Information Elements',
                           title=meta['title'],
                           acronym=meta['acronym'],
                           landingPage=meta['links']['landing_page'],
                           githubRepo=meta['links']['github_repository'],
                           slug='information-elements',
                           levels=levels,
                           informationElements=informationElements,
                           mappings=mappings_df,
                           informationElementsByLevel=informationElementsByLevel
                           )

@app.route('/mappings')
def mappings():
    home_mdfile = 'app/md/mappings-header.md'
    with open(home_mdfile, encoding="utf8") as f:
        marked_text = markdown2.markdown(f.read())

    master_list_csv = 'app/data/output/mids-master-list.csv'
    master_list_df = pd.read_csv(master_list_csv, encoding='utf8')

    mappings_csv = 'app/data/output/mids-mappings.csv'
    mappings_df = pd.read_csv(mappings_csv, encoding='utf8')

    return render_template('mappings.html',
                           home_markdown=Markup(marked_text),
                           pageTitle='MIDS Mappings',
                           title=meta['title'],
                           acronym=meta['acronym'],
                           landingPage=meta['links']['landing_page'],
                           githubRepo=meta['links']['github_repository'],
                           slug='information-elements',
                           mappings=mappings_df,
                           )