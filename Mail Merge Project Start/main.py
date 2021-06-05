# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".
#
# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
#     Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#         Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


with open("Input/Names/invited_names.txt", "r") as file:
    lines = file.readlines()
    clean_line = []
    for line in lines:
        line = line.rstrip("\n")
        clean_line.append(line)

with open("./Input/Letters/starting_letter.txt", "r") as file:
    content = file.readlines(1)
    print(content[0])
    new_names_list = []
for line in clean_line:
    new_content = content[0].replace("[Name]", line)
    new_names_list.append(new_content)

dear_name = []
for line in new_names_list:
    line = line.rstrip("\n")
    dear_name.append(line)

print(dear_name)
file_name_list = []
for name in clean_line:
    file_name = f'Output/ReadyToSend/{name}.txt'
    file_name_list.append(file_name)

print(file_name_list)

for i in range(len(file_name_list)):
    with open(file_name_list[i], "w") as f:
        f.write(dear_name[i])
        f.write("\n")
        f.write("You are invited to my birthday this Saturday.\n")
        f.write("Hope you can make it!\n")
        f.write("Mouad")

