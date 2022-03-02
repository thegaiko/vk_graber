from cgitb import reset
import requests
import time
from threading import *
from posting import post, post_photo
from send import post_check


names = ['pppppp_pppp_p', 'nnrv0', 'public69767901',
         'thankunext17', 'bonjourlasolitude', 'blooossom']
offsets = [1, 1, 1, 1, 1, 1]
counts = [2, 2, 2, 2, 2, 2]


def post_send(name, offset, count):
    id = post_check(name, offset, count)[0]
    post_text = post_check(name, offset, count)[1]

    old_id = id
    while True:
        post_check(name, offset, count)
        if old_id < id:
            if len(post_check(name, offset, count)) == 3:
                photo_id = post_check(name, offset, count)[2]
                post_photo(post_text, photo_id)
            else:
                post(post_text)


t = []

for i in range(len(names)):
    t.append(Thread(target=post_send, args=(names[i], offsets[i], counts[i],)))
    t[i].start()
