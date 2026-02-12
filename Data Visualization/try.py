from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd
import json
from pathlib import Path

# --- 数据处理 ---
path = Path('weather_data/readable_eq_data.geojson')
all_eq_data = json.loads(path.read_text(encoding='utf-8'))
all_eq_dicts = all_eq_data['features']

data = pd.DataFrame([
    {
        'mag': eq['properties']['mag'],
        'title': eq['properties']['title'],
        'lon': eq['geometry']['coordinates'][0],
        'lat': eq['geometry']['coordinates'][1]
    } for eq in all_eq_dicts
])

app = Dash(__name__)

# --- 页面布局 ---
app.layout = html.Div(style={
    'display': 'flex',
    'flexDirection': 'row',  # 左右排列
    'height': '100vh',  # 占满屏幕高度
    'fontFamily': 'sans-serif'
}, children=[

    # 左侧控制面板 (占 20% 宽度)
    html.Div(style={
        'width': '20%',
        'padding': '20px',
        'backgroundColor': '#f8f9fa',
        'borderRight': '1px solid #ddd'
    }, children=[
        html.H2("控制面板", style={'fontSize': '20px'}),
        html.Hr(),
        html.P("筛选最低震级:"),
        dcc.Slider(
            id='mag-slider',
            min=0, max=9, step=0.1, value=4,
            marks={i: str(i) for i in range(10)},
            included=True
        ),
        html.Div(id='slider-output-container', style={'marginTop': '20px', 'color': '#666'})
    ]),

    # 右侧图表区域 (占 80% 宽度)
    html.Div(style={'width': '80%', 'padding': '10px'}, children=[
        html.H1(all_eq_data['metadata']['title'], style={'textAlign': 'center', 'fontSize': '24px'}),
        dcc.Graph(
            id='earthquake-map',
            style={'height': '85vh'}  # 地图高度占屏幕 85%
        )
    ])
])


# --- 回调逻辑 ---
@app.callback(
    [Output('earthquake-map', 'figure'),
     Output('slider-output-container', 'children')],
    [Input('mag-slider', 'value')]
)
def update_map(min_mag):
    filtered_df = data[data['mag'] >= min_mag]

    fig = px.scatter_geo(
        filtered_df,
        lat='lat', lon='lon',
        size='mag', color='mag',
        hover_name='title',
        range_color=[0, 8],
        projection="orthographic",
        template="plotly_dark"  # 使用深色主题，地图会显得更高级
    )

    # 稍微优化一下地图边距
    fig.update_layout(margin={"r": 0, "t": 40, "l": 0, "b": 0})

    status_text = f"当前显示: {len(filtered_df)} 个地震点"
    return fig, status_text


if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
    # fig.write_html("C:/Users/ROG/Desktop/eq.html")
