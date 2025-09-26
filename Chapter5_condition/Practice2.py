current_users = ['admin', 'trump', 'alen', 'jaden', 'alex']
new_users = ['bob','john','steve','alen','alex']
current_users_fuben = ['admin', 'trump', 'alen', 'jaden', 'alex']


for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Your name'{new_user}' has been already taken,please type a name new.")

    else:
        print('Your name is OK.')
        current_users_fuben.append(new_user.lower())

print(current_users_fuben)