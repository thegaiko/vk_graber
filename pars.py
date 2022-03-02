from cgitb import reset
import requests
import time
from threading import *
from posting import post, post_photo
from send import post_check


names = ['pppppp_pppp_p', 'nnrv0', 'public69767901',
         'thankunext17', 'purplecherrybot', 'blooossom']
offsets = [1, 1, 1, 1, 1, 0]
counts = [2, 2, 2, 2, 2, 1]
timers = [1, 2, 3, 4, 5, 6]


def post_send(name, offset, count, timer):
    old_id = post_check(name, offset, count)[0]
    while True:
        id = post_check(name, offset, count)[0]
        if old_id < id:
            if len(post_check(name, offset, count)) == 3:
                post_text = post_check(name, offset, count)[1]
                photo_id = post_check(name, offset, count)[2]
                post_photo(post_text, photo_id)
            else:
                post_text = post_check(name, offset, count)[1]
                post(post_text)
            old_id = id
        time.sleep(timer)


t = []

for i in range(len(names)):
    t.append(Thread(target=post_send, args=(
        names[i], offsets[i], counts[i], timers[i])))
    t[i].start()
