import tinder.tinder_resource as tinder_resource
import json

facebook_token = ''
facebook_id = ''


# WARNING: THIS TAKES A WHILE!
def get_detailed_matches():
    data = tinder_resource.get_matches()['matches']
    matches = {}
    for match in data:
        user_id = match['person']['_id']
        user = tinder_resource.get_user(user_id)
        matches[user_id] = user['results']

    return matches


def save_detailed_matches():
    save('detailed_matches.json', jsonify(get_detailed_matches()))


def save_data():
    save('matches_data.json', jsonify(tinder_resource.get_matches()['matches']))
    save('profile.json', jsonify(tinder_resource.get_own_profile()))
    save('raw.json', jsonify(tinder_resource.get_matches()))


def save(file_name, data):
    f = open(file_name, 'w')
    f.write(data)
    f.close()


def jsonify(data):
    return json.dumps(data, indent=4)


tinder_resource.auth(facebook_token=facebook_token, facebook_id=facebook_id)

#save_data()
#save_detailed_matches()