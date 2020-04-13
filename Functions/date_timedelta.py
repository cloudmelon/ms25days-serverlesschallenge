from datetime import datetime, timedelta

current_date = datetime.now()

# use timedelta to define a period of time 
one_day = timedelta(days=1)
one_week = timedelta(weeks=1)

yday = current_date - one_day
the_same_date_last_week = current_date - one_week

print('Yesterday was ', str(yday))
print('The same day last week was ', str(the_same_date_last_week))

