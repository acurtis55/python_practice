import requests


# api request to get the first person
print("Getting first person...")
resp_one = requests.get("https://swapi.co/api/people/1")

if resp_one.status_code == 200:
    person = resp_one.json()
    for key in person:
        print("\t",key, person[key])


# api request to get all people
print("\nGetting the first ten people...")
resp_all = requests.get("https://swapi.co/api/people/")

if resp_all.status_code == 200:
    people = resp_all.json()
    print('First ten names: ')
    for character in people['results']:
        name = character['name']
        print("\t",name)


