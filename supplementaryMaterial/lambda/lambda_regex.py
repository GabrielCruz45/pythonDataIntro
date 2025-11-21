import re

# 📝 RegEx Exercises (5)
# Instructions: Use the re.sub() function with a lambda function as the repl argument on the string 
text = "Error 404, Code 500, Code 200, Error 503"


#     Code Incrementor: Find all occurrences of "Code XXX" (where XXX is a number) and increment the number by 1. (e.g., "Code 500" → "Code 501").
result_one = re.sub(r'Code\s(\d+)', lambda match: f"Code {int(match.group(1)) + 1}", text)
print(result_one)


#     Error Masking: Find all occurrences of "Error XXX" and replace the number with three asterisks (***).
result_two = re.sub(r'Error\s\d+', "Error ***", text)
print(result_two)


#     Vowel Count Replacement: Find any word in the string and replace it with its total number of vowels (A, E, I, O, U).
vowels = 'aeiou'
result_three = re.sub(r'([a-zA-Z]+\s)', lambda match: f"{str(sum(1 for char in match.group() if char in vowels))} ", text)
#                                                            ^^^^conditional sum technique
print(result_three)


#     Capture Group Case: Find all numbers (e.g., 404) and replace them with the number enclosed in parentheses (404).
result_four = re.sub(r'(\d+)', lambda match: f"({match.group()})", text)
print(result_four)


#     Status Normalization: Find all occurrences of three-digit numbers and replace them with "Success" if the number is ≤300, and "Failure" otherwise.
result_five = re.sub(r'\d\d\d', lambda match: 'Success' if int(match.group()) <= 300 else 'Failure', text)
print(result_five)
