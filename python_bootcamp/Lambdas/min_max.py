names = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(min(len(name) for name in names))

print(max(names, key=lambda n: len(n)))
