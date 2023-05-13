# matrix = [
#     [7, 'T']
#     ['h', 'i']
#     ['s', '$']
#     ['#', '^']
#     ['i', 's']
#     ['%', '']
#     ['M', 'a']
#     ['t', 'r']
#     [3, 'i']
#     ['x', '#']
#     ['', '']
#     ['%', '!']
# ]
matrix = [
    '7i3',
    'Tsi',
    'h%x',
    'i #',
    'sM ',
    '$a ',
    '#t%',
    '^r!'
]
message = ''

for j in range(len(matrix[0])):
    column = ''

    for i in range(len(matrix)):
        column += matrix[i][j]

    alpha_chars = ''
    
    for char in column:
        if char.isalpha():
            alpha_chars += char
    message += alpha_chars 

# def space(message):
#     for char in message:
#         for letter in char:
#             if char == 's':
#                 return " "

# new_message = space(message)
print(message)


            
        
             

