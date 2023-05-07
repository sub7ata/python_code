lst = [(1, 5), (2, 3), (4, 1), (3, 2)]
# sorted_list = sorted(lst, key=lambda x: x[0])
sorted_list = sorted(lst, key=lambda x: x[0], reverse=True)
print(sorted_list)