from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

def shortest_names(countries):
    short_names = []
    len_country_name = [len(country) for country in countries]
    for country in countries:
        if len(country) == min(len_country_name):
            short_names.append(country)
    return short_names


def most_vowels(countries):
    vowels = "aeiouAEIOU"
    vowel_counts = []
    # lower_case_country = [country.lower() for country in countries]
    for x in countries:
        count = 0
        for z in x:
            if z in vowels:
                count += 1
        vowel_counts.append((x, count))
    #print(vowel_counts)
    sorted_list = sorted(vowel_counts, key=lambda x: x[1], reverse=True)
    sorted_strings = [x for x, count in sorted_list][:3]
    #print(sorted_list)
    return sorted_strings


def alphabet_set(countries):
    lower_case_country = [country.lower() for country in countries]
    print(lower_case_country)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_list = []
    count_letters = []
    for country in lower_case_country:
        for letter in country:
            if letter in alphabet:
                if letter not in letter_list:
                    letter_list.append(letter)
                else:
                    
    count_letters = len(letter_list)
    return countries

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """
    # print(shortest_names(countries))
    # print(most_vowels(countries))
    print(alphabet_set(countries))