import requests
import json
import os
from dotenv import load_dotenv


load_dotenv()


ANIMALS_URL = "https://api.api-ninjas.com/v1/animals"
API_KEY = os.getenv('API_KEY')


def fetch_data(animal_name):
    """
    Fetch Json-data from the API, based on 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
            ...
        },
        'locations': [
            ...
        ],
        'characteristics': {
            ...
        }
    },
    """
    res = requests.get(ANIMALS_URL, params={
                                "X-API-KEY": API_KEY,
                                "name": animal_name
                                })
    return res.json()