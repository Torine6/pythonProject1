# sequential control
print('Hello')
print('How are you?')
print('Welcome to Lux Tech Academy.')
# if-else statement
value = int(input('Enter integer value: '))
if value < 10:
    print('The value entered is less than 10.')
else:
    print('The value entered is greater than 10.')
# iterative control
i = 0
while i <= 10:
    print(i)
    i += 1
# simple if statement
temperature = 35
if temperature > 30:
    print('It is a hot day')
# nested if statement
num_1 = float(input('Enter a number: '))
if num_1 >= 0:
    if num_1 == 0:
        print('Number is zero.')
    else:
        print('Number is positive.')
else:
    print('Number is negative')
# if-elif-else statement
temperature = 19
if temperature > 35:
    print('It is a hot day.')
elif temperature > 20:
    print('It is a good day.')
else:
    print('Enjoy your day!')


# functions
def cube(number):
    return number * number * number


print(cube(5))
