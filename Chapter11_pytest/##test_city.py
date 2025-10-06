from city_function import city

def test_city():
    formatted_city = city('Beijing', 'China','20000')
    assert formatted_city == 'Beijing, China, 20000'