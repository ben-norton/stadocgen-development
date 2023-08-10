import os
import glob
import sys
from pathlib import Path
# Pass directory parameter

# Set root project rootdir
rd = 'D:/webserver/Apache/flask/stadocgen/app/'
ext = ('.html')
chr = "_"
result = {}

def collapse_dirs(dir):

    # get a list of elements in the target directory
    elems = os.listdir(dir)

    # iterate over each element
    for elem in elems:

        # compute the path to the element
        path = os.path.join(dir, elem)

        # is it a directory?  If so, process it...
        if os.path.isdir(path):

            # get all of the elements in the subdirectory
            subelems = os.listdir(path)

            # process each entry in this subdirectory...
            for subelem in subelems:

                # compute the full path to the element
                filepath = os.path.join(path, subelem)

                # we only want to proceed if the element is a file.  If so...
                if os.path.isfile(filepath):

                    # compute the new path for the file - I chose to separate the names with an underscore,
                    # but this line can easily be changed to use whatever separator you want (or none)
                    newpath = os.path.join(path, elem + '_' + subelem)

                    # rename the file
                    os.rename(filepath, newpath)
