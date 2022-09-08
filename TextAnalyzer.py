"""Text Analyzer
Write a program that works with a text file. The aim of the program is to read a
text from the text file and analyze it. Specifically it should count and print:
1.the number of words
2.the number of letters
3.the number of sentences
4.the most used letter in a text
5.the most used word in a text
For example if out text file contains this text:
“Hello from Python world”
the program should give the following output:
Words: 4
Letters: 15 (special characters and space are not counted)
Sentences: 1
Letter frequency: o (both o and l are used 3 times so any of the letters is
considered as a right answer)
Word frequency: 0 (there is no word that is used more than once)
The result should be kept in a separate text file."""


print("Enter your file path(absolute)\n")
file = input()
with open(f'{file}') as data:
    text = data.read()
    sentences = text.count('.') + text.count('?') + text.count('!')
    text = text.split()
    words = len(text)
    words_count = {}
    letters_count = {}
    letters = 0
    for i in text:
        if not i[-1].isalpha():
            i = i[:len(i)-1]
        words_count[i] = words_count.get(i, 0) + 1
        for j in i:
            if j.isalpha():
                letters_count[j] = letters_count.get(j, 0) + 1
                letters += 1
    words_count_reverse = dict([val, key] for key, val in words_count.items())
    max_word = max(words_count_reverse.keys())

    letters_count_reverse = dict([val, key] for key, val in letters_count.items())
    max_letter = max(letters_count_reverse.keys())

with open('file_analyzer', 'w') as new_file:
    new_file.write('1.the number of words -> ' + f'{words}' + '\n')
    new_file.write('2.the number of letters -> ' + f'{letters}' + '\n')
    new_file.write('3.the number of sentences -> ' + f'{sentences}' + '\n')
    new_file.write('4.the most used letter in a text -> ' + f'{letters_count_reverse[max_letter]}' + '\n')
    new_file.write('5.the most used word in a text -> ' + f'{words_count_reverse[max_word]}' + '\n')
