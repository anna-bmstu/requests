import requests
import json
import datetime
from operator import itemgetter

ACCESS_TOKEN = '17da724517da724517da72458517b8abce117da' \
               '17da72454d235c274f1a2be5f45ee711'
V = '5.81'

url = 'https://api.vk.com/method/users.get'  # method for getting user id by nickname
url_2 = 'https://api.vk.com/method/friends.get'  # method for getting list of friends


def calc_age(uid):
    # get id by nickname
    if type(uid) == str:
        payload = {'v': V, 'access_token': ACCESS_TOKEN, 'user_ids': uid}
        r = requests.get(url, params=payload)

        # convert json string into dict
        p_s = json.loads(r.text)
        uid = p_s['response'][0]['id']

        # bdate field is for getting birthday
        payload_2 = {'v': V, 'access_token': ACCESS_TOKEN, 'user_id': uid, 'fields': 'bdate'}
        r2 = requests.get(url_2, params=payload_2)
        p_s2 = json.loads(r2.text)
        list_friends = p_s2['response']['items']  # list of dicts, where dict contains info about each friend

        list_of_ages = []
        for i in list_friends:
            if ('bdate' in i) == True:
                if len(i['bdate']) > 5:      # check if there is a year of birth
                    day, month, year = i['bdate'].split('.')
                    list_of_ages.append(int(datetime.date.today().strftime("%Y")) - int(year))

        ages = sorted(list(set(list_of_ages)))
        t = [(k, list_of_ages.count(k)) for k in ages]

        return sorted(t, key=itemgetter(1), reverse=True)


if __name__ == '__main__':
    res = calc_age('ann.wvss')
    print(res)
