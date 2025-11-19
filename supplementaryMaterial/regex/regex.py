# Regular Expressions

# Used to search for pattern of strings

# ^ $               -> describe a position
# [a-t] and \w      -> describe a set of characters 
#  + * {9}          -> describe a quantifier (a way to specify the number of character ocurrences)


# Sample text
# --------------
# Francois
# Mike Whitney
# Sagun Khatri
# Nick Francesco
# Pickles
# K5ANR


# Regex
# --------------
# Fran                  -> would return "Francois" and "Nick Francesco"

# ^Fran                 -> would return only Francois because the caret means "start of the string"
# i$                    -> would return Sagun Khatri because the dollar sign means the end of the string

# \d    (digit)         -> any entry with digits, K5ANR
# \s    (space)         -> matches a whitespace, would return: Mike Whitney Sagun Khatri Nick Francesco
# \w    (word)          -> matches a-z, A-Z, 0-9 and _
# \d\d                  -> won't have any matches because there's no entry with 2 consecutive digits
# ^\w\w\w\w\s           -> matches any entry with 4 letters/numbers/underscores followed by a whitespace: Mike Whitney Nick Francesco

# *                     -> 0+
# ?                     -> 0 or 1
# +                     -> 1+ (positive number of ocurrences)
# {n}                   -> exactly n ocurrences
# [...]                    -> creates custom character set ——where the dots are

# [aeiou]{2}            -> would only match Francois because this regex means "2 consecutive vowels"
# ^\w{7}$               -> only returns Pickles
# ^\w{7}                -> returns Francois Mike Whitney Nick Francesco Pickles

import re

names = ['Finn Bindeballe',
         'Geir Anders Berge',
         'HappyCodingRobot',
         'Ron Cromberge',
         'Sohil']

#                                       --find people with first and last name only--

regex_one = r'^\w+\s\w+$'           # use r'' when writing regex expression to avoid "SyntaxWarning: invalid escape sequence"

print("\n\nFirst Regex exercise.\n\n")
for name in names:
    result = re.search(regex_one, name)
    if result:
        print(name)
        print(result)               # match object returns a wealth of information regarding the found pattern


regex_two = r'C\w*'      

print("\n\nSecond Regex exercise.\n\n")
for name in names:
    result = re.search(regex_two, name)
    if result:
        print(name)
        print(result)
        print(result.start())
        print(result.end())
        
        print(result.span())        # returns same result of .start() and .end()
        print(result.group())       # display the substring that matched the regex
        
        
names_two = ['Brian Daugette',
             'Veronica Supersonica',
             'Tony Gasparovic',
             'Patrick Germann',
             'm!sha']



#                          --a group is a way to identify and name a part of the regex pattern found--

regex_three = r'(?P<fn>\w+)\s+(?P<ln>\w+)'  # ()        -> creates a regex group which you can later access
                                            # ?P<...>   -> gives the regex group a name ——the name is what's inside <>


print("\n\nThird Regex exercise.\n\n")
for name in names_two:
    match = re.search(regex_three, name)
    
    if match:
        print(f"\n\n{name}")
        print(match.group(1))       # access first group
        print(match.group(2))       # access second group
        
        print(match.group('fn'))    # accesses group with name fn
        print(match.group('ln'))    # accesses group with name ln

regex_four = r'^[a-zA-Z!]+$'

for name in names_two:
    match = re.search(regex_four, name)
    
    if match:
        print(f"\n\n\n{name}")
        print(match)
        
#                                       --re.findall(pattern, strings, flag=0)--
#                   --returns all non-overlapping matches of pattern in string, as a list of strings or tuples--

regex_five = r'[a-z]+'

#                                  this will return a list of strings, not match objects
for name in names_two:
    matches = re.findall(regex_five, name)
    
    if matches:
        print(matches)
        
#                  returns an iterator-yielding match objects over all non-overlapping matches for the RE pattern in string
for name in names_two:
    matches = re.finditer(regex_five, name)
    if matches:
        for match in matches:
            print(match)
            
            
values = [
    'https://www.socratica.com',
    'http://www.socratica.org',
    'file://test.this.path',
    'com.socratica.www_https://'
]

regex_six = r'https?'

#                                   .match() -> only searches from the beginning
# if zero or more characters at the beginning of 'string' match the regular expression 'pattern', return a corresponding match object
# Returns None if the string doesn't match the regex pattern

for value in values:
    match = re.match(regex_six, value)
    
regex_seven = r'https?://w{3}.\w+.(org|com)'

#                                   .fullmatch() -> beggining and end
# I f the whole string matches the regular expression pattern, return a corresponding match object.
# Return None if the string does not match the pattern.
for value in values:
    match = re.fullmatch(regex_seven, value)


# re.split() -> split string by occurences of the pattern
# re.sub() -> search and replace