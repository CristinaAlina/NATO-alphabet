import pandas

INPUT_FILE = "nato_phonetic_alphabet.csv"

# Create a dictionary containing the data from csv file:
all_data = pandas.read_csv(INPUT_FILE)
dict_nato_alphabet = {row.letter: row.code for (index, row) in all_data.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
input_word = (input("Enter a word: ")).upper()
output_list = [dict_nato_alphabet[letter] for letter in input_word]

print(output_list)
