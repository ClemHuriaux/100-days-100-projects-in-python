PATTERN_TO_REPLACE = "[name]"


with open("Input/Names/invited_names.txt") as f_names:
    names = f_names.read().splitlines()

with open("Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()
    
for name in names:
    new_letter = letter_content.replace(PATTERN_TO_REPLACE, name)
    with open(f"Output/ReadyToSend/letter_for_{name}.txt", "w") as file_to_write:
        file_to_write.write(new_letter)

