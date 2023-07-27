import pyinputplus as pyip

bread_type = {
    'white':2,
    'wheat':2.5,
    'sourdough':4
}
protein_type = {
    'chicken':4,
    'turkey':5,
    'ham':3.5,
    'tofu':3.5
}
cheese_type = {
    'cheddar':2,
    'Swiss':2.5,
    'mozzarella':2,
    'no cheese':0
}
topping_type = {
    'mayo':1,
    'mustard':1,
    'lettuce':1.5,
    'tomato':1.5,
    'no topping':0
}

print(bread_type['sourdough'])

chosen_bread = pyip.inputMenu(list(bread_type.keys()))
chosen_protein = pyip.inputMenu(list(protein_type.keys()))
if_cheese = pyip.inputYesNo('Do ya want some cheese with that?')
if if_cheese == 'yes':
    chosen_cheese = pyip.inputMenu(list(cheese_type.keys()))
else:
    chosen_cheese = 'no cheese'
if_topping = pyip.inputYesNo('Do ya want some topping?')
if if_topping == 'yes':
    chosen_topping = pyip.inputMenu(list(topping_type.keys()))
else:
    chosen_topping = 'no topping'
no_of_sandwitches = pyip.inputNum('How many sandwitches do ya want?',min=1)

to_pay = (bread_type[chosen_bread]+protein_type[chosen_protein]+cheese_type[chosen_cheese]+topping_type[chosen_topping])*no_of_sandwitches

print("Alright, here's your {4} sandwitch(es) with:{0},{1},{2},{3}.\nYour total is {5}$ ".format(chosen_bread,chosen_protein,chosen_cheese,chosen_topping,no_of_sandwitches,to_pay))