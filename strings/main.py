# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
player_1 = "Ruud Gullit"
player_2 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = player_1 + ' ' + str(goal_0) + "," + " " + player_2 + ' ' + str(goal_1)
# print(scorers)
report = player_1 + " scored in the " + str(goal_0) + "nd minute" + f"\n{player_2} scored in the {goal_1}th minute"

print(report)
player = player_1
first_name = player[0:player.find(" ")]
# print(first_name)

last_name_with_space = player[player.find(" "):]
last_name = last_name_with_space.strip()
last_name_len = len(last_name)
name_short = (first_name[0] + ". " + last_name)
# print(name_short)
chant_ruud = (first_name + "! ") * len(first_name)
chant = chant_ruud.strip()
print(chant)

good_chant = chant[-1] != " "
# print(good_chant)