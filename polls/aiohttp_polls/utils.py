import yaml
import aiopg.sa

def load_config(fname):
    with open(fname, 'rt') as f:
        data = yaml.load(f)
    return data
