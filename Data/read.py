#creating the function to display character
def display_chars(file_path, num_chars):
#Open file and close file
    with open(file_path) as file:
#Read the file and close the file
        data = file.read(num_chars)
        print("The first 5 character is:","\n",data)
def display_line(file_path):
# Open and close file
    with open(file_path) as file:
#Read a line in the text
        data = file.readline()
        print("The first line is:","\n",data)
def display_text(file_path):
# Open and close file
    with open(file_path) as file:
#Read the full text
        data = file.read()
        print("The full text is:","\n",data)
#run the functions
def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")
#Run the program
if __name__ == "__main__":
    run()