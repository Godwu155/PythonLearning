from pathlib import Path
import json
import plotly.express as px
import pandas as pd

path = Path('weather_data/readable_eq_data.geojson')
# path = Path('weather_data/readable_eq_data.json')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# path = Path('weather_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    title = eq_dict['properties']['title']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(titles[:10])
print(lons[:10])
print(lats[:10])

data = pd.DataFrame(
    data=zip(lons, lats, titles, mags),columns=['lon', 'lat', 'title', 'mag']
)
data.head()

fig = px.scatter_geo(
    data,
    lat='lat',  # 对应纬度列表
    lon='lon',  # 对应经度列表
    size='mag',  # (可选) 根据震级决定点的大小
    color='mag',  # (可选) 根据震级决定点的颜色
    hover_name='title',  # (可选) 鼠标悬停时显示地震标题
    range_color=[0, 8],  # (可选) 设置颜色条的范围，比如0到8级
    title=all_eq_data['metadata']['title'],
    projection="orthographic",  # 地图投影方式，让地图看起来更自然

)
fig.write_html('weather_data/readable_eq_data.html')
fig.show()
