import pandas as pd

# aggregate functions

# reduces a set of values into a single summary value
# used to summarize and analyze data
# often used with the groupby() function

pokemon_df = pd.read_csv("./pokemon.csv", index_col="Name")


# whole data frame aggregate functions
print(pokemon_df.mean(numeric_only=True)) # we're telling pandas to only analyze numeric columns
print(pokemon_df.sum(numeric_only=True))
print(pokemon_df.min(numeric_only=True))
print(pokemon_df.max(numeric_only=True))
print(pokemon_df.count()) # no need for numeric only, pandas will count how many values within each column


# single column aggregate functions
print(pokemon_df["Height"].mean()) # since height is numeric, no need to specify
print(pokemon_df["Height"].sum())
print(pokemon_df["Height"].min())
print(pokemon_df["Height"].max())
print(pokemon_df["Height"].count())


# groupby()

typeOne_group = pokemon_df.groupby("Type1")
print(typeOne_group) # prints object, not a list

print("\n\nheight mean\n\n")
print(typeOne_group["Height"].mean()) # prints mean of height by Type1 groups

print("\n\nheight min\n\n")
print(typeOne_group["Height"].min())

print("\n\nheight max\n\n")
print(typeOne_group["Height"].max())

print("\n\nheight sum\n\n")
print(typeOne_group["Height"].sum())
