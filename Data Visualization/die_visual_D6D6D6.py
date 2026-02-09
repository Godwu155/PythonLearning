from die import Die
import plotly.express as px



die = Die()

results = []
for roll_num in range(10000):
    result =die.roll() + die.roll() + die.roll()
    results.append(result)

max_value = die.num_sides + die.num_sides + die.num_sides
poss_values = range(3, max_value)
frequencies = [results.count(value) for value in poss_values]

title = 'The Frequency of Three D6 rolling.'
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_values, y=frequencies, title = title, labels = labels)
fig.show()
