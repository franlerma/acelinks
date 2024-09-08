import requests
from urllib import parse
from requests.exceptions import InvalidSchema
from bs4 import BeautifulSoup

def search_ace_url_in_google_query(url) :
    urlOK = parse.parse_qs(parse.urlsplit(url).query)['q'][0]
    try :
        response = requests.head(urlOK, allow_redirects=True)
        return urlOK, None
    except InvalidSchema as e :
        message = e.args[0].replace("'", "") if len(e.args) > 0 else None
        if message and "acestream://" in message :
            ace_id = message.split("acestream://")[1]
            return urlOK, ace_id
        else : 
            return urlOK, None
    except Exception as e :
        print(e)
        return urlOK, None

URL = "https://sites.google.com/view/elplandeportes/inicio"
URL = "https://elplan94.github.io/hook/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
buttons = soup.find_all("a", class_="FKF6mc", href=True)

for button in buttons :
    url = button.get("href")
    if not url.startswith("http") :
        continue
    res = search_ace_url_in_google_query(url)
    if res[1] :
        print(res)
