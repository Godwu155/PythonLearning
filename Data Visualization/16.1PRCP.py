from pathlib import Path
import matplotlib.pyplot as plt
import csv
from datetime import datetime

def get_weather_data(path, dates, prcps, date_index, prcp_index) ->None:
    lines = path.read_text().splitlines()
    reader = csv.reader(lines)
    header_row = next(reader)

    for row in reader:
        current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
        try:
            prcp = float(row[prcp_index])
        except ValueError:
            print(f'Error data for {current_date}')
        else:
            dates.append(current_date)
            prcps.append(prcp)


path = Path('weather_data/sitka_weather_2021_full.csv')
dates, prcps = [], []
get_weather_data(path, dates, prcps, 2, 5)

fig, ax = plt.subplots()
ax.bar(dates, prcps, color='blue')
# ax.set_xticks(dates)

ax.set_xlabel(' ',fontsize=16)
ax.set_ylabel('PRCP(mm)',fontsize=16)
fig.autofmt_xdate()
ax.set_title("Stika_PRCP",fontsize=24)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()