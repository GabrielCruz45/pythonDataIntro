import pandas as pd

data = {
    'Name' : ['Alice', 'Bob', 'Charlie', 'David'],
    'Score' : [85, 92, 78, 95],
    'Time_sec' : [125, 150, 90, 105]
}

df = pd.DataFrame(data)



# Use the .apply() method on the provided Pandas DataFrame df with a lambda function.

#   Normalize Score: Create a new column 'Norm_Score' by subtracting the minimum score (78) from each score.
df['Normalized_Score'] = df['Score'].apply(lambda x: x - 78)
print(df['Score'])
print(df['Normalized_Score'])

#   Time Grade: Create a column 'Speed' that returns 'Fast' if Time_sec is less than 100, otherwise 'Slow'.
df['Speed'] = df['Time_sec'].apply(lambda x: 'Fast' if x < 100 else 'Slow')
print(df['Speed'])

#   Full Name Index: Change the DataFrame index to be the uppercase version of the 'Name' column.
df.set_index(df['Name'].apply(lambda x: x.upper()), inplace=True)
print(df.index)

#   Score Difference: Use .apply() with axis=1 (row-wise) to create a column 'Diff' that is the difference between Score and Time_sec.
df['Diff'] = df.apply(lambda row: row['Score'] - row['Time_sec'], axis=1) 
#                            ^^^the current row (established with axis=1) is treated as a dictionary

# achieves the same thing
df['Diffe'] = df['Score'] - df['Time_sec'] 


print(df['Diff'])
print(df['Diffe'])


#   Custom Mapping: Create a column 'Initial' that extracts the first letter of the 'Name' column.
df['Initial'] = df['Name'].apply(lambda x: x[0])
print(df['Initial'])
