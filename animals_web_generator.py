import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as data:
        return json.load(data)


animals_data = load_data('animals_data.json')
print(animals_data)

for animal in animals_data:
    if animal['name']:
        print(f"Name: {animal['name']}")
    if 'diet' in animal['characteristics']:
        print(f"Diet: {animal['characteristics']['diet']}")
    if animal['locations']:
        print(f"Location: {animal['locations'][0]}")
    if 'type' in animal['characteristics']:
        print(f"Type: {animal['characteristics']['type']}")
    print()