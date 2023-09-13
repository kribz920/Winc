from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """

def shortest_names(countries):
    short_names = []
    len_country_name = [len(country) for country in countries]
    for country in countries:
        if len(country) == min(len_country_name):
            short_names.append(country)
    return short_names

print(shortest_names(countries))


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

print(most_vowels(countries))
