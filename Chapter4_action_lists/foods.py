teas = ['Longjing Tea', 'Tieguanyin', 'Da Hong Pao', 'Pu-erh Tea', 'Matcha', 'Sencha', 'Darjeeling Tea', 'Assam Tea']
# print(len(teas))


print(f'The first three items in this list are: {teas[:3]}')
print(f'The last three items in this list are: {teas[-3:]}')
print(f'The items from the middle of the list are: {teas[2:5]}')

other_teas = teas[:]

teas.append('bai tea')
other_teas.append('hei tea')
for tea in teas:
    print('\n',tea.title())
