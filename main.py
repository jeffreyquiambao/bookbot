path_to_frankenstein = 'books/frankenstein.txt'
with open(path_to_frankenstein) as f:
    file_content_string = f.read()

# function that takes text from the book as a string, and returns the number of words
def count_words(book):
    words = book.split()
    return len(words)

# takes text from the book as a string, and returns the number of tiems each character appears in the string. Convert any uppercase letters to lowercase, we don't want duplicates
def word_counter(text):
    # create a list of strings for each word in the text
    text = text.lower().split()
    character_count_dict = {}

    # go through each word individually 
    for word in text:
    # for each word, go through each character individually
        for char in word:
            # check if character exists in dictionary
            char_exists_in_dictionary = char in character_count_dict
            # if it exists in dictionary, increase count by 1
            if(char_exists_in_dictionary):
                character_count_dict[char] += 1
            # if it doesn't exist in dictionary, instantiate count of 1
            else:
                character_count_dict[char] = 1

    return character_count_dict


def generate_report(text, text_path):
    print(f"--- Begin report of {text_path} ---")
    print(f"{count_words(text)} word found in the document")
    print("")
    
    char_count_dict = word_counter(text)
    char_list = list(char_count_dict.keys())
    alpha_list = [char for char in char_list if char.isalpha()]
    alpha_list.sort()
    
    for letter in alpha_list:
        print(f"The '{letter}' character was found {char_count_dict[letter]} times")

    print("--- End report ---")

generate_report(file_content_string, path_to_frankenstein)