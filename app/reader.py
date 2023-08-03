import yaml
from yaml import SafeLoader, FullLoader
import pprint

with open("../config.yml", "r") as first_file:
    data = yaml.safe_load(first_file)
    print(type(data))
    pprint.pprint(data)
