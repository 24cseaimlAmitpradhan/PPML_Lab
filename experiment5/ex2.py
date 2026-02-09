
my_list = ['apple', 'banana', 'cherry', 'mango']
print("Looping over a List:")
for element in my_list:
    print(element)
print("-" * 20)
my_tuple = (10, 20, 30, 40)
print("Looping over a Tuple:")
for element in my_tuple:
    print(element)
print("-" * 20)
my_set = {'red', 'green', 'blue', 'yellow'}
print("Looping over a Set:")
for element in my_set:
    print(element)
print("-" * 20)
my_dict = {
    'name': 'Amit',
    'age': 19,
    'city': 'khallikote'
}

print("Looping over a Dictionary (keys):")
for key in my_dict:
    print(key)
print("-" * 20)

print("Looping over a Dictionary (values):")
for value in my_dict.values():
    print(value)
print("-" * 20)

print("Looping over a Dictionary (key-value pairs):")
for key, value in my_dict.items():
    print(f"{key}: {value}")
print("-" * 20)
