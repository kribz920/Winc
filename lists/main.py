# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
# example_list_of_lists = [['Bob', 3.14, 42], ['Preeti', 3.14, 42]]
Movie_list = ["Jaws", "Star Wars: Episode IV - A New Hope", "E.T. the Extra-Terrestrial", "Memoirs of a Geisha"]

# for movie in Movie_list:
#     Movie_list[movie] = Movie_list[movie].lower()
# print(Movie_list)
# Won = filter(lambda c: c[1] == "Won", Movie_list)
# print(list(Won))
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

