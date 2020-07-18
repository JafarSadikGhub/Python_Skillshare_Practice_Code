

def word_count(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()

    except FileNotFoundError:
        message = "Sorry, the file " + filename + " cannot be found."
        print(message)
        """To show end users no error, just write "pass" to this block and 
        erase the above 2 lines of codes"""

    else:
        words = contents.split()
        number_words = len(words)
        print("The file " + filename + " has approximately " + str(number_words) + " words.")

filename = ['C:\\Users\\USER\\Desktop\\Python_Skillshare_Code_Repo\\files\\heathcliff.txt','C:\\Users\\USER\\Desktop\\Python_Skillshare_Code_Repo\\files\\mobydick.txt']

for file in filename:
    word_count(file)