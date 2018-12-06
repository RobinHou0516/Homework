current_users = ['kakaxi','mingren','zuozu','wadaxi','nalutuo']
new_users = ['laozi','mingren','flihai','gd','wadaxi']


for new_user in new_users:
	if new_user.upper() in current_users:
		print('please enter a new username')
	elif new_user.lower() in current_users:
		print('please enter a new username')
	elif new_user.title() in current_users:
		print('please enter a new username')
	else:
		print('the username is available')
