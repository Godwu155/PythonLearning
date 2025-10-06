from name_function import get_formatted_name

def test_name():
    formatted_name = get_formatted_name('John', 'Doe')
    assert formatted_name == 'JohnDoe'