numbers = ['231343','345241','452342','235453',]

Message = ', 9872439529857,3462,.543634,3456,.'
print(numbers[2].title()+Message)
print(numbers[1].title()+Message)
print(numbers[0].title()+Message)
print(numbers[3].title()+Message)


numbers.insert( 0,'2436666')
numbers.insert( 2,'3454444')
numbers.append('3567785435675')
print('\n')

for number in numbers:
	print(number + Message)


print ('\n')
while len(numbers) > 2:
	kick = numbers.pop()
	print ('4564564..45644,56.46,564 ' + kick +' 3456.3456.345.6465666.4654.456.')

print ('\n')
for number in numbers:
	print ("4564567547, " + number + Message)


del numbers[2:]
print (numbers)
print (len (numbers))

black = sorted(numbers)
print (black)
white = sorted(numbers,reverse=True)
print (white)
biue = sorted(numbers,reverse=False)
print (biue)