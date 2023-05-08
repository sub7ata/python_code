lst_no = [1,2,3]
lst_name = ['ABC', 'BCA', 'CAB']
print(dict(zip(lst_name, lst_no)))

zip_data = list(zip(lst_name, lst_no))
print(zip_data)

a,b = zip(*zip_data)
print(a)
print(b)


fields = ['name', 'last_name', 'age', 'job']
values = ['John', 'Doe', '45', 'Python Developer']
a_dict = dict(zip(fields, values))
print(a_dict)

new_job = ['Python Consultant']
field = ['job']
a_dict.update(zip(field, new_job))
print(a_dict)