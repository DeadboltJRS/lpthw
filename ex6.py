types_of_people = 10
x = f"There are {types_of_people} types of people."
#one instance of s/s
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
#2nd instnace of s/s
print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
#3rd instance of s/s
print(joke_evaluation.format(hilarious))
#4th instance of s/s .format is used for when a variable is already inside another string
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
# using a + to ad the variables 'w' and 'e'that add two variables together rather than creathing two strings
