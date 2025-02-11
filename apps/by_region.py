# -*- coding: utf-8 -*-
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import plotly.plotly as py
import plotly.graph_objs as go

import pandas as pd

from app import app
from .core_app import print_button, get_menu, get_sub_menu

#Define constant of this page
page_id = 'Theo khu vực/vùng miền'
def init():
    global graph_layout, table_layout
    graph_layout = table_layout =[]

graph_layout = html.Div([
    html.Div([
        get_menu (page_id),
        html.H3('Điểm thi tốt nghiệp THPT 2018 theo vùng miền'),
        html.Br([]),
        dcc.Dropdown(
            id='by-region-dropdown',
            options=[
                {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                    'NYC', 'MTL', 'LA'
                ]
            ]
        ),
        html.Div(id='by-region-display-value'),
        html.Br([]),

        get_sub_menu(page_id,'graph'),
        html.Div([
            html.Div("This is graph tab!", className="ui text container")
        ],className= "ui byRegionGraph vertical stripe segment", id="theo-mon-graph"),
    ], className="ui byRegion container")

], className='ui autumn leaf container')

table_layout = html.Div([
    html.Div([
        get_menu (page_id),
        html.H3('Điểm thi tốt nghiệp THPT 2018 theo vùng miền'),
        html.Br([]),
        dcc.Dropdown(
            id='by-region-dropdown',
            options=[
                {'label': 'App 1 - {}'.format(i), 'value': i} for i in [
                    'NYC', 'MTL', 'LA'
                ]
            ]
        ),
        html.Div(id='by-region-display-value'),
        html.Br([]),

        get_sub_menu(page_id,'table'),
        html.Div([
            html.Div("This is table tab!", className="ui text container")
        ],className= "ui byRegionGraph vertical stripe segment", id="theo-mon-graph"),
    ], className="ui byRegion container")

], className='ui autumn leaf container')


@app.callback(
    Output('by-region-display-value', 'children'),
    [Input('by-region-dropdown', 'value')])
def display_value(value):
    return 'You have selected "{}"'.format(value)