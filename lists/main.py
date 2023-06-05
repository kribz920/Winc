# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
# example_list_of_lists = [['Bob', 3.14, 42], ['Preeti', 3.14, 42]]
Movie_list = [["The Poseidon Adventure", "Nominated"],
              ["Cinderella Liberty", "Nominated"],
              ["Tom Sawyer", "Nominated"],
              ["Earthquake", "Nominated"],
              ["Jaws", "Won"],
              ["Close Encounters of the Third Kind", "Nominated"],
              ["Star Wars: Episode IV – A New Hope", "Won"],
              ["Superman", "Nominated"],
              ["Star Wars: Episode V – The Empire Strikes Back", "Nominated"],
              ["E.T. the Extra-Terrestrial", "Won"],
              ["If We Were in Love (from Yes, Giorgio)", "Nominated"],
              ["The River", "Nominated"],
              ["Empire of the Sun", "Nominated"],
              ["The Accidental Tourist", "Nominated"],
              ["Born on the Fourth of July", "Nominated"],
              ["Schindler's List", "Nominated"],
              ["Moonlight (from Sabrina)", "Nominated"],
              ["Seven Years in Tibet", "Nominated"],
              ["Saving Private Ryan", "Nominated"],
              ["Angela's Ashes", "Nominated"],
              ["A.I. Artificial Intelligence", "Nominated"],
              ["Memoirs of a Geisha", "Won"],
              ["War Horse", "Nominated"],
              ["Lincoln", "Nominated"],
              ["The Book Thief", "Nominated"],
              ["The Post", "Nominated"],
              ["The Fabelmans", "Nominated"]]


# Won = filter(lambda c: c[1] == "Won", Movie_list)

# print(list(Won))


def  alphabetical_order(movies):
    sorted_list = sorted(movies)
    return sorted_list

def won_golden_globe(film_name):
    lowercase_film_name = film_name.lower()
    lowercast_movie_list = list(map(lambda x: list(map(lambda y: y.lower(), x)), Movie_list))
    if any(lowercase_film_name in sublist for sublist in lowercast_movie_list):
        return True
    else:
        return False

movie_alphabetical_order = (alphabetical_order(Movie_list))
# print(movie_alphabetical_order)

did_movie_won_golden_globe = won_golden_globe("Jaws")
print(did_movie_won_golden_globe)