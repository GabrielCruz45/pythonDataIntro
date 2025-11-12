import re

# .search() -> boolean
# .split() -> uses pattern to create a list of substrings
# .findall() -> looks for pattern and pulls out all ocurrences

text = "It's a good day today!"

if re.search("good", text):
    print("Wonderful!")
else:
    print("Alas :(")
    
text = "Amy works dilligently. Amy gets good grades because she studies hard. Amy is one of our most successful students."

print(re.split("Amy", text))
print(re.findall("Amy", text))


# regex uses a markup language
# ^ -> text after will retrieved
# $ -> text after will retrieved
# similar a % en SQL!


# returns a re.Match object; this object always has a boolean value of true (you can evaluate it in an if statement)
print(re.search("^Amy", text))
# the object also tells you what pattern was matched and where w/span

# patterns and character classes
grades = 'ACAAAABCBCBAA'
print(len(re.findall('B', grades)))
print(re.findall('[AB]', grades)) # this is called a set operator in re's markkup language

# simple regex to parse out all instances where an A is followed either by a B or a C
print(re.findall('[A][B-C]', grades))
print(re.findall('AB|AC', grades))

print(re.findall('[^A]', grades)) # the caret ^ is the negation operator; this will look for all instances of NOT 'A'
print(re.findall('^[^A]', grades)) # It will return a oattern if it doesn't start with 'A'

# quantifiers

# Quantifiers are the number of times you want a pattern to be matched, in order to match (??? lol)
# The most basic quantifier is expressed as e{min,max} 
# where 'e' is the expression or character we're matching
# min is the minimum number of times you want it matched
# max is the maximum number of times you want it matched
print(re.findall("A{2,10}", grades))
print(re.findall("A{1,1}A{1,1}", grades))
# As you can see this results in a different combination than the first pattern
# the first pattern is looking for any combination of 2 and up to 10 A's in a row.
# The second pattern is looking for two A's, back-to-back
# If you don't include a quantifier, the default is e{1,1}
# e{2,2} == e{2}
print(re.findall("AA", grades))
print(re.findall("A{2}", grades))


print(re.findall('A{1,10}B{1,10}C{1,10}', grades))
# There are 3 other quantifiers that are used as shorthand
# * -> 0 or more
# ? -> 1 or more
# + -> 1 or more

with open("datasets/ferpa.txt", "r") as file:
    wiki = file.read()
    print(re.findall("[a-zA-Z]{1,100}\[edit\]", wiki))
    print(re.findall("[\w]{1,100}\[edit\]", wiki)) # \w -> shorthand to match any letter
    print(re.findall("[\w ]*\[edit\]", wiki))
    
    for title in re.findall("[\w ]*\[edit\]", wiki):
        print(re.split("\[", title)[0])
        
# groups
# you can match different patterns at the same time and refer as you want to -> groups
# breaks into tuples?

print(re.findall("([\w ]*)(\[edit\])", wiki))


# two new funcs -> finditer() and group()
for item in re.finditer("([\w ]*)(\[edit\])", wiki):
    print(item.group(1))


    
# One more piece of regex groups that I rarely use, but is a good idea, is labeling or naming groups. 
# In the previous example I showed you how you can use the position of the group. 
# But giving them a label and looking at the results as a dictionary is pretty useful.
# For that, we use the syntax: (?P<name>), where the parenthesis starts the group. 
# The ?P indicates that this is an extension of basic regexes
# <name> is the dictionary key we want to use, wrapped in <>
for item in re.finditer("(?P<title>[\w ]*)(?P<edit_link>\[edit\])", wiki):
    print(item.groupdict())
    print(item.groupdict()['title'])
    
# other shorthands in regex markup language
# . for any single character that is not a newline
# \d for any digit
# \s for any whitespace character, like spaces and tabs


# look-ahead and look-behind matching

print("dame un breis")
print("----------------------------------------------------------------------------------------------------")
# The pattern being given to the regex engine is for text before or after the text we are trying to isolate.
# For example, in our headers, we want to isolate text which comes before the '[edit]' renedering, 
# but we actually don't care about the '[edit]' text itself.
# Thus far we've been throwing the '[edit]' away, but if we want to use them to match and don't want to capture them,
# we could put them in a group and use look-ahead instead with ?= syntax.
for item in re.finditer("(?P<title>[\w ]+)(?=\[edit\])", wiki):
    # What this regex says: match 2 groups. 
    # The first, will be named title and will have 1 or more amount of regular word characters and whitespace.
    # The second, will be the characters [edit] but we don't actually want this edit put in our output match objects.
    print(item)
    print(item.groupdict())

print("hola")

with open("datasets/buddhist.txt", "r") as file:
    wiki = file.read()
    print(wiki)
    
    # The verbose mode allows you to write multi-line regexes and increases readability
    
    pattern = r"""
        ^                                   # 1. Anchor Point
        (?P<title>.*?)                      # 2. Target ID (Title)
        \s+(?:–|is)\s+located\s+in\s+       # 3. Handshake Protocol (Location Delimiter)
        (?P<city>.*?)                       # 4. Primary Coordinate (City)
        ,\s+                                # 5. Coordinate Separator
        (?P<state>[^,\[(]*)                 # 6. Secondary Coordinate (State) & Noise Filter
    """

    for item in re.finditer(pattern, wiki, re.VERBOSE):
        print(item.groupdict())
        
        
print("final :P")

