import requests
import json
from fake_useragent import UserAgent

ua = UserAgent()


def get_search_result(req):
    req = req.split(' ')
    string = ''
    for i in req:
        string += i + '-'
    req = string[:-1]

    print(f'https://www.shutterstock.com/en/search/{req}?image_type=photo&safe=off')

    url = f'https://www.shutterstock.com/_next/data/af90a90eda6/en/_shutterstock/search/{req}.json?image_type=photo&safe=off&term={req}'
    print(url)
    headers = {"User-Agent": ua.random}
    r = requests.get(url, headers=headers)

    data = r.json()["pageProps"]["assets"]
    print(len(data), '- images on a page')
    with open(f'{req}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)

    all_items = []
    for i in data:
        # print(i["description"])
        # print(i["displays"]["1500W"]["src"])
        all_items.append('https://www.shutterstock.com/en' + i["link"])
    # print(all_items)
    return all_items


# get_search_result(req)

