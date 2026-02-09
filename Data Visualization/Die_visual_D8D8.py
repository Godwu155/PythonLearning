from die import Die
import plotly.express as px

die = Die(8)

results = []
for roll_no in range(10000):
    result = die.roll() * die.roll()
    results.append(result)


max_value = die.num_sides * die.num_sides
poss_value = range(1,max_value)
frequencies = [results.count(value) for value in poss_value]




title = 'D8 * D8'
labels = {'x':'value', 'y':'Frequency of values'}
fig = px.bar(x=poss_value, y=frequencies, barmode='group', title=title, labels=labels)
fig.show()