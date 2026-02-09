from pathlib import Path
import csv
import matplotlib.pyplot as plt
from datetime import datetime

path = Path('weather_data/sitka_weather_2021_simple.csv')
lines = path.read_text().splitlines()

# print(lines)
reader = csv.reader(lines)
header_row = next(reader)
print(reader)
print(header_row)

for index, column_header in enumerate(header_row):
    print(index, column_header)

sign_num = int(input('Chose number: '))

dates, highs, lows= [], [], []
if sign_num == 1:
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        if current_date.year == 2021 and current_date.month == 5 :
            try:
                high = int(row[4])
                low = int(row[5])
            except ValueError:
                print(f'Missing data for {current_date}')
            else:
                dates.append(current_date)
                highs.append(high)
                lows.append(low)

else:
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)


print(highs)
print(dates)
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates,highs,color='red')
ax.plot(dates,lows,color='blue')
ax.fill_between(dates,highs,lows,facecolor='blue', alpha=0.2)

ax.set_xlabel(' ',fontsize=16)
ax.set_ylabel('Temperature(F)',fontsize=16)
fig.autofmt_xdate()
ax.set_title("Daily High and Low Temperatures, July 2021",fontsize=24)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()