favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

friends = {'phil', 'sarah'}
for name in favourite_languages.keys():
    print(f"Hi {name.title()}!")

    if name in friends:
        language = favourite_languages[name].title()
        print(f"\t{name.title()} ,I see you like {language}!")

Dic1 = {'name': 'AAA',
        'age': '10',
        'location': 'NYC',
        'country': 'USA'
        }

Dic2 = {
    'name': 'BBB',
    'age': '11',
    'location': 'NYC',
    'country': 'USA'
}
Dic3 = {
    'name': 'CCC',
    'age': '12',
    'location': 'NYC',

    'country': 'USA'
}

Dic = [Dic1, Dic2, Dic3]
for item in Dic:
    print(item.keys())


set = {
    
}

print()