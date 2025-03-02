"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Dominika Lukášková
email: lukaskova.dominika@gmail.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

name = input("Enter your login name: ")
password = input("Please enter your login password: ")

registered_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

separator = "-" * 50
print(separator)


if name in registered_users and registered_users[name] == password:
    print("Welcome to the app,", name,".")
    choice = input("Choose by numbers (1-3) which part of the text you want to analyse: ")
    print(separator)
    if choice.isdigit() and 1 <= int(choice) <= 3:
        selected_text = TEXTS[int(choice) - 1]
        print("Your chosen text is: ", "\n", selected_text)
        print(separator)

        # Total count words
        words = selected_text.split()
        word_count = len(words)
        print("Number of words in the selected text is:", word_count)

        # Total count for titlecase
        title_count = sum(word.istitle() for word in words)
        print("Number of words starting with a capital letter:", title_count)

        # Total count for uppercase
        uppercase_count = sum(word.isupper() for word in words)
        print("Number of words written in capital letters:", uppercase_count)

        # Total count for lowercase
        lowercase_count = sum(word.islower() for word in words)
        print("Number of words written in lower case:", lowercase_count)

        # Count for numeric strings
        numeric_count = sum(word.isnumeric() for word in words)
        print("Number of numeric strings:", numeric_count)

        # Sum of all numeric values
        numeric_sum = sum(int(word) for word in selected_text.split() if word.isnumeric())
        print("The sum of all numbers in the text is:", numeric_sum)
        print(separator)

        # Calculate the frequency of word lengths
        word_lengths = [len(word.strip(",.")) for word in words]
        length_counts = {}     

        for length in word_lengths:
            length_counts[length] = length_counts.get(length, 0) + 1
        print("LEN|  OCCURRENCES  |NR.")
        print(separator)

        for length, count in sorted(length_counts.items()):
            print(f"{length:2}|{'*' * count:<15}|{count}")


    else:
        print("Invalid choice! You can only enter numbers from 1 to 3.")
else:
    print("Unregistered user.")
