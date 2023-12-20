import time
import random
import shutter_search
import shutter_lightbox
import shutter_current_img
# import get_description


# url = 'https://www.shutterstock.com/en'
# all_trands = shutter_lightbox.get_popular_result(url)  # get all trands with main page
# print(all_trands)


# get all search results pages
# safe = 'off'
# color = 'F1F129'
# age = '20s'
# gender = 'female'
# people_number = '2'
# ethnicity = 'black'
# mreleased = 'true'

req = 'christmas'


all_urls = shutter_search.get_search_result(req)
print(all_urls)

# make description from api AI
# img = '123.jpg'
# desc = get_description.get_from_blip2_api(img)
# print(desc)


# url = 'https://www.shutterstock.com/en/g/swillklitch/sets/322381294?rid=699280'
# all_urls = shutter_lightbox.get_lightbox_result(url)
# print(all_urls)



# all_urls = ['https://www.shutterstock.com/ru/image-illustration/abstract-background-geometric-shapes-similar-green-306765689']
#
# for url in all_urls:
#     asset = shutter_current_img.get_info_img(url)
#     print(asset)
#
#     time.sleep(random.randint(0, 3))


# with open(f'{data["id"]}.json', 'w', encoding='utf-8') as f:
    #     json.dump(asset, f, indent=4)


