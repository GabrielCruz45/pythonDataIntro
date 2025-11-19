import pandas as pd

# data cleaning

# the process of fixing/removing
# incomplete, incorrect or irrelevant data
# more than half of the work done in Pandas is data cleaning

pokemon_df = pd.read_csv("./pokemon.csv")

# drop irrelevant columns
pokemon_df = pokemon_df.drop(columns=["No"]) # you need to assign the df again
print(pokemon_df)

# handle missing data

# dropna -> drop not available
# pokemon_df = pokemon_df.dropna(subset="Type2")

# instead of deleting the rows with missing data on Type2, we will fill
pokemon_df = pokemon_df.fillna({"Type2" : "None"})

print(pokemon_df.to_string())

# fix inconsistent values

pokemon_df["Type1"] = pokemon_df["Type1"].replace(
    {"Grass" : "GRASS", "Poison" : "POISON", "Fire" : "FIRE", "Water" : "WATER"}
)
print(pokemon_df.to_string())

# standarize text
pokemon_df["Name"] = pokemon_df["Name"].str.lower()
print(pokemon_df.to_string())

# fix data types
pokemon_df["Legendary"] = pokemon_df["Legendary"].astype(bool)
print(pokemon_df.to_string())

# remove duplicate values
pokemon_df = pokemon_df.drop_duplicates()
print(pokemon_df.to_string())
