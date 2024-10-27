import yaml
from pprint import pprint

# add input of the file name
file_name = input("Enter the file name: ")
with open(file_name,'r') as f:
    config = yaml.safe_load(f)

pprint(config,sort_dicts=False)

