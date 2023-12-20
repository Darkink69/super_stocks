import requests
import json
from fake_useragent import UserAgent

ua = UserAgent()


# url = 'https://www.shutterstock.com/en/g/swillklitch/sets/322381294?rid=699280'
# url = 'https://www.shutterstock.com/en'


def get_lightbox_result(url):
    headers = {"User-Agent": ua.random}
    r = requests.get(url, headers=headers)
    page = r.text

    data = page[page.find('<script id="__NEXT_DATA__" type="application/json">') + 51:page.find('</script></body></html>')]
    data = json.loads(data)["props"]['pageProps']

    with open(f'{data["assets"]["title"]}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    print(data["assets"]["totalItemCount"], '- images on a page')

    all_items = []
    for item in data["assets"]["items"]:
        # print(item["mediaItem"]["description"])
        all_items.append('https://www.shutterstock.com/en' + item["mediaItem"]["link"])

    # print(all_items)
    return all_items


# get_lightbox_result(url)

def get_popular_result(url):
    headers = {"User-Agent": ua.random}
    r = requests.get(url, headers=headers)
    page = r.text

    data = page[page.find('<script id="__NEXT_DATA__" type="application/json">') + 51:page.find('</script></body></html>')]
    data = json.loads(data)["props"]['pageProps']['cmsModules'][2]

    # print(data['items'][0]['content']['items'])
    all_trands = []
    for i in data["tabTableInlineContentData"]["fields"]["items"]:
        # print(i)
        all_trands.append(i['label'])

    # print(all_trands)
    return all_trands

    # print(dict.keys(data['items'][0]))




# get_popular_result(url)

