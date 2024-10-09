
with open("Day 21- File Handeling/Mail Merge Project/Input/Names/invited_names.txt", "r") as names_file:
    names = names_file.readlines()

with open("Day 21- File Handeling/Mail Merge Project/Input/Letters/starting_letter.txt", "r") as letter_file:
    letter_template = letter_file.read()

for name in names:
    stripped_name = name.strip()
    new_letter = letter_template.replace("[name]", stripped_name)
    
    output_filename = f"Day 21- File Handeling/Mail Merge Project/Output/ReadyToSend/letter_for_{stripped_name}.txt"
    
    with open(output_filename, "w") as output_file:
        output_file.write(new_letter)

print("Letters created successfully")