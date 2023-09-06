# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
def create_passport(
        name: str, 
        date_of_birth: str,
        place_of_birth: str,
        height: float,
        nationality: str):
    passport = {'name': name, 
        'date_of_birth': date_of_birth,
        'place_of_birth': place_of_birth,
        'height': height,
        'nationality': nationality}
    return (passport)


def add_stamp(passport, country):
    if 'stamps' not in passport:
         passport['stamps'] = []
    if country not in passport['stamps'] and country not in passport['nationality']:
            passport['stamps'].append(country)
            print(['stamps'])
    return passport

def add_biometric_data(passport, type_biometric, value, date_recorded):
    if 'biometric' not in passport:
        passport['biometric'] = {}
        passport['biometric'][type_biometric] = {'date': date_recorded, 'value': value}
    else:
        passport['biometric'][type_biometric] = {'date': date_recorded, 'value': value}
    return passport