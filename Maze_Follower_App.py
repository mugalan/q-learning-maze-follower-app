import dash
from dash import Dash,html,dcc,Input,Output,State,ctx
import dash_bootstrap_components as dbc

import plotly.graph_objects as go

import numpy as np



Maze_Follower_App = Dash(
    __name__,
    external_stylesheets = [
        dbc.themes.BOOTSTRAP
    ]
)



maze = go.Figure()

maze.update_layout(
    font = dict(
        family = 'Bahnschrift'
    ),
    grid = dict(
        columns = 1,
        rows = 1
    ),
    hovermode = 'closest',
    margin = dict(
        b = 0,
        l = 0,
        r = 0,
        t = 0
    ),
    paper_bgcolor = 'white',
    plot_bgcolor = 'white',
    showlegend = False,
    xaxis = dict(
        fixedrange = True,
        visible = False
    ),
    yaxis = dict(
        fixedrange = True,
        scaleanchor = 'x',
        scaleratio = 1,
        visible = False
    )
)


aislesReward = - 1
wallsReward = - 100
destinationReward = 100


textShadowStyle = {
    'text-align':'center',
    'text-shadow':'0px 0px 10px'
}

gridSizeSwitchStyle = [
    {
        'border-radius':'10px',
        'padding':'5px',
        'text-align':'center',
        'background-color':'gainsboro',
        'color':'black',
        'width':'100px'
    },
    {
        'border-radius':'10px',
        'padding':'5px',
        'text-align':'center',
        'background-color':'lightslategrey',
        'color':'black',
        'width':'100px'
    }
]

layoutSwitchStyle = [
    {
        'border-radius':'10px',
        'padding':'5px',
        'text-align':'center',
        'background-color':'gainsboro',
        'color':'black',
        'width':'100px'
    },
    {
        'border-radius':'10px',
        'padding':'5px',
        'text-align':'center',
        'background-color':'lightslategrey',
        'color':'black',
        'width':'100px'
    }
]

destinationSwitchStyle = [
    {
        'border-radius':'10px',
        'padding':'5px',
        'text-align':'center',
        'background-color':'gainsboro',
        'color':'black',
        'width':'100px'
    },
    {
        'border-radius':'10px',
        'padding':'5px',
        'text-align':'center',
        'background-color':'lightslategrey',
        'color':'black',
        'width':'100px'
    }
]

algorithmParametersSwitchStyle = [
    {
        'border-radius':'10px',
        'padding':'5px',
        'text-align':'center',
        'background-color':'gainsboro',
        'color':'black',
        'width':'100px',
        'margin-right':'35px'
    },
    {
        'border-radius':'10px',
        'padding':'5px',
        'text-align':'center',
        'background-color':'lightslategrey',
        'color':'black',
        'width':'100px',
        'margin-right':'35px'
    }
]

initialPointSwitchStyle = [
    {
        'border-radius':'10px',
        'padding':'5px',
        'text-align':'center',
        'background-color':'gainsboro',
        'color':'black',
        'width':'100px'
    },
    {
        'border-radius':'10px',
        'padding':'5px',
        'text-align':'center',
        'background-color':'lightslategrey',
        'color':'black',
        'width':'100px'
    }
]

obstaclesSwitchStyle = [
    {
        'border-radius':'10px',
        'padding':'5px',
        'text-align':'center',
        'background-color':'gainsboro',
        'color':'black',
        'width':'100px'
    },
    {
        'border-radius':'10px',
        'padding':'5px',
        'text-align':'center',
        'background-color':'lightslategrey',
        'color':'black',
        'width':'100px'
    }
]


disabledLayoutConfiguraion = [
    [
        {
            'label':'Add Walls',
            'value':'Add Walls',
            'disabled':False
        },
        {
            'label':'Remove Walls',
            'value':'Remove Walls',
            'disabled':False
        }
    ],
    [
        {
            'label':'Add Walls',
            'value':'Add Walls',
            'disabled':True
        },
        {
            'label':'Remove Walls',
            'value':'Remove Walls',
            'disabled':True
        }
    ]
]

