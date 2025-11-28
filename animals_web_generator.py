import data_fetcher
import requests


def save_data(data_string):
    """ Save html_string as HTML file """
    with open('Web-Template/animals.html', 'w') as animal_page:
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


def data_to_string(animal_data):
    """
    Define an empty string and add name, diet, location
    and type for each animal from a dictionary. if there is data.
    """
    string_data = ''
    for animal in animal_data:
        string_data += serialize_animal(animal)
    return string_data


def change_html_data(new_data):
    """ 
    Open the template and replace the placeholder 
    with the animal infos as html string.
    """
    with open("Web-Template/animals_template.html", "r") as data:
        old_file = data.read()
        new_file = old_file.replace("__REPLACE_ANIMALS_INFO__", new_data)
    save_data(new_file)


def main():
    """ Ask the user for an Animal, get data from the API and change the Placeholder in the html with data from those"""
    user_choice = input("Enter a name of an animal: ").strip().title()
    animals = data_fetcher.fetch_data(user_choice)
    # Generate message, if the animal doesn't exist.
    if not animals:
        new_data = f"\n<h2>The animal '{user_choice}' doesn't exist.</h2>\n"
    else:
        new_data = data_to_string(animals)
    # Save data 
    change_html_data(new_data)


if __name__ == "__main__":
    main()



