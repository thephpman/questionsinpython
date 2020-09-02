# What is function in python ?

# How to define a function in python

# What is the structure of passing data to a function

# What a function return when i pass some value to it ?

# What is the fuction syntex ?

# What can i pass to a fuction ?

person1 = "Jamil"
person2 = "kamil"
person3 = 12345

persontype1 = "Human"
persontype2 = "Shel Fish"
persontype3 = 3333333

contain_digit = True

def custom_Function(name, type):
    if name.isnumeric() == contain_digit:
        # Returning the value that its a number,
        # Name can not be a number
        return "The name contain number"
    else:
        return "Name is passed"
    if type.isnumeric() == contain_digit:
        return "The type also contain number please check the inputed data"
    else:
        return "Type is passed"

check_names = custom_Function(person1, persontype1)

print(check_names)
