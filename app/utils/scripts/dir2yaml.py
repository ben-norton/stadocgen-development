import os
import sys
import yaml

# https://gist.githubusercontent.com/blaketmiller/ee85ec1b5ddf038aa923/raw/d5ad304043e63464fc7e949dc193d67cf86cd2c7/dir2yaml.py
# https://btmiller.com/2015/03/17/represent-file-structure-as-yaml-with-python.html

# python dir2yaml.py /path/to/directory
def dir_to_dict(path):

    directory = {}

    for dirname, dirnames, filenames in os.walk(path):
        dn = os.path.basename(dirname)
        directory[dn] = []

        if dirnames:
            for d in dirnames:
                directory[dn].append(dir_to_dict(path=os.path.join(path, d)))

            for f in filenames:
                directory[dn].append(f)
        else:
            directory[dn] = filenames

        return directory

if len(sys.argv) == 1:
    p = os.getcwd()
elif len(sys.argv) == 2:
    p = os.path.abspath(sys.argv[1])
else:
    sys.stderr.write("Unexpected argument {}\n".format(sys.argv[2:]))

try:
    with open("{}.yaml".format(os.path.basename(p)), "w") as f:
        try:
            yaml.dump(dir_to_dict(path=p), f, default_flow_style=False)
            print("Dictionary written to {}.yaml".format(os.path.basename(p)))
        except Exception as e:
            print(e)
except Exception as e:
    print(e)
