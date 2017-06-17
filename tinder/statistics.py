import json
import datetime
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict


def open_file(file):
    with open(file) as data_file:
        return json.load(data_file)


def age_statistics():
    matches = open_file('matches.json')

    ages = []
    for match in matches:
        age = calculate_age(match['person']['birth_date'])
        ages.append(age)

    print('### OLDEST MATCH ###')
    print('{0} years'.format(max(ages)))
    print('### YOUNGEST MATCH ###')
    print('{0} years'.format(min(ages)))
    print('### AVERAGE AGE ###')
    print('{0:.2f} years'.format(sum(ages) / len(matches)))

    plt.title('Tinder')
    plt.hist(ages, bins=100)
    plt.xticks(np.arange(20, 38))
    plt.ylabel('Matches')
    plt.xlabel('Age')
    plt.show()


def calculate_age(birthday_string):
    today = datetime.date.today()
    birth_year = int(birthday_string[:4])
    birth_month = int(birthday_string[5:7])
    birthday = int(birthday_string[8:10])
    return today.year - birth_year - ((today.month, today.day) < (birth_month, birthday))


def distance_statistics():
    matches = open_file('detailed_matches.json')

    distances = []
    for match in matches:
        distance = matches[match]['distance_mi'] * 1.609344
        distances.append(distance)

    print('### FURTHEST AWAY MATCH ###')
    print('{0:.2f} km'.format(max(distances)))
    print('### CLOSEST MATCH ###')
    print('{0} km'.format(min(distances)))
    print('### AVERAGE DISTANCE ###')
    print('{0:.2f} km'.format(sum(distances) / len(matches)))

    plt.title('Tinder')
    plt.hist(distances, bins=100)
    plt.ylabel('Matches')
    plt.xlabel('Distance')
    plt.show()


def school_statistics():
    matches = open_file('detailed_matches.json')

    schools = {}
    for match in matches:
        school = matches[match]['schools']
        if len(school) is not 0:
            if school[0]['name'] in schools:
                schools[school[0]['name']] += 1
            else:
                schools[school[0]['name']] = 1

    crap_impl_but_im_hungry_so_screw_it = {}
    for school in schools:
        if schools[school] > 1:
            crap_impl_but_im_hungry_so_screw_it[school[:5]] = schools[school]

    X = np.arange(len(crap_impl_but_im_hungry_so_screw_it))
    plt.bar(X, crap_impl_but_im_hungry_so_screw_it.values())
    plt.xticks(X, crap_impl_but_im_hungry_so_screw_it.keys())
    ymax = max(crap_impl_but_im_hungry_so_screw_it.values()) + 1
    plt.ylim(0, ymax)
    plt.show()


# age_statistics()
# distance_statistics()
school_statistics()
