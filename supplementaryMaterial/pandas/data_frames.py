import pandas as pd

# A data frame is a tabular data structure with rows and columns, 2 dimensional
spongebob_data = {
    "Name" : ["Spongebob", "Patrick", "Squidward"],
    "Age" : [30, 35, 50]
}
 
spongebob_df = pd.DataFrame(spongebob_data, index=["Employee 1", "Employee 2", "Employee 3"])

print(spongebob_df)
print(spongebob_df.loc["Employee 1"])
print(spongebob_df.loc["Employee 2"])
print(spongebob_df.loc["Employee 3"])
# the same as
print(spongebob_df.iloc[0])
print(spongebob_df.iloc[1])
print(spongebob_df.iloc[2])


#                                               --add a new column--
spongebob_df["Job"] = ["Cook", "Caller", "Cashier"] # Job is the new row
print(spongebob_df)


#                                               --add a new row--
new_row = pd.DataFrame([{"Name": "Sandy",  "Age" : 28, "Job" : "Engineer"}, 
                        {"Name": "Eugene",  "Age" : 60, "Job" : "Manager"}], 
                       index=["Employee 4", "Employee 5"]) 
# if you wanted to add three new rows, the list should have three dictionaries pd.DataFrame([{}, {}, {}])

spongebob_df = pd.concat([spongebob_df, new_row])
print(spongebob_df)
