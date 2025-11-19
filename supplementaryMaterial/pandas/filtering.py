import pandas as pd

pokemon_df = pd.read_csv("./pokemon.csv", index_col="Name")

# Keeping rows that match a condition -> filtering in Pandas is  similar to NumPy
tall_pokemon = pokemon_df[pokemon_df["Height"] >= 2]
print(tall_pokemon)

heavy_pokemon = pokemon_df[pokemon_df["Weight"] >= 100]
print(heavy_pokemon)

legendary_pokemon = pokemon_df[pokemon_df["Legendary"] == 1]
print(legendary_pokemon)

water_pokemon = pokemon_df[pokemon_df["Type1"] == "Water"]
print(water_pokemon)

waterWater_pokemon = pokemon_df[(pokemon_df["Type1"] == "Water") | (pokemon_df["Type2"] == "Water")] # only "|" not "or" in pandas
print(waterWater_pokemon)


fire_or_flying_pokemon = pokemon_df[((pokemon_df["Type1"] == "Flying") | ((pokemon_df["Type2"] == "Flying"))) | 
                                 ((pokemon_df["Type1"] == "Fire") | ((pokemon_df["Type2"] == "Fire")))]
print(fire_or_flying_pokemon)


fire_and_flying_pokemon = pokemon_df[((pokemon_df["Type1"] == "Flying") | ((pokemon_df["Type2"] == "Flying"))) & 
                                 ((pokemon_df["Type1"] == "Fire") | ((pokemon_df["Type2"] == "Fire")))]
print(fire_and_flying_pokemon)

