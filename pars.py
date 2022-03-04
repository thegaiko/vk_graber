import requests
import time
from threading import *
from posting import post, post_photo
from send import post_check

names = ['thynk', 'whrmedia', 'yourwoorlld', 'theoh', 'kim_kardashian', 'pppppp_pppp_p', 'nnrv0',
         'thankunext17', '01caramelka', 'g_laurent']
offsets = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
counts = [1, 1, 2, 2, 2, 2, 2, 2, 2, 2]
old_id = []


for i in range(len(names)):
    old_id.append(str(post_check(names[i], offsets[i], counts[i])[0]))

while True:
    for i in range(len(names)):
        result = post_check(names[i], offsets[i], counts[i])
        id = str(result[0])
        if old_id[i] < id:
            if len(result) == 5:
                post_text = result[1]
                photo_id = result[2]
                post_owner_id = result[3]
                copyright_post_id = result[4]
                post_copyright = 'https://vk.com/' + \
                    names[i] + '?w=wall' + post_owner_id + \
                    '_' + copyright_post_id
                post_photo(post_text, photo_id, post_copyright)
                print(post_copyright)
                old_id[i] = id
            else:
                post_text = result[1]
                post_owner_id = result[2]
                copyright_post_id = result[3]
                post_copyright = 'https://vk.com/' + \
                    names[i] + '?w=wall' + post_owner_id + \
                    '_' + copyright_post_id
                post(post_text, post_copyright)
                old_id[i] = id
