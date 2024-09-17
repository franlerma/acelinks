
import requests
from urllib import parse
from requests.exceptions import InvalidSchema

def analize_url(url) :
    if url and "acestream://" in url :
        res = [ url, url.split("acestream://")[1] ]
    if "www.google.com/url?q=" in url :        
        res = __analize_url_googlesites(url)
    else :
        res = __analize_url(url)
    return res

def __analize_url_googlesites(url) :
    urlOK = parse.parse_qs(parse.urlsplit(url).query)['q'][0]
    return __analize_url(urlOK)
    
def __analize_url(url) :
    response = {}
    response['url'] = url
    
    try :
        requests.head(url, allow_redirects=True)
    except InvalidSchema as e :
        message = e.args[0].replace("'", "") if len(e.args) > 0 else None
        if message and "acestream://" in message :
            ace_id = message.split("acestream://")[1]
            response['acestream_id'] = ace_id
    except Exception as e :
        print(e)
        
    return response