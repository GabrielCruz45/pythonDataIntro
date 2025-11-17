import numpy as np

rng = np.random.default_rng() # generated numbers will be the same if using the same seed
# you want a random number between 1 and 6; x, y exclusive
print(rng.integers(low=1, high=101, size=3))

# you could also generate a np array
print(rng.integers(low=1, high=101, size=(3, 2)))

print(np.random.uniform()) # prints a random number with a value between 0 and 1

rng_two = np.random.default_rng(seed=(int((np.random.uniform()) * (np.random.uniform() * 100))))
print(rng_two.random())

print(np.random.uniform(low=-1, high=1, size=(10, 10)))

# shuffle an array

array = np.array([1, 2, 3, 4, 5])
print(array)
rng = np.random.default_rng()
rng.shuffle(array)
print(array)

fruits = np.array(["apple", "orange", "banana", "coconut", "pineapple"])
print(fruits)
rng.shuffle(fruits)
fruit = rng.choice(fruits)
more_fruits = rng.choice(fruits, size=(10, 10))
print(fruits)
print(fruit)
print(more_fruits)
