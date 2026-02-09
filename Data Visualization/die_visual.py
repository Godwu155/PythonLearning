from die import Die
import plotly.express as px



die = Die()
results = []
for roll_num in range(10000):
    result = die.roll()
    results.append(result)

frequencies = []
poss_results = range(1,die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

fig = px.bar(x=poss_results, y=frequencies,title="Result")
fig.update_layout(xaxis_tickangle=1)
fig.show()

