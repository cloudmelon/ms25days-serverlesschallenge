# Import the libraries
from datetime import datetime


current_date = datetime.now()

print(current_date)
print('Now is ', str(current_date))
print('Day: ' + str(current_date.day))
print('Month: ' + str(current_date.month))
print('Year : ' + str(current_date.year))

# convert to a date time object

date_for_today = datetime.strftime(current_date,'%d/%m/%y')
print("Today's date is : " + str(date_for_today))