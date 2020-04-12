your_greetings = 'Hello'
your_name = 'cloudmelon'

str_output = 'hello,{0} {1}'.format(your_greetings, your_name)

# Below is only working in Python 3
str_output_py3 = f'{your_greetings} {your_name}'

print(str_output)
print('In Python 3 : ', str_output_py3)