"""
Boilerplate script for practicing Python regular expressions (regex).

Run this file locally (e.g., `python practice.py`) and
add your code under each exercise section.
"""

# The 're' module is required for regex operations in Python 
import re
from typing import List, Iterator, Optional, Match


def main() -> None:
    """Main function to run regex practice exercises."""

    # --- Data Variables for Exercises ---
    log_ex1: str = "ID: 404 STATUS: Not Found"
    data_stream_ex2: str = "file.mov,file.txt,file.jpg,file.txt"
    text1_ex3: str = "ACCESS DENIED"
    text2_ex3: str = "USER: 101 ACCESS DENIED"
    grades_ex4: str = "AABCFABBC"
    signal_ex5: str = "ERR_001_OK_OK_ERR_0005_OK"
    log_ex6: str = "2025-09-15 10:30:05_HOST 127.0.0.1"
    data_ex7_8: str = "user:Aramaki pass:D1g1t@l"
    tweets_ex9: str = "New vulnerability found #cyber #security Update now!"

    print("--- Regex Practice Script Online --- 💻\n")

    # -- Exercise 1: Core Functions (re.search) --
    print("--- Exercise 1 ---")
    # Your re.search() code here:
    target = "Found" # it's case sensitive
    if re.search(target, log_ex1):
        print("Target found! ✅")
    else: 
        print("Not found! ❌😵")

    print("\n")

    # -- Exercise 2: Tokenizing (re.split, re.findall) --
    print("--- Exercise 2 ---")
    # 2.1 (re.split):
    # 2.2 (re.findall):
    
    split_array = re.split(',', data_stream_ex2)
    print(split_array)
    
    all_file = re.findall('file.txt', data_stream_ex2)
    print(all_file)

    print("\n")

    # -- Exercise 3: Anchors (^ and $) --
    print("--- Exercise 3 ---")
    # 3.1 (Start anchor ^):
    # 3.2 (End anchor $):
    
    if re.search('^ACCESS',text1_ex3):
        print(re.search('^ACCESS',text1_ex3))
        print("Yes, the access. 🐕‍🦺")
        
    if re.search('DENIED$',text2_ex3):
        print(re.search('DENIED$',text2_ex3))
        print("Access denied, bro! 😎")

    print("\n")

    # -- Exercise 4: Character Classes ([]) --
    print("--- Exercise 4 ---")
    # 4.1 (Set operator [AB]):
    # 4.2 (Negation set [^A]):
    
    print(grades_ex4)
    print(re.findall('[AB]', grades_ex4))
    print(re.findall('[^A]', grades_ex4))
    print(re.findall('[^B]', grades_ex4))
    print(re.findall('[^C]', grades_ex4))
    print(re.findall('[^AB]', grades_ex4))

    print("\n")

    # -- Exercise 5: Quantifiers ({m,n}, +, *) --
    print("--- Exercise 5 ---")
    # 5.1 ({m,n}):
    # 5.2 (+):
    # 5.3 (*):
    
    print(re.findall('ERR_\d*', signal_ex5))
    print(re.findall('OK+', signal_ex5))
    print(re.findall('_+', signal_ex5))

    print("\n")

    # -- Exercise 6: Metacharacters (\d, \w, .) --
    print("--- Exercise 6 ---")
    # 6.1 (\d+):
    # 6.2 (\w+):
    # 6.3 (.{10}):
    print(log_ex6)
    print(re.findall('\d+', log_ex6))
    print(re.findall('\w+', log_ex6))
    print(re.findall('\D+', log_ex6))
    print(re.findall('[a-zA-Z]', log_ex6))

    print("\n")

    # -- Exercise 7: Groups (()) and finditer --
    print("--- Exercise 7 ---")
    # Your re.finditer() code here:

    print("\n")

    # -- Exercise 8: Named Groups (?P<name>...) --
    print("--- Exercise 8 ---")
    # Your re.finditer() code with named groups here:

    print("\n")

    # -- Exercise 9: Lookahead (?=...) --
    print("--- Exercise 9 ---")
    # Your re.findall() code with lookahead here:

    print("\n")

    # -- Exercise 10: Verbose Mode (re.VERBOSE) --
    print("--- Exercise 10 ---")
    # Your multiline re.finditer() code with re.VERBOSE here:

    print("\n--- Script Complete ---")


if __name__ == "__main__":
    main()