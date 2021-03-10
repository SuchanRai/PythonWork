# You live 4 miles from the university . the bus drives at 25mph but spends 2 minutes at each of the 10 stops onthe way
# How long will the bus journey take ? alternstive, you could run to university. you jog the first mile at 7mph
# then run the next two at 15mph ; before
living_miles = 4
drives = 25
time = (living_miles/drives) * 68
time_spend= 28
total_time = time+time_spend
print(f'total time taken by bus is {total_time}')
jog_one= ((1/7)*60)
jog_two = ((2/15) * 60)
jog_three = ((1/7)*60)
total_walk_time = jog_three+jog_one+jog_two
print(f'time taken by running is {total_walk_time}')
if (total_time>total_walk_time):
    print('taking bus is slower than running !!')
else:
    print(f'time taken by bus is quicker!!')

