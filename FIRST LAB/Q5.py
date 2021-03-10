# A school decided to replace the desks in three classrooms. Each desks sits two students. Given the number of students
# In each class, print the smallest [possible number of desks that can be purchased.
# the program should read the three integers: the number of student in each of the three classes a,b and c respectly
# in the first test there are three groups. the first group has 20 students thus needs 10  desks . the second desk
# the second group has 21 student , so they can get by with no fewer than 11 desks .
# 11 desks are also enough for the third group of 22 students. so, we need 32 desks in total .
std1 = int(input('enter the number of std.:'))
std2 = int(input('enter the number of std.:'))
std3 = int(input('enter the number of std.:'))
desk1 = (std1//2)
print(f'the number of desk required is {desk1}')
desk2 = (std1//2)
print(f'the number of desk required is {desk2}')
desk3 = (std1//2)
print(f'the number of desk required is {desk3}')
total = desk3+desk2+desk1