disabledObstaclesConfiguraion = [
    [
        {
            'label':'Add Obstacle',
            'value':'Add Obstacle',
            'disabled':False
        },
        {
            'label':'Remove Obstacle',
            'value':'Remove Obstacle',
            'disabled':False
        }
    ],
    [
        {
            'label':'Add Obstacle',
            'value':'Add Obstacle',
            'disabled':True
        },
        {
            'label':'Remove Obstacle',
            'value':'Remove Obstacle',
            'disabled':True
        }
    ]
]



Maze_Follower_App.layout = dbc.Container(
   children = [
        dbc.Row(
            children = [
                dbc.Col(
                    children = [
                        html.H1(
                            children = [
                                'Maze Follwer App',
                            ],
                            style = {
                                'text-align':'center',
                                'text-shadow':'0px 0px 2px'
                            }
                        )
                    ]
                )
            ]
        ),
        html.Br(),
        dbc.Row(
            children = [
                dbc.Col(
                    children = [
                        dcc.Graph(
                            id = 'maze-figure',
                            figure = maze,
                            clear_on_unhover = True,
                            config = {
                                'displayModeBar':False
                            }
                        )
                    ]
                )
            ]
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            children = [
                dbc.Col(
                    children = [
                        dbc.Stack(
                            children = [
                                dbc.Row(
                                    children = [
                                        html.Div(
                                            id = 'grid-size-text',
                                            children = [
                                                'Configure Grid Size'
                                            ],
                                            style = textShadowStyle
                                        ),
                                    ],
                                    justify = 'center'
                                ),
                                dbc.Row(
                                    children = [
                                        html.Button(
                                            id = 'grid-size-button',
                                            children = [
                                                'Set'
                                            ],
                                            value = 'off',
                                            style = gridSizeSwitchStyle[0]
                                        ),
                                        dcc.Input(
                                            id = 'grid-rows',
                                            type = 'number',
                                            value = 1,
                                            min = 1,
                                            step = 1,
                                            inputMode = 'numeric',
                                            required = True,
                                            autoFocus = True,
                                            style = {
                                                'border-radius':'10px',
                                                'padding':'5px',
                                                'text-align':'center',
                                                'vertical-align':'middle',
                                                'width':'75px',
                                                'margin-left':'15px'
                                            }
                                        ),
                                        dcc.Input(
                                            id = 'grid-columns',
                                            type = 'number',
                                            value = 1,
                                            min = 1,
                                            step = 1,
                                            inputMode = 'numeric',
                                            required = True,
                                            autoFocus = True,
                                            style = {
                                                'border-radius':'10px',
                                                'padding':'5px',
                                                'text-align':'center',
                                                'width':'75px',
                                                'margin-left':'15px'
                                            }
                                        )
                                    ],
                                    justify = 'center'
                                )
                            ],
                            gap = 2
                        )
                    ],
                    width = 4
                ),
                dbc.Col(
                    children = [
                        dbc.Stack(
                            children = [
                                dbc.Row(
                                    children = [
                                        html.Div(
                                            id = 'layout-text',
                                            children = [
                                                'Configure Layout'
                                            ],
                                            style = textShadowStyle
                                        ),
                                    ],
                                    justify = 'center'
                                ),
                                dbc.Row(
                                    children = [
                                        html.Button(
                                            id = 'layout-button',
                                            children = [
                                                'Set'
                                            ],
                                            value = 'off',
                                            disabled = True,
                                            style = layoutSwitchStyle[0]
                                        ),
                                        dcc.RadioItems(
                                            id = 'layout-radio-items',
                                            value = 'Add Walls',
                                            options = disabledLayoutConfiguraion[1],
                                            inline = True,
                                            inputStyle = {
                                                'margin-left':'10px',
                                                'margin-right':'10px'
                                            },
                                            style = {
                                                'width':'280px'
                                            }
                                        )
                                    ],
                                    align = 'center',
                                    justify = 'center'
                                )
                            ],
                            gap = 2
                        )
                    ],
                    width = 4
                ),
                dbc.Col(
                    children = [
                        dbc.Stack(
                            children = [
                                dbc.Row(
                                    children = [
                                        html.Div(
                                            id = 'destination-point-text',
                                            children = [
                                                'Configure Destination Point'
                                            ],
                                            style = textShadowStyle
                                        ),
                                    ],
                                    justify = 'center'
                                ),
                                dbc.Row(
                                    children = [
                                        html.Button(
                                            id = 'destination-point-button',
                                            children = [
                                                'Set'
                                            ],
                                            value = 'off',
                                            disabled = True,
                                            style = destinationSwitchStyle[0]
                                        )   
                                    ],
                                    align = 'center',
                                    justify = 'center'
                                )
                            ],
                            gap = 2
                        )
                    ],
                    width = 3
                )
            ],
            justify = 'center'
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            children = [
                dbc.Stack(
                    children = [
                        dbc.Row(
                            children = [
                                html.Div(
                                    id = 'algorithm-parameters-text',
                                    children = [
                                        'Configure Algorithm Parameters'
                                    ],
                                    style = textShadowStyle
                                )
                            ],
                            justify = 'center'
                        ),
                        dbc.Row(
                            children = [
                                html.Div(
                                    id = 'algorithm-parameters',
                                    children = [
                                        html.Button(
                                            id = 'algorithm-parameters-button',
                                            children = [
                                                'Set'
                                            ],
                                            value = 'off',
                                            disabled = True,
                                            style = algorithmParametersSwitchStyle[0]
                                        ),
                                        'Discount Factor',
                                        dcc.Input(
                                            id = 'discount-factor',
                                            type = 'number',
                                            value = 0.5,
                                            disabled = True,
                                            min = 0,
                                            max = 1,
                                            step = 0.1,
                                            inputMode = 'numeric',
                                            required = True,
                                            style = {
                                                'border-radius':'10px',
                                                'padding':'5px',
                                                'text-align':'center',
                                                'vertical-align':'middle',
                                                'width':'65px',
                                                'margin-left':'15px',
                                                'margin-right':'35px'
                                            }
                                        ),
                                        'Greedy Policy',
                                        dcc.Input(
                                            id = 'greedy-policy',
                                            type = 'number',
                                            value = 0.5,
                                            disabled = True,
                                            min = 0,
                                            max = 1,
                                            step = 0.1,
                                            inputMode = 'numeric',
                                            required = True,
                                            style = {
                                                'border-radius':'10px',
                                                'padding':'5px',
                                                'text-align':'center',
                                                'vertical-align':'middle',
                                                'width':'65px',
                                                'margin-left':'15px',
                                                'margin-right':'35px'
                                            }
                                        ),
                                        'Learning Rate',
                                        dcc.Input(
                                            id = 'learning-rate',
                                            type = 'number',
                                            value = 0.5,
                                            disabled = True,
                                            min = 0,
                                            max = 1,
                                            step = 0.1,
                                            inputMode = 'numeric',
                                            required = True,
                                            style = {
                                                'border-radius':'10px',
                                                'padding':'5px',
                                                'text-align':'center',
                                                'vertical-align':'middle',
                                                'width':'65px',
                                                'margin-left':'15px'
                                            }
                                        )
                                    ],
                                    style = {
                                        'text-align':'center'
                                    }
                                )
                            ],
                            justify = 'center'
                        )
                    ],
                    gap = 2
                )
            ],
            justify = 'center'
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            children = [
                dbc.Stack(
                    children = [
                        dbc.Row(
                            children = [
                                html.Div(
                                    id = 'algorithm-training-text',
                                    children = [
                                        'Algorithm Training'
                                    ],
                                    style = textShadowStyle
                                )
                            ],
                            justify = 'center'
                        ),
                        dbc.Row(
                            children = [
                                html.Div(
                                    children = [
                                        'Current Session Episodes',
                                        dcc.Input(
                                            id = 'current-session-episodes',
                                            type = 'text',
                                            disabled = True,
                                            value = 0,
                                            required = True,
                                            style = {
                                                'border-radius':'10px',
                                                'padding':'5px',
                                                'text-align':'center',
                                                'width':'120px',
                                                'margin-left':'15px',
                                                'margin-right':'35px'
                                            }
                                        ),
                                        'Train Episodes',
                                        dcc.Input(
                                            id = 'train-episodes',
                                            type = 'number',
                                            value = 1,
                                            disabled = True,
                                            min = 1,
                                            step = 1,
                                            inputMode = 'numeric',
                                            required = True,
                                            style = {
                                                'border-radius':'10px',
                                                'padding':'5px',
                                                'text-align':'center',
                                                'vertical-align':'middle',
                                                'width':'120px',
                                                'margin-left':'15px',
                                                'margin-right':'35px',
                                            }
                                        ),
                                        html.Button(
                                            id = 'train-algorithm-button',
                                            children = [
                                                'Train Algorithm'
                                            ],
                                            disabled = True,
                                            style = {
                                                'border-radius':'10px',
                                                'padding':'5px',
                                                'text-align':'center',
                                                'background-color':'gainsboro',
                                                'color':'black',
                                                'width':'140px',
                                                'margin-right':'15px'
                                            }
                                        ),
                                        html.Button(
                                            id = 'reset-session-button',
                                            children = [
                                                'Reset Session'
                                            ],
                                            disabled = True,
                                            style = {
                                                'border-radius':'10px',
                                                'padding':'5px',
                                                'text-align':'center',
                                                'background-color':'gainsboro',
                                                'color':'black',
                                                'width':'140px'
                                            }
                                        )
                                    ],
                                    style = {
                                        'text-align':'center'
                                    }
                                )
                            ],
                            justify = 'center'
                        )
                    ],
                    gap = 2
                )
            ],
            justify = 'center'
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            children = [
                dbc.Col(
                    children = [
                        dbc.Stack(
                            children = [
                                dbc.Row(
                                    children = [
                                        html.Div(
                                            id = 'initial-point-text',
                                            children = [
                                                'Configure Initial Point'
                                            ],
                                            style = textShadowStyle
                                        ),
                                    ],
                                    justify = 'center'
                                ),
                                dbc.Row(
                                    children = [
                                        html.Button(
                                            id = 'initial-point-button',
                                            children = [
                                                'Set'
                                            ],
                                            value = 'off',
                                            disabled = True,
                                            style = initialPointSwitchStyle[0]
                                        )   
                                    ],
                                    align = 'center',
                                    justify = 'center'
                                )
                            ],
                            gap = 2
                        )
                    ],
                    width = 4
                ),
                dbc.Col(
                    children = [
                        dbc.Stack(
                            children = [
                                dbc.Row(
                                    children = [
                                        html.Div(
                                            id = 'dynamic-simulation-text',
                                            children = [
                                                'Dynamic Simulation'
                                            ],
                                            style = textShadowStyle
                                        ),
                                    ],
                                ),
                                dbc.Row(
                                    children = [
                                        html.Button(
                                            id = 'dynamic-simulation-start-button',
                                            children = [
                                                'Start'
                                            ],
                                            disabled = True,
                                            style = {
                                                'border-radius':'10px',
                                                'padding':'5px',
                                                'text-align':'center',
                                                'background-color':'gainsboro',
                                                'color':'black',
                                                'width':'80px',
                                                'margin-right':'15px'
                                            }
                                        ),
                                        html.Button(
                                            id = 'dynamic-simulation-pause-button',
                                            children = [
                                                'Pause'
                                            ],
                                            disabled = True,
                                            style = {
                                                'border-radius':'10px',
                                                'padding':'5px',
                                                'text-align':'center',
                                                'background-color':'gainsboro',
                                                'color':'black',
                                                'width':'80px'
                                            }
                                        )
                                    ],
                                    align = 'center',
                                    justify = 'center'
                                ),
                                dbc.Row(
                                    children = [
                                        html.Button(
                                            id = 'dynamic-simulation-restart-button',
                                            children = [
                                                'Restart'
                                            ],
                                            disabled = True,
                                            style = {
                                                'border-radius':'10px',
                                                'padding':'5px',
                                                'text-align':'center',
                                                'background-color':'gainsboro',
                                                'color':'black',
                                                'width':'80px'
                                            }
                                        )
                                    ],
                                    align = 'center',
                                    justify = 'center'
                                )
                            ],
                            gap = 2
                        )
                    ],
                    width = 2
                ),
                dbc.Col(
                    children = [
                        dbc.Stack(
                            children = [
                                dbc.Row(
                                    children = [
                                        html.Div(
                                            id = 'static-simulation-text',
                                            children = [
                                                'Static Simulation'
                                            ],
                                            style = textShadowStyle
                                        ),
                                    ],
                                ),
                                dbc.Row(
                                    children = [
                                        html.Button(
                                            id = 'static-simulation-button',
                                            children = [
                                                'Simulate'
                                            ],
                                            disabled = True,
                                            style = {
                                                'border-radius':'10px',
                                                'padding':'5px',
                                                'text-align':'center',
                                                'background-color':'gainsboro',
                                                'color':'black',
                                                'width':'100px'
                                            }
                                        )
                                    ],
                                    justify = 'center'
                                )
                            ],
                            gap = 2
                        )
                    ],
                    width = 2
                ),
                dbc.Col(
                    children = [
                        dbc.Stack(
                            children = [
                                dbc.Row(
                                    children = [
                                        html.Div(
                                            id = 'configure-obstacles-text',
                                            children = [
                                                'Obstacles Configured'
                                            ],
                                            style = textShadowStyle
                                        ),
                                    ],
                                ),
                                dbc.Row(
                                    children = [
                                        html.Div(
                                            children = [
                                                dcc.RadioItems(
                                                    id = 'configure-obstacles-radio-items',
                                                    value = 'Add Obstacle',
                                                    options = disabledObstaclesConfiguraion[1],
                                                    inline = True,
                                                    inputStyle = {
                                                        'margin-left':'10px',
                                                        'margin-right':'10px'
                                                    }
                                                )
                                            ],
                                            style = {
                                                'text-align':'center'
                                            }
                                        )
                                    ]
                                ),
                                dbc.Row(
                                    children = [
                                        html.Button(
                                            id = 'configure-obstacles-button',
                                            children = [
                                                'Configure'
                                            ],
                                            value = 'on',
                                            disabled = True,
                                            style = obstaclesSwitchStyle[1]
                                        )
                                    ],
                                    align = 'center',
                                    justify = 'center'
                                )
                            ],
                            gap = 2
                        )
                    ],
                    width = 4
                )
            ],
            justify = 'center'
        )
    ],
    style = {
        'font-family':'Bahnschrift'
    }
)


