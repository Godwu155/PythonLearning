import collections

from die import Die
import plotly.express as px

die1 = Die()
die2 = Die(10)

results =[]
for roll_no in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)


frequencies = []
max_result = die1.num_sides + die2.num_sides
poss_results = range(2, max_result + 1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)

title = 'Result of rolling D6&D10 Dice 1,000 Times'
label = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=label)
fig.update_layout(xaxis_tickangle=1)
fig.show()
fig.write_html('D6D10.html')


