def show_magicians(magician_list):
    for magician in magician_list:
        print(magician)

def make_great(magician_list):
    for i in range(len(magician_list)):
        magician_list[i] = "The Great " + magician_list[i]

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']


# print("Original list:")

show_magicians(magician_names)
make_great(magician_names)


print("\nModified list:")
show_magicians(magician_names)