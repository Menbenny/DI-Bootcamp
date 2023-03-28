wallet = 300
store_items = {"apple": 50, "banana": 100, "orange": 75, "grape": 150, "pear": 200}

affordable_items = []

for item in store_items:
    if store_items[item] <= wallet:
        affordable_items.append(item)

if affordable_items:
    affordable_items.sort()
    print("You can afford the following items:")
    for item in affordable_items:
        print("- " + item)
else:
    print("Nothing")
