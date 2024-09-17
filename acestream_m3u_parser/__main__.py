import json
import yaml

from deepsearch.site import site_ace_ids

with open('config.yaml', 'r') as config_file: 
    config = yaml.safe_load(config_file)

links = {}
for site_config in config['sites'] :
    try :
        links.update(site_ace_ids(site_config=site_config))
    except Exception as e:
        print("".format(e))
    
print(json.dumps(links, sort_keys=True, indent=4))
                
               

