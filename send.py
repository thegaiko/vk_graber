import requests
import time
from pprint import pprint

def post_check(name, offset, count):
    url = "https://api.vk.com/method/wall.get"
    payload = f'domain={name}&offset={offset}&count={count}&extended=false&access_token=efc31359efc31359efc3135901efbfa9c4eefc3efc313598d48465ad25a585974cbdc96&v=5.131'
    response = requests.request("POST", url, params=payload)
    post_id = response.json()['response']['items'][0]['date']
    text = response.json()['response']['items'][0]['text']
    post_owner_id = post_owner_id = str(response.json()[
        'response']['items'][0]['owner_id'])
    print(post_owner_id)
    copyright_post_id = str(response.json()[
        'response']['items'][0]['id'])
    time = response.json()['response']['items'][0]['date']
    try:
        response.json()[
            'response']['items'][0]['attachments'][0]['photo']['sizes'][0]['url']
    except KeyError:
        post_text = text
        return(post_id, post_text, post_owner_id, copyright_post_id, time)
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
        return(post_id, post_text, photo_id, post_owner_id, copyright_post_id, time)
    