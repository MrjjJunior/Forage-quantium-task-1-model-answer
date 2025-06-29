from  dash import Dash, html, dash_table, dcc, callback, Output, Input
import plotly.express as px # datavisualization library
import pandas as pd     # data manipulation library
import csv
'''
dcc : Dash Core Components
html: HTML components
'''

dataframe = pd.read_csv('history_pink_morsel.csv')

def filter_region(file_name):
    with open('combined.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        
        with open(file_name + '.csv', mode="w") as east_file:
            east_writer = csv.writer(east_file)

            for line in csv_reader:
                if file_name in line:
                    east_writer.writerow(line)

filter_region('north')
filter_region('south')
filter_region('east')
filter_region('west')


app = Dash()

app.layout = [  # components are displayed in here, they are provided as a list
    html.H1("Pink Morsek Sales Histor", style={'textAlign': 'center'}), # Heading of graph
    html.Hr(), # horizontal line
    dash_table.DataTable(data=dataframe.to_dict('records'), page_size=10),
    html.Hr(),
    dcc.RadioItems(options=['sale','east'], value='sale', id='controls-and-radio-item', style={'textAlign': 'center'}),

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