word = input("Please enter a word: ")
letter_dict = {}

for i in range(len(word)):
    
    letter = word[i]
    if letter not in letter_dict:
        
        letter_dict[letter] = []
    letter_dict[letter].append(i)
    

print(letter_dict)

