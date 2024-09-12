'''
create a program file including the data ,find total number of digits,symbols,first letter start with a ,upper 
letters,total number of words and sentence
'''
import string


def is_symbol(char):
    return char in string.punctuation


def main_text(my_file):
    with open(my_file, 'r') as file:
        data = file.read()

   
    digit_count = 0
    symbol_count = 0
    uppercase_start_count = 0
    word_count = 0
    sentence_count = 0

    
    words = data.split()
    sentences = data.split('.')

    
    for word in words:
        if word[0].isupper():
            uppercase_start_count += 1
        word_count += 1
        for char in word:
            if char.isdigit():
                digit_count += 1
            if is_symbol(char):
                symbol_count += 1

   
    sentence_count = len(sentences) - 1

  
    print(f"Total number of digits: {digit_count}")
    print(f"Total number of symbols: {symbol_count}")
    print(f"Number of words starting with uppercase letters: {uppercase_start_count}")
    print(f"Total number of words: {word_count}")
    print(f"Total number of sentences: {sentence_count}")


file_path = 'my_file.txt' 
main_text(file_path)