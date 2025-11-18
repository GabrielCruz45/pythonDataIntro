# buitl on top of NumPy
# pandas stands for "panel data"; not the animal

# series -> a one dimensional labeled column
# data fram -> a 2 dimensional labeled grid (a table)

# with pandas you can: import, display, manipulate, export tabular data

import pandas as pd

print(pd.__version__)

# int type
int_data = [100, 102, 104]
int_series = pd.Series(int_data, index=["Apartment #1", "Apartment #2", "Aprtment #3"]) # index could be array, tuple, dictionary, np.array and/or another series
print(int_series)

# float type
float_data = [100.1, 102.2, 104.3]
float_series = pd.Series(float_data)
print(float_series)

# string type
string_data = ["A", "B", "C"]
string_series = pd.Series(string_data)
print(string_series)

# boolean type
boolean_data = [False, False, True]
boolean_series = pd.Series(boolean_data)
print(boolean_series)

print(int_series.loc["Apartment #2"]) # locates value by label

int_series.loc["Apartment #1"] = 98 # changes value by label
print(int_series.loc["Apartment #1"]) 

print(int_series.iloc[0]) # location by integer (each row is index starting from 0)


print("-----------")
int_data_two = [100, 102, 104, 200, 202]
int_series_two = pd.Series(int_data_two, index=["a", "b", "c", "d", "e"])
print(int_series_two[int_series_two >= 200])
print(int_series_two[int_series_two < 200])

print("-----------")

calories = {"Day 1" : 1750, "Day 2" : 2100, "Day 3" : 1700}
caloric_series = pd.Series(calories)

caloric_series.loc["Day 3"] += 500
print(caloric_series.loc["Day 3"])
print(caloric_series[caloric_series >= 2000])
print(caloric_series[caloric_series < 2000])
