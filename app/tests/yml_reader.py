import yaml
import pprint

# Root app config
with open("../../config.yml", "r") as app_config:
    coredata = yaml.safe_load(app_config)
    print(type(coredata))
    pprint.pprint(coredata)

# LtC config
with open("../ltc.yml", "r") as ltc_config:
    ltcdata = yaml.safe_load(ltc_config)
    print(type(ltcdata))
    pprint.pprint(ltcdata)
