Guests = ['freeman','freezeman','fireman','ironman',]

Message = ', i am sorry, there are only two peoples can come.'
print(Guests[2].title()+Message)
print(Guests[1].title()+Message)
print(Guests[0].title()+Message)
print(Guests[3].title()+Message)


Guests.insert( 0,'Tony Starck')
Guests.insert( 2,'Marco')
Guests.append('ironman')
print('\n')

for Guest in Guests:
	print(Guest + Message)


print ('\n')
while len(Guests) > 2:
	kick = Guests.pop()
	print ('Sorry ' + kick +' you can come to my party later, maybe next live.')

print ('\n')
for Guest in Guests:
	print ("Hey, " + Guest + Message)


del Guests[0:]
print (Guests)