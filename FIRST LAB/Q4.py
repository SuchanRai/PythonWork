# N students take K apples and distribute them among each other evenly. The remaining (the undivisible)
# part remains in the basket. how many apples will each single student get? how many apples will remains in the basket
# the program reads the numbers N and K. It should print the two answers for the queation above

number_of_student = int(input('enter the total number of students:'))
number_of_apples = int(input('enter the total number of apples:'))
divisible_apples = number_of_apples/number_of_student
remaining_apples = (number_of_apples%number_of_student)
print(f'each student got {divisible_apples}')
print(f'the remaining apples are {remaining_apples} ')