def addition(a: int, b: int) -> int: # type hints
    return a + b

print(addition(1, 2))
print(type(addition(1, 2)))

# simple lambda function
add_lambda = lambda a, b: a + b
print(add_lambda(1, 2))

# conditional lambda function
conditional_lambda = lambda x: "Even" if (x % 2 == 0) else "odd"
print(conditional_lambda(1))

# lambda functions shine when used in tandem with higher order functions
# most common ones are map() filter() and sorted()

# sorted() -> used to define a custom sort key
data_one = [("apple", 3), ("banana", 1), ("orange", 2)]
sorted_data = sorted(data_one, key=lambda item: item[1])
print(sorted_data)

# map() -> applies a function to every item in an iterable
data_two = [1, 2, 3, 4, 5, 7, 8, 9, 10]
power = list(map(lambda x: x ** x, data_two))
print(power)

# filter() -> used to select items from an iterable to satisfy a condition
data_three = [1, 2, 3, 4, 5, 6, 7]
evens = list(filter(lambda x: x % 2 == 0, data_three)) # el filter ya es un "if/else" per se
print(evens)
