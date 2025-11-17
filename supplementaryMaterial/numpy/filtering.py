import numpy as np

# filtering = refers to the process of selecting elements from an array that match a given condition
ages = np.array([[21, 17, 19, 20, 16, 30, 18, 65],
                [39, 22, 15, 99, 18, 19, 20, 21]
])

teenagers = ages[ages < 18]
adults = ages[(ages >= 18) & (ages < 65)]
seniors = ages[ages >= 65]
evens = ages[ages % 2 == 0]
odds = ages[ages % 2 != 0]

print(teenagers)
print(adults)
print(seniors)
print(evens)
print(odds)

# use .where() when you want to preserve the original array's shape
teenagers_og = np.where(ages < 18, ages, np.nan)
adults_og = np.where((ages >= 18) & (ages < 65), ages, np.nan)
seniors_og = np.where(ages >= 65, ages, np.nan)

print(teenagers_og)
print(adults_og)
print(seniors_og)