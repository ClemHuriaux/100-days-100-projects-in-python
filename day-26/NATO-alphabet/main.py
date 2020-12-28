import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")
dict_alphabet_words = {row.letter: row.code for (index, row) in df.iterrows()}


user_input = input("Choose a name:\n").upper()
list_of_codes = [dict_alphabet_words[letter] for letter in user_input]
print(list_of_codes)
