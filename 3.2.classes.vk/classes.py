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

token = 'd4798e7ecf10b73f1a3b65ae24327ab20f85a8ef831c0693051c2b757b021a0be252a0a228912f181c97d'


class User:
    def __init__(self, id_user):
        self.id_user = id_user

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
user = 'https://vk.com/id' + str(common_friends[0])
print(user)
print(common_friends_class)
