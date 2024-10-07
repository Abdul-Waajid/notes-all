#tempra converter 

arg=input('Do you wish to convert celsius to farenhiet? y/n\n') 
if arg =='n':
	argtwo= input('Do you wish to convert farenhiet to celsius? y/n\n')

if arg =='y':
	c = float(input('Please enter value: '))
	print(f'\nYour converted value, from celsius to farenhiet is equal to {(c*(9/5))+32}')
	exit()
elif argtwo=="y":
	f=float(input ('Please enter value: '))
	print(f"\nYour converted valur, from farenhet to celcius is equal to {((f-32)*(5/9))}")
	exit()
else:
	print('No conversion taken place')
exit()
