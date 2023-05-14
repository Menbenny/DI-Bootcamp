# unsorted_str = "without,hello,bag,world"

# def sorted_str():
#     unsorted_str = sorted("a-z")
#     return sorted_str

# print(sorted_str)

user_input = input("Enter a comma-separated sequence of words: ")

words = user_input.split(",")
words.sort()
sorted_words = ",".join(words)

print(sorted_words)