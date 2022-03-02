import requests


def post(post_text):
    url = "https://api.vk.com/method/wall.post"

    payload = f'owner_id=-210983267&friends_only=0&from_group=0&message={post_text}&publish_date=1677761844&signed=0&mark_as_ads=0&close_comments=0&mute_notifications=0&access_token=f731ac8724793016d8e04ae80823babaa2b9e8d4915c921deab5f0b190b48b0a193ec6ab0a1eb200c816b&v=5.131'
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
    requests.request("POST", url, headers=headers, params=payload)


def post_photo(post_text, photo_id):
    url = "https://api.vk.com/method/wall.post"

    payload = f'owner_id=-210983267&friends_only=0&from_group=0&message={post_text}&publish_date=1677761844&attachments={photo_id}&signed=0&mark_as_ads=0&close_comments=0&mute_notifications=0&access_token=f731ac8724793016d8e04ae80823babaa2b9e8d4915c921deab5f0b190b48b0a193ec6ab0a1eb200c816b&v=5.131'
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

    requests.request("POST", url, headers=headers, params=payload)
