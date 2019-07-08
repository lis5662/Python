class GrumpyDict(dict):
    def __repr__(self):
        print("NONE OF YOUR BUSINESS")
        return super().__repr__()

    def __missing__(self, key):
        print(f"You want {key}? Well it aint here!")

    def __setitem__(self, key, value):
        print("You want to change the dictionary?")
        print("Ok that fine!")
        super().__setitem__(key, value)


data = GrumpyDict({"first": "Tom", "animal": "cat"})
print(data)
data['city'] = 'Tokyo'
print(data)