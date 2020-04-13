# Input a number
num = float(input('What is your number of donated toys ?'))

if num < 1.00:
    note = .02   #number 4 spaces, can also written as note = 0.07
  
elif num >= 1.00 and num < 5:
    note = .07 
elif num >= 5:
    note = 0.9
else :
    note = 0
print(note)