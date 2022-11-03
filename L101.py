#the authors' name are: Holly, Haley and Anna

sizes= {"shoe":7, "shirt": "small", "pants": 4, "ring": 6}

def my_get_method (dictionary,key,default):
    if key in dictionary:
        print(dictionary[key])
    else:
        return default

my_get_method(sizes, "shoe", 10)

my_get_method(sizes, "shirt", "large")

my_get_method(sizes, "pants", "large")

my_get_method(sizes, "ring", False )
