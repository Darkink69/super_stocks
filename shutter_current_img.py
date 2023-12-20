import requests
import json
from fake_useragent import UserAgent

ua = UserAgent()

# url = 'https://www.shutterstock.com/en/image-vector/black-hole-scheme-gravity-grid-scientific-1927860602'


def get_info_img(url):
    headers = {"User-Agent": ua.random}
    r = requests.get(url, headers=headers)
    page = r.text

    data = page[page.find('<script id="__NEXT_DATA__" type="application/json">') + 51:page.find('</script></body></html>')]
    data = json.loads(data)["props"]['pageProps']["asset"]

    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    asset = {
        "id": data["id"],
        "type": data["type"],
        "imageType": data["imageType"],
        "description": data["description"],
        "keywords": data["keywords"],
        "uploadedDate": data["uploadedDate"],
        "src": data["src"],
        "1500W_src": data["displays"]["1500W"]["src"],
        "link": 'https://www.shutterstock.com/en' + data["link"],
        "imageScores": data["imageScores"],
    }
    # print(asset)
    return asset



