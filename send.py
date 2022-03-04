import requests
import time


def post_check(name, offset, count):
    url = "https://api.vk.com/method/wall.get"
    payload = f'domain={name}&offset={offset}&count={count}&extended=false&access_token=0b97751f0b97751f0b97751f920bec1a5500b970b97751f698deca772c621f6c27724c3&v=5.131'
    headers = {
        'authority': 'api.vk.com',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.109 Safari/537.36',
        'sec-ch-ua-platform': '"macOS"',
        'content-type': 'application/x-www-form-urlencoded',
        'accept': '*/*',
        'origin': 'https://dev.vk.com',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://dev.vk.com/',
        'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7'
    }

    response = requests.request("POST", url, headers=headers, params=payload)
    post_id = response.json()['response']['items'][0]['date']
    text = response.json()['response']['items'][0]['text']
    post_owner_id = post_owner_id = str(response.json()[
        'response']['items'][0]['owner_id'])
    copyright_post_id = str(response.json()[
        'response']['items'][0]['id'])
    try:
        response.json()[
            'response']['items'][0]['attachments'][0]['photo']['sizes'][0]['url']
    except KeyError:
        post_text = text
        return(post_id, post_text, post_owner_id, copyright_post_id)
    else:
        post_text = text
        photo_count = len(
            response.json()['response']['items'][0]['attachments'])
        photo_id = ''
        for i in range(photo_count):
            owner_id = str(response.json()[
                'response']['items'][0]['attachments'][i]['photo']['owner_id'])
            id = str(response.json()['response']['items']
                     [0]['attachments'][i]['photo']['id'])
            photo_id += 'photo' + owner_id + '_' + id + ','
        return(post_id, post_text, photo_id, post_owner_id, copyright_post_id)
