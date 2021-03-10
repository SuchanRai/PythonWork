# Given the integers N - the number of minutes that is passed since midnight - how many hours and minutes are
# displayed on the 24h digit clock?
# The program should print two numbers :the number of hours (between 0 and 23).
# and the numbers of minutes (between 0 and 59).
# For example , if N= 150 then 150 minutes have passed since midnight - i.e now is 2:30 am.
# so, the program should print 2:30.
N = int(input('enter the minutes:'))
hours = int((N/60))
minutes = (N % 60)
print(f'the value in hours is {hours}')
print(f'the value in minutes is {minutes}')
print(f'{hours}:{minutes}')