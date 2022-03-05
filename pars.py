from threading import *
from posting import post, post_photo
from send import post_check

names = ['thynk', 'yourwoorlld', 'pppppp_pppp_p', 'nnrv0', 'thankunext17',
         '01caramelka', 'b1ackstreet1', 'club_big_boys', 'tsukuyyyomi', 'purplecherrybot']
offsets = [0, 1, 1, 0, 1, 0, 1, 0, 1, 0]
counts = [1, 2, 2, 1, 2, 1, 2, 1, 2, 1]
old_id = []
my_name = 'gpntrst'

for i in range(len(names)):
    old_id.append(str(post_check(names[i], offsets[i], counts[i])[0]))

time = 1646490600
while True:
    for i in range(len(names)):
        result = post_check(names[i], offsets[i], counts[i])
        id = str(result[0])
        if old_id[i] < id:
            if len(result) == 6:
                post_text = result[1]
                photo_id = result[2]
                post_owner_id = result[3]
                copyright_post_id = result[4]
                post_copyright = 'https://vk.com/' + \
                    names[i] + '?w=wall' + post_owner_id + \
                    '_' + copyright_post_id
                time += 3600
                post_photo(post_text, photo_id, post_copyright, time)
                old_id[i] = id
            else:
                post_text = result[1]
                post_owner_id = result[2]
                copyright_post_id = result[3]
                post_copyright = 'https://vk.com/' + \
                    names[i] + '?w=wall' + post_owner_id + \
                    '_' + copyright_post_id
                time += 3600
                time = str(time)
                post(post_text, post_copyright, time)
                time = int(time)
                old_id[i] = id
