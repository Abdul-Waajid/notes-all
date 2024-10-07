#distance converter 

arg=input('Do you wish to convert from meters to kilometers? y/n\n') 
if arg =='n':
	argtwo= input('Do you wish to convert from meters to miles? y/n\n')

if arg =='y':
	m= float(input('Please enter value: '))
	print(f'\nYour converted value, from meters to kilometers is equal to {m/1000}km')
	exit()
elif argtwo=="y":
	m=float(input ('Please enter value: '))
	print(f"\nYour converted value, from meters to miles is equal to {m/1609.34}miles")
	exit()
else:
	print('No conversion taken place')
exit()

