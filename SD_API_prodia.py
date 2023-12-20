import requests
import time
import random
import json
from fake_useragent import UserAgent
from gradio_client import Client

ua = UserAgent()

prompt = 'woman walk on a beach, beautiful, female, ultrarealistic, soft lighting, 8k'


def gen_api_prodia_512(prompt):
    prompt = prompt.split(' ')
    string = ''
    for i in prompt:
        string += i + '+'
    prompt = string[:-1]

    # model = 'Realistic_Vision_V5.0.safetensors+%5B614d1063%5D'
    model = 'absolutereality_v181.safetensors+%5B3d9d4d2b%5D'

    negative_prompt = '3d+cartoon+anime+bad+anatomy+ugly'
    # negative_prompt = ''
    sampler = 'DPM%2B%2B+2M+Karras'
    seed = '-1'
    # seed = random.randint(0, 3851315814)
    # 2147483647
    # print("seed -", seed)


    url = f'https://api.prodia.com/generate?new=true&prompt={prompt}&upscale=true&model={model}&negative_prompt={negative_prompt}&steps=25&cfg=7&seed={seed}&sampler={sampler}&aspect_ratio=square'
    print(url)

    headers = {"User-Agent": ua.random}
    r = requests.get(url, headers=headers)
    # print(r.json())

    img = f'https://images.prodia.xyz/{r.json()["job"]}.png'
    print(img)


gen_api_prodia_512(prompt)


# time.sleep(10)
# p = requests.get(img)
# out = open(f"{r.json()['job']}.png", "wb")
# out.write(p.content)
# out.close()



# url = "https://api.prodia.com/v1/sd/generate"
# payload = {
#     "model": "v1-5-pruned-emaonly.safetensors [d7049739]",
#     "prompt": "nude woman on a beach take sunbathe",
#     "negative_prompt": "badly drawn",
#     "steps": 25,
#     "cfg_scale": 7,
#     "seed": -1,
#     "upscale": False,
#     "sampler": "DPM++ 2M Karras",
#     "width": 1024,
#     "height": 1024
# }
# headers = {
#     "accept": "application/json",
#     "content-type": "application/json",
#     "X-Prodia-Key": "API_KEY"
# }
#
# response = requests.post(url, json=payload, headers=headers)
#
# print(response.text)

#
# url = "https://api.prodia.com/v1/sd/models"
# headers = {"accept": "application/json"}
# response = requests.get(url, headers=headers)
# print(response.text)

# https://prodia-fast-stable-diffusion.hf.space/--replicas/tnhzn/info


# url = "https://prodia-fast-stable-diffusion.hf.space/queue/join?fn_index=0&session_hash=t4k6fno8ikj"

# https://prodia-fast-stable-diffusion.hf.space/queue/join?fn_index=0&session_hash=a3o6ethult
# {"msg": "estimation", "rank": 0, "queue_size": 1, "avg_event_process_time": 18.25924482686856, "avg_event_concurrent_process_time": 0.07132517510495531, "rank_eta": 18.25924482686856, "queue_eta": 0.0}
# {"msg": "send_data", "event_id": "cf1579a7fe724480ab9b897c197e5fd7"}
# {"msg": "process_starts"}
# {"msg": "process_completed", "output": {"data": [{"path": "/tmp/gradio/69ebb509a68e87ffce498971057eec41f3e2127f/1c9b93bc-eb5b-40d0-84c5-190101f278c5.png", "url": null, "size": null, "orig_name": null, "mime_type": null}], "is_generating": false, "duration": 13.091008186340332, "average_duration": 16.329305578698264}, "success": true}
# {"data":["worker, beautiful, female, ultrarealistic, soft lighting, 8k","3d, cartoon, anime, (deformed eyes, nose, ears, nose), bad anatomy, ugly","absolutereality_v181.safetensors [3d9d4d2b]",25,"DPM++ 2M Karras",7,1024,1024,-1],"event_data":null,"fn_index":0,"trigger_id":15,"session_hash":"a3o6ethult","event_id":"cf1579a7fe724480ab9b897c197e5fd7"}
# https://prodia-fast-stable-diffusion.hf.space/--replicas/qm94v/file=/tmp/gradio/69ebb509a68e87ffce498971057eec41f3e2127f/1c9b93bc-eb5b-40d0-84c5-190101f278c5.png

#
# data = {"data":["retro car and woman near, ultrarealistic, soft lighting, 8k","3d, cartoon, anime, (deformed eyes, nose, ears, nose), bad anatomy, ugly","absolutereality_v181.safetensors [3d9d4d2b]",25,"DPM++ 2M Karras",7,1024,1024,-1],"event_data": 'null',"fn_index":0,"trigger_id":15,"session_hash":"t4k6fno9ikj","event_id":"fe1cefae26194dfba09cad96ca6e63fb"}
#
#
# headers = {"User-Agent": ua.random}
# # r = requests.get(url, headers=headers)
# # print(r)
#
# s = requests.Session()
#
# s.get(url)
#
# r = s.get(url, json=data, headers=headers, stream=True)
#
# print(r.text)


# response = requests.post(url, data=json.dumps(data)).json()
# answer = response.get("replies")
# print(answer)

# fetch("https://prodia-fast-stable-diffusion.hf.space/queue/data", {
#   "headers": {
#     "accept": "*/*",
#     "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,it;q=0.6",
#     "content-type": "application/json",
#     "sec-ch-ua": "\"Google Chrome\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"",
#     "sec-ch-ua-mobile": "?0",
#     "sec-ch-ua-platform": "\"Windows\"",
#     "sec-fetch-dest": "empty",
#     "sec-fetch-mode": "cors",
#     "sec-fetch-site": "same-origin"
#   },
#   "referrer": "https://prodia-fast-stable-diffusion.hf.space/",
#   "referrerPolicy": "strict-origin-when-cross-origin",
#   "body": "{\"data\":[\"retro car, ultrarealistic, soft lighting, 8k\",\"3d, cartoon, anime, (deformed eyes, nose, ears, nose), bad anatomy, ugly\",\"absolutereality_v181.safetensors [3d9d4d2b]\",25,\"DPM++ 2M Karras\",7,512,512,-1],\"event_data\":null,\"fn_index\":0,\"trigger_id\":15,\"session_hash\":\"t4k6fno9ikj\",\"event_id\":\"948cb3e86ccb4c27ac0b4613b93ebe18\"}",
#   "method": "POST",
#   "mode": "cors",
#   "credentials": "include"
# });


# https://replicate.delivery/pbxt/JvpO0tsJDZuM6DPRKzEj6cB4WwliA6zSCJBqGmCfur6pDkGI/izu_strip15375.png