admin_list = ['den', 'cicada']
print(admin_list)
far = input('Name:  ')

if far in admin_list:
    print('ok')
else:
    print('non')

player = input('ADD:    ')

admin_list.append(player)
print(admin_list)