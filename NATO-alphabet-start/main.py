

import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
Nato = {row.letter: row.code for (index, row) in df.iterrows()}
print(Nato)
# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
Nato_user_input = input("Select a word:").upper()

result_word_list = [Nato[nato_word] for nato_word in Nato_user_input]

print(result_word_list)



