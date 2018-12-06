Guests = ['freeman','freezeman','fireman','ironman',]

Message = ', can youy come to my party with your family.'
print(Guests[2].title()+Message)
print(Guests[1].title()+', can youy come to my party with your family.')
print(Guests[0].title()+', can youy come to my party with your family.')
print(Guests[3].title()+', can youy come to my party with your family,')

Guests[3] = 'batman'
print(Guests[2].title()+', take your wines plz.')
print(Guests[1].title()+', take your wines plz.')
print(Guests[0].title()+', take your wines plz.')
print(Guests[3].title()+', take your wines plz.')


Guests.insert( 0,'Tony Starck')
Guests.insert( 2,'Marco')
Guests.append('ironman')
print('\n')

for Guest in Guests:
	print(Guest + Message)