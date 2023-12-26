import markdown2

# Create Jinja Template from Markdown

mdfile = 'md/tdwg/termlist-header.md'

with open(mdfile, 'r') as f:
    input = f.read()

parsed_md = markdown2.markdown(input, extras=["meta"])

with open("templates/termlist-header.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
    output_file.write(parsed_md)
