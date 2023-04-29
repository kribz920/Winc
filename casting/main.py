# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line
leek_price = 2
price_of_leek = f"Leek is {leek_price} euro per kilo."
print(price_of_leek)

four_leek = 'leek 4'
number_leek = int((four_leek[four_leek.find(" "):]))
# print(type(number_leek))
sum_total = number_leek * leek_price
print(sum_total)

broccoli_price = 2.34
broccoli_amout = 1.6
broccoli_total = broccoli_price * broccoli_amout
print(f"{broccoli_amout}kg broccoli costs {round(broccoli_total,2)}e")