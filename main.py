import pandas

INPUT_FILE = "nato_phonetic_alphabet.csv"

# Create a dictionary containing the data from csv file:
all_data = pandas.read_csv(INPUT_FILE)
dict_nato_alphabet = {row.letter: row.code for (index, row) in all_data.iterrows()}


def generate_phonetic():
    """Creates a list of the phonetic codes from a word that the user inputs."""
    input_word = input("Enter a word: ").upper()
    try:
        output_list = [dict_nato_alphabet[letter] for letter in input_word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)


generate_phonetic()
