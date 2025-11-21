# list, dictionary and set comprehension

# structure
# expression for item in iterable if condition


# list comprehension
numbers = [10, 15, 20, 33, 42, 55, 60]
evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(evens)

# becomes

evens_comprehension = [num for num in numbers if num % 2 == 0]
print(evens_comprehension)


numbers_two = [10, -5, 3, -2, 8 -1, 6]
positive_numbers = []

for num in numbers_two:
    if num > 0:
        positive_numbers.append(num)

print(positive_numbers)

positive_numbers_comprehension = [num for num in numbers_two if num > 0]
print(positive_numbers_comprehension)


emails = ["user1@gmail.com", "admin@yahoo.com", "support@outlook.com"]
domains = []

for email in emails:
    domains.append(email.split('@')[1])
print(domains) 

domains_comprehension = [email.split('@')[1] for email in emails]
print(domains_comprehension)

word = "comprehensions"
unique_letters = set()

for letter in word:
    unique_letters.add(letter)
print(sorted(unique_letters))

unique_letters_comprehension = {letter for letter in word}


sentence = "Comprehensions make Python code cleaner"
word_lengths = {}
for word in sentence.split():
    word_lengths[word] = len(word)
print(word_lengths)

word_lengths_comprehension = {word : len(word) for word in sentence.split()}
print(word_lengths_comprehension)
