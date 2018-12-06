Guests = ['freeman','freezeman','fireman','ironman',]

print ('\n')
while len(Guests) > 2:
	kick = Guests.pop()
	print ('Sorry ' + kick +' you can come to my party later, maybe next live.')

print ('\n')
for Guest in Guests:
	print ("Hey, " + Guest )


del Guests[2:]
print (Guests)

print (len (Guests))