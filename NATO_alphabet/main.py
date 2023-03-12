import pandas

# reading database
data = pandas.read_csv("nato_phonetic_alphabet.csv")
pandas.DataFrame(data)

# turning database into dictionary
alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

# making a list of words according to the given input
word = input("Give a word that you want to be represented by the NATO alphabet: ").upper()
phonetic = [alphabet[letter] for letter in word]
print(f"Represented by NATO alphabet: {phonetic}", sep=", ")
