# write a python program to convert seconds to day, hour, minute, and seconds\
time = int(input('='))
day = int(time / 86400)
hours = int(((time-(day*86400))/60)/60)
minutes = int((time - (day*86400)-(hours*60*60))/60)
seconds = time - (day*86400) - (hours*60*60) - (minutes*60)
print(f'{day}days:{hours}hrs:{minutes}min:{seconds}sec')