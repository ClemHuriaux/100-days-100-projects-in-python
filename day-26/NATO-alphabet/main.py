import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
dict_alphabet_words = {row.letter: row.code for (index, row) in df.iterrows()}


def generate_phonetic():
    user_input = input("Choose a name:\n").upper()
    try:
        list_of_codes = [dict_alphabet_words[letter] for letter in user_input]
    except KeyError as error_message:
        print(f"Sorry, but {error_message} is not valid ! ")
        generate_phonetic()
    else:
        print(list_of_codes)


generate_phonetic()
