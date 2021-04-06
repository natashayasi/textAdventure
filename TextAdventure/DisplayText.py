# A function to display the text in text file of the passed in name
# Prints text file line by line

# Input: name of text file (minus .txt)
# Output: text of file to console

# Requirements: file must be located in "Text Files" folder,
#               which must be in same folder as program

def displayText(name):
    textfile = "./Text Files/" + name + ".txt"
    with open(textfile) as f:
        for line in f:
            print(line)

