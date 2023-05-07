my_list = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 30},
    {'name': 'Charlie', 'age': 20},
    {'name': 'David', 'age': 35}
]
sorted_list = sorted(my_list, key=lambda x: x['age'])
print(sorted_list)
