sample_input = input('what is your impression on our world ?')
sample_str = 'Hello ' + sample_input +' world'

print(sample_str.upper())
print(sample_str.lower())
print(sample_str.capitalize())
print(sample_str.count('o'))

print(sample_str + ' ' \
    + sample_str.upper() + '!')
