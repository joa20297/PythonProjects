#defines variable
types_of_people = 10
#defines variable as an f-String
x = f"There are {types_of_people} types of people."
# def var with a string (set variable equal to a string - you code the variable but the output will be the string's content)
binary = "binary"
#def var with a string
do_not = "don't"
#sets y's value to an f-string with words and two other variables
y = f"Those who know {binary} and those who {do_not}."
#prints f-string in x variable
print(x)
#prints f-string in y variable
print(y)
#prints f-string with words and inserts the f-string for variable x
print(f"I said: {x}")
#same as in l15
print(f"I also said: '{y}'")
#defines variable/argument as condition false
hilarious = False
#defines variable with text and room for insertion of another argument or variable in {} - BOOLEAN VALUE
joke_evaluation = "Isn't that joke so funny?! {}"
#prints strings in variable joke_evaluation defined by variable hilarious BOOLEAN VALUE
print(joke_evaluation.format(hilarious))
#defines variable with string
w = "This is the left side of..."
#defines variable with string
e = "a string with a right side."
#prints both strings from left to right
print(w + e)
