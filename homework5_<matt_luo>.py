pokemon = ["pikachu","charmander","squirtle","bulbasaur","pichu","raichu"]
print(pokemon)
pkmn1 = pokemon[0:2]
print("The first two items in the list are:", pkmn1[0],",", pkmn1[1])
pkmn2 = pokemon[2:4]
print("The middle two items in the list are:", pkmn2[0],",", pkmn2[1])
print("The first and last items in the list are:", pokemon[0],",", pokemon[5])

print("\n")
restaurant = ("mac & cheese","chicken nuggets","salad","deconstructed duck pate drizzled in a blueberry compote","fries")
for item in restaurant:
    print(item)
    
print("\n")
restaurant = ("four cheese truffle ravioli speckled with gold flakes","spicy McChicken","salad","deconstructed duck pate drizzled in a blueberry compote","fries")
for item2 in restaurant:
    print(item2)