@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'grid-size-text',
            component_property = 'children'
        ),
        Output(
            component_id = 'grid-size-button',
            component_property = 'children'
        ),
        Output(
            component_id = 'grid-size-button',
            component_property = 'value'
        ),
        Output(
            component_id = 'grid-size-button',
            component_property = 'style'
        ),
        Output(
            component_id = 'grid-rows',
            component_property = 'disabled'
        ),
        Output(
            component_id = 'grid-columns',
            component_property = 'disabled'
        )
    ],
    [
        Input(
            component_id = 'grid-size-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'grid-size-button',
            component_property = 'value'
        )
    ],
    [
        State(
            component_id = 'grid-rows',
            component_property = 'value'
        ),
        State(
            component_id = 'grid-columns',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def grid_size_function(gridSizeButton_n_clicks,gridSizeButton_value,gridRows_value,gridColumns_value):
    if gridSizeButton_value == 'off' and gridRows_value*gridColumns_value > 2:
        return ['Grid Size Configured','Configure','on',gridSizeSwitchStyle[1],True,True]
    else:
        return ['Configure Grid Size','Set','off',gridSizeSwitchStyle[0],False,False]


@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'layout-text',
            component_property = 'children'
        ),
        Output(
            component_id = 'layout-button',
            component_property = 'disabled'
        ),
        Output(
            component_id = 'layout-button',
            component_property = 'children'
        ),
        Output(
            component_id = 'layout-button',
            component_property = 'value'
        ),
        Output(
            component_id = 'layout-button',
            component_property = 'style'
        ),
        Output(
            component_id = 'layout-radio-items',
            component_property = 'options'
        )
    ],
    [
        Input(
            component_id = 'grid-size-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'grid-size-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'layout-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'layout-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def layout_function(gridSizeButton_n_clicks,gridSizeButton_value,layoutButton_n_clicks,layoutButton_value):
    if ctx.triggered_id == 'grid-size-button':
        if gridSizeButton_value == 'on':
            return ['Configure Layout',False,'Set','off',layoutSwitchStyle[0],disabledLayoutConfiguraion[0]]
        else:
            return ['Configure Layout',True,'Set','off',layoutSwitchStyle[0],disabledLayoutConfiguraion[1]]
    else:
        if layoutButton_value == 'off':
            return ['Layout Configured',False,'Configure','on',layoutSwitchStyle[1],disabledLayoutConfiguraion[1]]
        else:
            return ['Configure Layout',False,'Set','off',layoutSwitchStyle[0],disabledLayoutConfiguraion[0]]


@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'destination-point-text',
            component_property = 'children'
        ),
        Output(
            component_id = 'destination-point-button',
            component_property = 'disabled'
        ),
        Output(
            component_id = 'destination-point-button',
            component_property = 'children'
        ),
        Output(
            component_id = 'destination-point-button',
            component_property = 'value'
        ),
        Output(
            component_id = 'destination-point-button',
            component_property = 'style'
        )
    ],
    [
        Input(
            component_id = 'grid-size-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'grid-size-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'layout-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'layout-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'destination-point-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'destination-point-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def destination_point_function(gridSizeButton_n_clicks,gridSizeButton_value,layoutButton_n_clicks,layoutButton_value,destinationPointButton_n_clicks,destinationPointButton_value):
    if ctx.triggered_id == 'grid-size-button' or ctx.triggered_id == 'layout-button':
        if gridSizeButton_value == 'on' and layoutButton_value == 'on':
            return ['Configure Destination Point',False,'Set','off',destinationSwitchStyle[0]]
        else:
            return ['Configure Destination Point',True,'Set','off',destinationSwitchStyle[0]]
    else:
        if destinationPointButton_value == 'off':
            return ['Destination Point Configured',False,'Configure','on',destinationSwitchStyle[1]]
        else:
            return ['Configure Destination Point',False,'Set','off',destinationSwitchStyle[0]]


@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'algorithm-parameters-text',
            component_property = 'children'
        ),
        Output(
            component_id = 'algorithm-parameters-button',
            component_property = 'disabled'
        ),
        Output(
            component_id = 'algorithm-parameters-button',
            component_property = 'children'
        ),
        Output(
            component_id = 'algorithm-parameters-button',
            component_property = 'value'
        ),
        Output(
            component_id = 'algorithm-parameters-button',
            component_property = 'style'
        ),
        Output(
            component_id = 'discount-factor',
            component_property = 'disabled'
        ),
        Output(
            component_id = 'greedy-policy',
            component_property = 'disabled'
        ),
        Output(
            component_id = 'learning-rate',
            component_property = 'disabled'
        )
    ],
    [
        Input(
            component_id = 'grid-size-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'grid-size-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'layout-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'layout-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'destination-point-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'destination-point-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'algorithm-parameters-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'algorithm-parameters-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def algorithm_parameters_fuction(gridSizeButton_n_clicks,gridSizeButton_value,layoutButton_n_clicks,layoutButton_value,destinationPointButton_n_clicks,destinationPointButton_value,algorithmParametersButton_n_clicks,algorithmParametersButton_value):
    if ctx.triggered_id == 'grid-size-button' or ctx.triggered_id == 'layout-button' or ctx.triggered_id == 'destination-point-button':
        if gridSizeButton_value == 'on' and layoutButton_value == 'on' and destinationPointButton_value == 'on':
            return ['Configure Algorithm Parameters',False,'Set','off',algorithmParametersSwitchStyle[0],False,False,False]
        else:
            return ['Configure Algorithm Parameters',True,'Set','off',algorithmParametersSwitchStyle[0],True,True,True]
    else:
        if algorithmParametersButton_value == 'off':
            return ['Algorithm Parameters Configured',False,'Configure','on',algorithmParametersSwitchStyle[1],True,True,True]
        else:
            return ['Configure Algorithm Parameters',False,'Set','off',algorithmParametersSwitchStyle[0],False,False,False]


@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'current-session-episodes',
            component_property = 'value'
        ),
        Output(
            component_id = 'train-episodes',
            component_property = 'disabled'
        ),
        Output(
            component_id = 'train-algorithm-button',
            component_property = 'disabled'
        ),
        Output(
            component_id = 'reset-session-button',
            component_property = 'disabled'
        )
    ],
    [
        Input(
            component_id = 'grid-size-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'grid-size-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'layout-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'layout-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'destination-point-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'destination-point-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'algorithm-parameters-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'algorithm-parameters-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'train-algorithm-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'reset-session-button',
            component_property = 'n_clicks'
        )
    ],
    [
        State(
            component_id = 'current-session-episodes',
            component_property = 'value'
        ),
        State(
            component_id = 'train-episodes',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def algorithm_training_function(gridSizeButton_n_clicks,gridSizeButton_value,layoutButton_n_clicks,layoutButton_value,destinationPointButton_n_clicks,destinationPointButton_value,algorithmParametersButton_n_clicks,algorithmParametersButton_value,trainAlgorithmButton_n_clicks,resetSessionButton_n_clicks,currentSessionEpisodes_value,trainEpisodes_value):
    if ctx.triggered_id == 'grid-size-button' or ctx.triggered_id == 'layout-button' or ctx.triggered_id == 'destination-point-button' or ctx.triggered_id == 'algorithm-parameters-button':
        if gridSizeButton_value == 'on' and layoutButton_value == 'on' and destinationPointButton_value == 'on' and algorithmParametersButton_value == 'on':
            return [0,False,False,True]
        else:
            return [0,True,True,True]
    elif ctx.triggered_id == 'train-algorithm-button':
        return [currentSessionEpisodes_value + trainEpisodes_value,False,False,False]
    else:
        return [0,False,False,True]


@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'initial-point-text',
            component_property = 'children'
        ),
        Output(
            component_id = 'initial-point-button',
            component_property = 'disabled'
        ),
        Output(
            component_id = 'initial-point-button',
            component_property = 'children'
        ),
        Output(
            component_id = 'initial-point-button',
            component_property = 'value'
        ),
        Output(
            component_id = 'initial-point-button',
            component_property = 'style'
        )
    ],
    [
        Input(
            component_id = 'grid-size-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'layout-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'destination-point-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'algorithm-parameters-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'train-algorithm-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'reset-session-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'initial-point-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'initial-point-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def initial_point_function(gridSizeButton_n_clicks,layoutButton_n_clicks,destinationPointButton_n_clicks,algorithmParametersButton_n_clicks,trainAlgorithmButton_n_clicks,resetSessionButton_n_clicks,initialPointButton_n_clicks,initialPointButton_value):
    if ctx.triggered_id == 'grid-size-button' or ctx.triggered_id == 'layout-button' or ctx.triggered_id == 'destination-point-button' or ctx.triggered_id == 'algorithm-parameters-button' or ctx.triggered_id == 'train-algorithm-button' or ctx.triggered_id == 'reset-session-button':
        if ctx.triggered_id == 'train-algorithm-button':
            return ['Configure Initial Point',False,'Set','off',initialPointSwitchStyle[0]]
        else:
            return ['Configure Initial Point',True,'Set','off',initialPointSwitchStyle[0]]
    else:
        if initialPointButton_value == 'off':
            return ['Initial Point Configured',False,'Configure','on',initialPointSwitchStyle[1]]
        else:
            return ['Configure Initial Point',False,'Set','off',initialPointSwitchStyle[0]]


@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'dynamic-simulation-start-button',
            component_property = 'disabled'
        ),
        Output(
            component_id = 'dynamic-simulation-pause-button',
            component_property = 'disabled'
        ),
        Output(
            component_id = 'dynamic-simulation-restart-button',
            component_property = 'disabled'
        ),
        Output(
            component_id = 'static-simulation-button',
            component_property = 'disabled'
        )
    ],
    [
        Input(
            component_id = 'grid-size-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'layout-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'destination-point-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'algorithm-parameters-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'train-algorithm-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'reset-session-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'initial-point-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'initial-point-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def dynamic_and_static_simulation_function(gridSizeButton_n_clicks,layoutButton_n_clicks,destinationPointButton_n_clicks,algorithmParametersButton_n_clicks,trainAlgorithmButton_n_clicks,resetSessionButton_n_clicks,initialPointButton_n_clicks,initialPointButton_value):
    if initialPointButton_value == 'on':
        return [False,False,False,False]
    else:
        return [True,True,True,True]


@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'configure-obstacles-text',
            component_property = 'children'
        ),
        Output(
            component_id = 'configure-obstacles-button',
            component_property = 'disabled'
        ),
        Output(
            component_id = 'configure-obstacles-button',
            component_property = 'children'
        ),
        Output(
            component_id = 'configure-obstacles-button',
            component_property = 'value'
        ),
        Output(
            component_id = 'configure-obstacles-button',
            component_property = 'style'
        ),
        Output(
            component_id = 'configure-obstacles-radio-items',
            component_property = 'options'
        )
    ],
    [
        Input(
            component_id = 'grid-size-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'layout-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'destination-point-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'algorithm-parameters-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'train-algorithm-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'reset-session-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'initial-point-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'initial-point-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'configure-obstacles-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'configure-obstacles-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)


def obstacle_function(gridSizeButton_n_clicks,layoutButton_n_clicks,destinationPointButton_n_clicks,algorithmParametersButton_n_clicks,trainAlgorithmButton_n_clicks,resetSessionButton_n_clicks,initialPointButton_n_clicks,initialPointButton_value,configureObstaclesButton_n_clicks,configureObstaclesButton_value):
    print(str(ctx.triggered_id)+'   '+configureObstaclesButton_value)
    if ctx.triggered_id == 'configure-obstacles-button':
        if configureObstaclesButton_value == 'on':
            return ['Configure Obstacles',False,'Set','off',obstaclesSwitchStyle[0],disabledObstaclesConfiguraion[0]]
        else:
            return ['Obstacles Configured',False,'Configure','on',obstaclesSwitchStyle[1],disabledObstaclesConfiguraion[1]]
    elif initialPointButton_value == 'on':
        return ['Obstacles Configured',False,'Configure','on',obstaclesSwitchStyle[1],disabledObstaclesConfiguraion[1]]
    else:
        return ['Obstacles Configured',True,'Configure','on',obstaclesSwitchStyle[1],disabledObstaclesConfiguraion[1]]



if __name__ == '__main__':
    Maze_Follower_App.run_server(debug=True)