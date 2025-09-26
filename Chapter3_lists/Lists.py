Names = ['Ruan Yuanke', 'Wang Chenyu', 'Bai Yuce', 'Liu Henyu']
print(Names)
print(Names[2])
print(Names[1].upper())
print(Names[-2])
messages = f'I want to find {Names[1]}!'
print(messages)
Names.append('Yang Hao')
print(Names)

Names.insert(0, 'Liu Quanwei')
print(Names)

Names.append('Zhang Yiwei')
print(Names)

Names_popped = Names.pop()
print(f'I hate {Names_popped}')

Names.sort()
print(Names)

print(sorted(Names, reverse=True))

