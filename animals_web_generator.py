import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as data:
        return json.load(data)


def save_data(data_string):
    """Save a HTML file"""
    with open('animals_template.html', 'w') as animal_page:
        animal_page.write(data_string)


def serialize_animal(animal_data):
    """
    From a dictionary get animal data and return as html string
    """
    html_string = ''
    html_string += "\n<li class='cards__item'>\n"
    html_string += f"\t<div class='card__title'>{animal_data['name']}</div>\n"
    html_string += "\t<p class='card__text'>\n"
    if 'diet' in animal_data['characteristics']:
        html_string += f"\t\t<strong>Diet:</strong>  {animal_data['characteristics']['diet']}<br/>\n"
    if animal_data['locations']:
        html_string += f"\t\t<strong>Location:</strong> {animal_data['locations'][0]}<br/>\n"
    if 'type' in animal_data['characteristics']:
        html_string += f"\t\t<strong>Type:</strong> {animal_data['characteristics']['type']}<br/>\n"
    html_string += "\t</p>\n</li>\n"
    return html_string


def data_to_string(data):
    """
    Define an empty string and add name, diet, location
    and type for each animal. if there is data.
    """
    string_data = ''
    for animal in animals_data:
        string_data += serialize_animal(animal)
    return string_data


def change_html_data(new_data):
    with open('animals_template.html', 'r') as animals:
        old_file = animals.read()
        new_file = old_file.replace('__REPLACE_ANIMALS_INFO__', new_data)
    save_data(new_file)


""" Load data """
animals_data = load_data('animals_data.json')
new_data = data_to_string(animals_data)
""" Save data (one time replace)"""
#change_html_data(new_data)


