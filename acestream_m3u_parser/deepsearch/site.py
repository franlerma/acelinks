import requests
from urllib.parse import unquote
from bs4 import BeautifulSoup

from deepsearch.acesearcher import analize_url

def site_ace_ids(site_config) :
    info = {}
    
    url = site_config['url']
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    for query in site_config['queries'] :
        buttons = soup.find_all(
            query['query']['tag'], 
            class_  = query['query'].get('class_', None),
        )
        
        for button in buttons :
            url = button.get("href")
            label = unquote(button.get("aria-label"))
            if not url.startswith('http') and not url.startswith("acestream://") :
                continue
            
            info[f"{label}"]  = analize_url(url)
            
    return info