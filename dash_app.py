from  dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px # datavisualization library
import pandas as pd     # data manipulation library
'''
dcc : Dash Core Components
html: HTML components
'''

dataframe = pd.read_csv('history_pink_morsel.csv')

app = Dash()

app.layout = [  # components are displayed in here, they are provided as a list
    html.H1("Pink Morsek Sales Histor", style={'textAlign': 'center'}), # Heading of graph
    html.Hr(), # horizontal line
    dcc.RadioItems(options=['sale','date','region'], value='sale', id='controls-and-radio-item'),
    dash_table.DataTable(data=dataframe.to_dict('records'), page_size=10),
    html.Hr(),
    #dcc.Graph(figure=px.line(dataframe, x='date', y='sale', title='Pink Morsel Sales Over Time')), 
    dcc.Graph(figure={}, id='controls-and-graph')
]

@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='controls-and-radio-item', component_property='value')
)

def update_graph(col_chosen):
    fig = px.line(dataframe, x='date', y=col_chosen, title='Pink Morsel Sales Over Time')
    return fig

if __name__ == '__main__':
    app.run(debug=True)