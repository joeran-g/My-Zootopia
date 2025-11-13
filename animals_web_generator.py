import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as data:
        return json.load(data)


def save_data(data_string):
    """Save a HTML file"""
    with open('animals_template.html', 'w') as animal_page:
        animal_page.write(data_string)


def data_to_string(data):
    """
    Define an empty string and add name, diet, location
    and type for each animal. if there is data.
    """
    string_data = ''
    for animal in animals_data:
        string_data += "<li class='cards__item'>\n"
        string_data += f"<div class='card__title'>{animal['name']}</div>\n"
        string_data += "<p class='card__text'>"
        if 'diet' in animal['characteristics']:
            string_data += f"<strong>Diet:</strong>  {animal['characteristics']['diet']}<br/>\n"
        if animal['locations']:
            string_data += f"<strong>Location:</strong> {animal['locations'][0]}<br/>\n"
        if 'type' in animal['characteristics']:
            string_data += f"<strong>Type:</strong> {animal['characteristics']['type']}<br/>\n"
        string_data += "</p>\n</li>\n"
    return string_data


def change_html_data(new_data):
    with open('animals_template.html', 'r') as animals:
        old_file = animals.read()
        new_file = old_file.replace('__REPLACE_ANIMALS_INFO__', new_data)
    save_data(new_file)


""" Load data """
animals_data = load_data('animals_data.json')
new_data = data_to_string(animals_data)
""" Save data (commented out)"""
#change_html_data(new_data)


