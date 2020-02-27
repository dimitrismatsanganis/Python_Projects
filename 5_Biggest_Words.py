#Write a program in Python that finds the five largest words of a text that reads from a file and
#prints upside down, having the vowels removed, firstly.

#Read file.
f = open(text.txt, r)
text = f.read()
f.close()

#Remove all the punctuation marks.
punctuation_marks = [., ,, !, , (, ), [, ], ;, ']
text_unmarked = 
for letter in text
    if letter not in punctuation_marks
        text_unmarked += letter

#Creation of a list of lists, where the first elemnnt of the sublist is every word,
#while the second element is the length of each word.
words = text_unmarked.split( )
words_lengths = []
for word in words
    item = [len(word), word]
    words_lengths.append(item)

#Sort.
words_lengths.sort()

#Getting the 5 biggest words
max = []
for i in range(1,6)
    max.append(words_lengths[-i][1])


#Remove the vowels and reversing the words' order.
vowels = [a, e, i, o, u, y]
max_rearranged = [, , , , ]
for word in range(len(max))
    tmp = 
    for letter in max[word]
        if letter not in vowels
            tmp += letter
    max_rearranged[word] = tmp[-1]
    
#Print the results.
print(Largest words+str(max)+n+Reversed+str(max_rearranged))