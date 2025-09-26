Users = ['admin', 'trump', 'alen', 'jaden', 'alex']
# Users = []
# for user in Users:
#     if user == 'admin':
#         print('Hello admin,would you like to see status report?')
#
#     else:
#         print('Hello ' + user + ',thank you for logging in again.')


if Users:
    for user in Users:
        if user == 'admin':
            print('Hello admin,would you like to see status report?')

        else:
            print('Hello ' + user + ',thank you for logging in again.')

else:
    print('We need some users.')

