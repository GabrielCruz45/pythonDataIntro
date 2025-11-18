import pandas as pd

print("\n\n                                 ---csv---\n\n")
pokemon_csv_df = pd.read_csv("./pokemon.csv")
print(pokemon_csv_df.to_string()) # to print a non-truncated version -> .to_string()

print("\n\n                                 ---json---\n\n")
pokemon_json_df = pd.read_json("./pokemon_data.json")
print(pokemon_json_df.to_string()) # to print a non-truncated version -> .to_string()