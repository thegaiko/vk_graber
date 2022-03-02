import requests

url = "https://api.vk.com/method/wall.post"
text = 'https://sun9-57.userapi.com/sun9-36/impg/od23LQH5UFy2zFzLRh0stbYyGNeXifXhZzf7LQ/hrKtEl4zW5Y.jpg?size=1280x800&quality=96&sign=07a4d077626f9dff23d1dc588abe7394&c_uniq_tag=WKKSZlb7M5mM0whCaT3HvJS09zbsG31qSI9HAnQZSOA&type=album'
payload = f'owner_id=-209886591&friends_only=0&from_group=0&message={text}&signed=0&mark_as_ads=0&close_comments=0&mute_notifications=0&access_token=f731ac8724793016d8e04ae80823babaa2b9e8d4915c921deab5f0b190b48b0a193ec6ab0a1eb200c816b&v=5.131'
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

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
