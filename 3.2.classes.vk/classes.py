from urllib.parse import urlencode

import requests

APP_ID = 6773521
AUTH_URL = 'https://oauth.vk.com/authorize?'

auth_data = {
    'client_id': APP_ID,
    'display': 'page',
    'redirect_uri': 'https://oauth.vk.com/blank.html',
    'response_type': 'token',
    'scope': 'friends',
    'v': '5.92'
}

# print(AUTH_URL + (urlencode(auth_data)))

token = '0604595234f3425f42c4cad8791ac96d1f52b43be6e446c098edb38860cce4ab425fd5ac8cf1e8b3daaaa'


class User:
    def __init__(self, id_user):
        self.id_user = id_user

    def __str__(self):
        return 'https://vk.com/id' + str(self.id_user)

    def get_friends(self):
        params = {
            'user_id': self.id_user,
            'access_token': token,
            'v': '5.92'
        }

        response = requests.get('https://api.vk.com/method/friends.get',
                                params)
        return response.json()


Kris = User(120597952)
friends_Kris = Kris.get_friends()

Anna = User(176913353)
friends_Anna = Anna.get_friends()

common_friends = list(set(friends_Anna['response']['items']) & set(friends_Kris['response']['items']))
common_friends_class = []
for i in common_friends:
    common_friends_class.append(User(i))
print(Kris)
print(common_friends_class)
