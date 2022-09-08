# Python 3.8
# Dependencies [re]


import re

# Regex for line starting with //
regex_1 = r"\A\/\/"

# Regex for line starting with /*
regex_2 = r"\A\/\*"

# Regex for line starting with */
regex_3 = r"\A\*\/"


# regex_4 = r"[\t\s]\/\*[\s\S]*?\*\/[\s\S\t]"

#Creating variable for storing text
comment = ""
code_base = ""
# Reading .txt file
f = open("1_Program.txt", "rt")

Lines = f.readlines()

#Flags
trigger = False
iscode = True

# Strips the newline character
for line in Lines:

    # for printing line starting with "//"
    if re.search(regex_1, line.strip(), re.DOTALL):
        comment = comment + line.strip() + "\n"
        iscode = False
        continue

    # for printing line starting with "/*"
    if re.search(regex_2, line.strip(), re.DOTALL):
        comment = comment + line.strip() + "\n"
        trigger = True
        iscode = False
        continue

    # for printing line   "*/"
    if re.search(regex_3, line.strip(), re.DOTALL):
        trigger = False
        iscode = False
        comment = comment + line.strip() + "\n"
        continue
    # for printing line after  "/*"
    if trigger:
        comment = comment + line.strip() + "\n"
        iscode = False

    elif iscode == True or trigger == False:
        code_base = code_base + line.strip() + "\n"

print(comment)
print("Codebase=" + code_base)

# write Comment.txt output file
with open('problem1_comment_output.txt', 'w') as f:
    for line in comment:
        f.write(line)

# write Code.txt output file
with open('problem1_code_output.txt', 'w') as f:
    for line in code_base:
        f.write(line)

