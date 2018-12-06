person_age = range(1,101)
for age in person_age:
	if age < 2:
		print('baby')
	else:
		if age >=2 and age <4:
			print('toddler')
		else:
			if age >=4 and age <13:
				print('kid')
			else:
				if age >=13 and age <20:
					print('teens')
				else:
					if age >=20 and age <65:
						print('an adult')
					else:
						print('elder')


