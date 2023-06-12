# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
# example_list_of_lists = [['Bob', 3.14, 42], ['Preeti', 3.14, 42]]
Movie_list = ["Jaws", "Star Wars: Episode IV - A New Hope", "E.T. the Extra-Terrestrial", "Memoirs of a Geisha"]


for x in range(len(Movie_list)):
    Movie_list[x] = Movie_list[x].lower()

def  alphabetical_order(movies):
    sorted_list = sorted(movies)
    return sorted_list

def won_golden_globe(film_name):
    lowercase_film_name = film_name.lower()
    if lowercase_film_name in Movie_list:
        return True
    else:
        return False

movie_alphabetical_order = (alphabetical_order(Movie_list))
# print(movie_alphabetical_order)

did_movie_won_golden_globe = won_golden_globe("jawas")
print(did_movie_won_golden_globe)


# John's son Joseph accidentally mixed in some of his own work as lead singer for Toto with a list of his dad's compositions. Write a function remove_toto_albums that takes a list of strings,
# removes Joseph's Toto albums from it and returns the tidy list.
# Use this information: Wikipedia -- Joseph Williams (musician)
# It is not certain that all of Joseph's Toto albums are in the list received by remove_toto_albums, but they might! Don't let your script run into any errors.
# Joseph did not inherit his dad's sloppiness with capitalization, so his Toto albums would be listed correctly.
# Search the web on how to remove an item from a list by value.

# mixed_albums = ['Fahrenheit', 
#                'The Seventh One', 
#                'Falling in Between', 
#                'Toto XIV', 'Old Is New',
#                'pippo']


# def remove_toto_albums(albums):
#     Joseph_albums = ['Fahrenheit', 
#                'The Seventh One', 
#                'Falling in Between', 
#                'Toto XIV', 'Old Is New']
#     for x in Joseph_albums:
#         if x in mixed_albums:
#             mixed_albums.remove(x)
#     return mixed_albums

# cleanup_list = remove_toto_albums(mixed_albums)
# print(cleanup_list)


album_list = ['I Passed for White',"Because They're Young", 'Fahrenheit', 'The Seventh One', 'Falling in Between', 'Toto XIV', 'Old Is New']

def remove_toto_albums(album_list):
        toto_albums = ['Fahrenheit', 'The Seventh One', 'Falling in Between', 'Toto XIV', 'Old Is New']
        for x in toto_albums:
             if x in album_list:
                  album_list.remove(x)
        return album_list

print(remove_toto_albums(album_list))