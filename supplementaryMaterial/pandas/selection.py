import pandas as pd

pokemon_csv_df = pd.read_csv("./pokemon.csv")

# selection by column
print(pokemon_csv_df["Name"])               # truncated version
print(pokemon_csv_df["Name"].to_string())   # complete version

print("\n\n                             --No--\n\n")
print(pokemon_csv_df["No"].to_string())
print("\n\n                             --Type 1--\n\n")
print(pokemon_csv_df["Type1"].to_string())
print("\n\n                             --Type 2--\n\n")
print(pokemon_csv_df["Type2"].to_string())
print("\n\n                             --Height--\n\n")
print(pokemon_csv_df["Height"].to_string())
print("\n\n                             --Weight--\n\n")
print(pokemon_csv_df["Weight"].to_string())
print("\n\n                             --Legendary--\n\n")
print(pokemon_csv_df["Legendary"].to_string())

# you can select multiple columns

print("\n\n                             --Name, Height, Weight, Type 1--\n\n")
print(pokemon_csv_df[["Name", "Height", "Weight", "Type1"]].to_string()) # you pass a list

# selection by Row; with this data set it would be each pokemon and it's attributes

print("\n\n                             --Selection by Row--\n\n")
print(pokemon_csv_df.loc[0])

# we can specify one column to be the index if number list is harder to work with
print("\n\n                             --Selection by Row after custom indexing--\n\n")
pokemon_csv_df_two = pd.read_csv("./pokemon.csv", index_col="Name")
print(pokemon_csv_df_two.loc["Moltres"]) # remember .loc[] -> location by label
print(pokemon_csv_df_two.loc["Mewtwo", ["No", "Weight", "Type1"]]) # list if you want specific columns


# : if you want various rows, from x to y df.loc["x" : "y", ["col1", "col2", ...]]
print(pokemon_csv_df_two.loc["Charmander" : "Blastoise", ["No", "Weight", "Type1"]]) # list if you want specific columns

# using number index location -> start : end : step
print(pokemon_csv_df_two.iloc[0 : 50 : 2, 0 : 3]) # you won't use column names; use the column numbers



#                                                   --User Input--
print("\n\n                             --User input--\n\n")
pokemon = input("Enter a Pokémon name: ")

# we're using a try block in case the pokémon name doesn't exist
try:
    print(pokemon_csv_df_two.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found!")
