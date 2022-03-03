import yaml
from yaml.loader import SafeLoader


with open('config.yml') as f:
    data = yaml.load(f, Loader=SafeLoader)
