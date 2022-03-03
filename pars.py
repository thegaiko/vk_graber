import requests
import time
from threading import *
from posting import post, post_photo
from send import post_check


names = ['pppppp_pppp_p', 'nnrv0',
         'thankunext17', '01caramelka', 'g_laurent']
offsets = [1, 1, 1, 0, 1]
counts = [2, 2, 2, 1, 2]
old_id = []


for i in range(len(names)):
    old_id.append(str(post_check(names[i], offsets[i], counts[i])[0]))
print(old_id)

while True:
    for i in range(len(names)):
        result = post_check(names[i], offsets[i], counts[i])
        id = str(result[0])
        if old_id[i] != id:
            if len(result) == 3:
                post_text = result[1]
                print(post_text)
                photo_id = result[2]
                post_photo(post_text, photo_id)
                old_id[i] = id
            else:
                post_text = result[1]
                print(post_text)
                post(post_text)
                old_id[i] = id
    print(old_id)
