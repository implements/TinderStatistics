import requests
import json

api_url = 'https://api.gotinder.com'
headers = {
    'content-type': 'application/json',
    'User-agent': 'Tinder/7.5.2 (iPhone; iOS 10.3.1; Scale/2.00)'
}


def auth(facebook_token, facebook_id):
    url = api_url + '/auth'
    data = json.dumps({'facebook_token': facebook_token, 'facebook_id': facebook_id})
    req = requests.post(url, headers=headers, data=data)
    headers.update({'X-Auth-Token': req.json()['token']})


def get_matches():
    url = api_url + '/updates'
    data = json.dumps({'last_activity_date': ''})
    req = requests.post(url, headers=headers, data=data)
    return req.json()


def get_own_profile():
    url = api_url + '/profile'
    req = requests.get(url, headers=headers)
    return req.json()


def get_user(user_id):
    url = api_url + '/user/{0}'.format(user_id)
    req = requests.get(url, headers=headers)
    return req.json()
