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



initializeFigure = go.Figure()

initializeFigure.update_layout(
    paper_bgcolor = 'white',
    plot_bgcolor = 'white',
    xaxis = dict(
        fixedrange = True,
        visible = False
    ),
    yaxis = dict(
        fixedrange = True,
        visible = False
    )
)


transitionDuration = 1000



aisleReward = - 1
wallReward = -100
destinationReward = 100


discountFactor = 0.5
greedyPolicy = 0.5
learningRate = 0.5



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


destinationPointSwitchStyle = [
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
                            figure = initializeFigure,
                            config = {
                                'displayModeBar':False
                            },
                            animate = True,
                            animation_options = {
                                'transition': {
                                    'duration':600,
                                    'ease':'cubic-in-out'
                                }
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
                                            disabled = False,
                                            style = gridSizeSwitchStyle[0]
                                        ),
                                        dcc.Input(
                                            id = 'grid-rows',
                                            type = 'number',
                                            value = 1,
                                            min = 1,
                                            max = 20,
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
                                            max = 50,
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
                                            style = destinationPointSwitchStyle[0]
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
                                            value = discountFactor,
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
                                            value = greedyPolicy,
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
                                            value = learningRate,
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
                    width = 2
                ),
                dbc.Col(
                    children = [
                        dbc.Stack(
                            children = [
                                dbc.Row(
                                    children = [
                                        html.Div(
                                            id = 'obstacles-text',
                                            children = [
                                                'Configure Obstacles'
                                            ],
                                            style = textShadowStyle
                                        ),
                                    ],
                                ),
                                dbc.Row(
                                    children = [
                                        html.Button(
                                            id = 'obstacles-button',
                                            children = [
                                                'Configure'
                                            ],
                                            value = 'on',
                                            disabled = True,
                                            style = obstaclesSwitchStyle[1]
                                        ),
                                        html.Button(
                                            id = 'reset-obstacles-button',
                                            children = [
                                                'Reset'
                                            ],
                                            disabled = True,
                                            style = {
                                                'border-radius':'10px',
                                                'padding':'5px',
                                                'text-align':'center',
                                                'background-color':'gainsboro',
                                                'color':'black',
                                                'width':'100px',
                                                'margin-left':'15px'
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
                    width = 3
                ),
                dbc.Col(
                    children = [
                        dbc.Stack(
                            children = [
                                dbc.Row(
                                    children = [
                                        html.Div(
                                            id = 'simulation-text',
                                            children = [
                                                'Simulation'
                                            ],
                                            style = textShadowStyle
                                        ),
                                    ],
                                ),
                                dbc.Row(
                                    children = [
                                        html.Button(
                                            id = 'start-simulation-button',
                                            children = [
                                                'Start Simulation'
                                            ],
                                            disabled = True,
                                            style = {
                                                'border-radius':'10px',
                                                'padding':'5px',
                                                'text-align':'center',
                                                'background-color':'gainsboro',
                                                'color':'black',
                                                'width':'150px'
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
            component_id = 'grid-size-button',
            component_property = 'disabled'
        )
    ],
    [
        Input(
            component_id = 'grid-rows',
            component_property = 'value'
        ),
        Input(
            component_id = 'grid-columns',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def grid_size_button_disabled_function(gridRows_value,gridColumns_value):
    if gridRows_value == None or gridColumns_value == None:
        return [True]
    else:
        return [False]


@Maze_Follower_App.callback(
    [
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
        )
    ],
    [
        Input(
            component_id = 'grid-size-button',
            component_property = 'n_clicks'
        )
    ],
    [
        State(
            component_id = 'grid-size-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def grid_size_button_children_value_style_function(gridSizeButton_n_clicks,gridSizeButton_value):
    if gridSizeButton_value == 'off':
        return ['Configure','on',gridSizeSwitchStyle[1]]
    else:
        return ['Set','off',gridSizeSwitchStyle[0]]
    

@Maze_Follower_App.callback(
    [
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
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def grid_row_grid_column_disabled_function(gridSizeButton_value):
    if gridSizeButton_value == 'off':
        return [False,False]
    else:
        return [True,True]
    

@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'layout-button',
            component_property = 'disabled'
        )
    ],
    [
        Input(
            component_id = 'grid-size-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def layout_button_disabled_function(gridSizeButton_value):
    if gridSizeButton_value == 'off':
        return [True]
    else:
        return [False]
    

@Maze_Follower_App.callback(
    [
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
        )
    ],
    [
        State(
            component_id = 'layout-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def layout_button_children_value_style_function(gridSizeButton_n_clicks,layoutButton_n_clicks,layoutButton_value):
    if ctx.triggered_id == 'layout-button' and layoutButton_value == 'off':
        return ['Configure','on',layoutSwitchStyle[1]]
    else:
        return ['Set','off',layoutSwitchStyle[0]]
    

@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'layout-radio-items',
            component_property = 'options'
        )
    ],
    [
        Input(
            component_id = 'grid-size-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'layout-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def layout_radio_items_options_function(gridSizeButton_value,layoutButton_value):
    if gridSizeButton_value == 'on' and layoutButton_value == 'off':
        return [disabledLayoutConfiguraion[0]]
    else:
        return [disabledLayoutConfiguraion[1]]
    

@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'destination-point-text',
            component_property = 'children'
        )
    ],
    [
        Input(
            component_id = 'layout-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'destination-point-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def destination_point_text_children_function(layoutButton_value,destinationPointButton_value):
    if layoutButton_value == 'on' and destinationPointButton_value == 'off':
        return ['Select Destination Point']
    else:
        return ['Configure Destination Point']
    

@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'destination-point-button',
            component_property = 'disabled'
        )
    ],
    [
        Input(
            component_id = 'layout-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'maze-figure',
            component_property = 'clickData'
        )
    ],
    [
        State(
            component_id = 'destination-point-button',
            component_property = 'disabled'
        )
    ],
    prevent_initial_call = True
)

def destination_point_button_disabled_function(layoutButton_value,mazeFigure_clickData,destinationPointButton_disabled):
    if layoutButton_value == 'on' and ctx.triggered_id == 'maze-figure':
        if destinationPointButton_disabled:
            return [False]
        else:
            return [dash.no_update]
    else:
        return [True]
    

@Maze_Follower_App.callback(
    [
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
            component_id = 'layout-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'destination-point-button',
            component_property = 'n_clicks'
        )
    ],
    [
        State(
            component_id = 'destination-point-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def destination_point_button_children_value_style_function(gridSizeButton_n_clicks,layoutButton_n_clicks,destinationPointButton_n_clicks,destinationPointButton_value):
    if ctx.triggered_id == 'destination-point-button' and destinationPointButton_value == 'off':
        return ['Configure','on',destinationPointSwitchStyle[1]]
    else:
        return ['Set','off',destinationPointSwitchStyle[0]]
    

@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'algorithm-parameters-button',
            component_property = 'disabled'
        )
    ],
    [
        Input(
            component_id = 'destination-point-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'discount-factor',
            component_property = 'value'
        ),
        Input(
            component_id = 'greedy-policy',
            component_property = 'value'
        ),
        Input(
            component_id = 'learning-rate',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def algorithm_parameters_button_disabled_function(destinationPointButton_value,discountFactor_value,greedyPolicy_value,learningRate_value):
    if destinationPointButton_value == 'off' or discountFactor_value == None or greedyPolicy_value == None or learningRate_value == None:
        return [True]
    else:
        return [False]
    

@Maze_Follower_App.callback(
    [
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
        )
    ],
    [
        State(
            component_id = 'algorithm-parameters-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def algorithm_parameters_button_children_value_style_function(gridSizeButton_n_clicks,layoutButton_n_clicks,destinationPointButton_n_clicks,algorithmParametersButton_n_clicks,algorithmParametersButton_value):
    if ctx.triggered_id == 'algorithm-parameters-button' and algorithmParametersButton_value == 'off':
        return ['Configure','on',algorithmParametersSwitchStyle[1]]
    else:
        return ['Set','off',algorithmParametersSwitchStyle[0]]
    

@Maze_Follower_App.callback(
    [
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
            component_id = 'destination-point-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'algorithm-parameters-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def algorithm_parameters_disabled_function(destinationPointButton_value,algorithmParametersButton_value):
    if destinationPointButton_value == 'on' and algorithmParametersButton_value == 'off':
        return [False,False,False]
    else:
        return [True,True,True]


@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'train-episodes',
            component_property = 'disabled'
        )
    ],
    [
        Input(
            component_id = 'algorithm-parameters-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def train_episodes_disabled_function(algorithmParametersButton_value):
    if algorithmParametersButton_value == 'off':
        return [True]
    else:
        return [False]
    

@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'train-algorithm-button',
            component_property = 'disabled'
        )
    ],
    [
        Input(
            component_id = 'algorithm-parameters-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'train-episodes',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def train_algorithm_button_disabled_function(algorithmParametersButton_value,trainEpisodes_value):
    if algorithmParametersButton_value == 'off' or trainEpisodes_value == None:
        return [True]
    else:
        return [False]
    

@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'reset-session-button',
            component_property = 'disabled'
        )
    ],
    [
        Input(
            component_id = 'algorithm-parameters-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'current-session-episodes',
            component_property = 'value'
        ),
        Input(
            component_id = 'reset-session-button',
            component_property = 'n_clicks'
        )

    ],
    prevent_initial_call = True
)

def reset_session_button_disabled_function(algorithmParametersButton_value,currentSessionEpisodes_value,resetSessionButton_n_clicks):
    if algorithmParametersButton_value == 'on' and currentSessionEpisodes_value > 0:
        return [False]
    else:
        return [True]
    

@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'initial-point-text',
            component_property = 'children'
        )
    ],
    [
        Input(
            component_id = 'current-session-episodes',
            component_property = 'value'
        ),
        Input(
            component_id = 'initial-point-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def initial_point_text_children_function(currentSessionEpisodes_value,initialPointButton_value):
    if currentSessionEpisodes_value > 0 and initialPointButton_value == 'off':
        return ['Select Initial Point']
    else:
        return ['Configure Initial Point']
    

@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'initial-point-button',
            component_property = 'disabled'
        )
    ],
    [
        Input(
            component_id = 'current-session-episodes',
            component_property = 'value'
        ),
        Input(
            component_id = 'maze-figure',
            component_property = 'clickData'
        )
    ],
    prevent_initial_call = True
)

def initial_point_button_disabled_function(currentSessionEpisodes_value,mazeFigure_clickData):
    if currentSessionEpisodes_value > 0 and ctx.triggered_id == 'maze-figure':
        if rewardTableFullydefined[initialPoint[0],initialPoint[1]] == aisleReward:
            return [False]
        else:
            return [True]
    else:
        return [True]
    

@Maze_Follower_App.callback(
    [
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
        )
    ],
    [
        State(
            component_id = 'initial-point-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def initial_point_button_children_value_style_function(gridSizeButton_n_clicks,layoutButton_n_clicks,destinationPointButton_n_clicks,algorithmParametersButton_n_clicks,trainAlgorithmButton_n_clicks,resetSessionButton_n_clicks,initialPointButton_n_clicks,initialPointButton_value):
    if ctx.triggered_id == 'initial-point-button' and initialPointButton_value == 'off':
        return ['Configure','on',initialPointSwitchStyle[1]]
    else:
        return ['Set','off',initialPointSwitchStyle[0]]
    

@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'obstacles-button',
            component_property = 'disabled'
        )
    ],
    [
        Input(
            component_id = 'initial-point-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def configure_obstacles_button_disabled_function(initialPointButton_value):
    if initialPointButton_value == 'on':
        return [False]
    else:
        return [True]
    

@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'obstacles-button',
            component_property = 'children'
        ),
        Output(
            component_id = 'obstacles-button',
            component_property = 'value'
        ),
        Output(
            component_id = 'obstacles-button',
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
            component_id = 'obstacles-button',
            component_property = 'n_clicks'
        )
    ],
    [
        State(
            component_id = 'obstacles-button',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def configure_obstacles_button_children_value_style_function(gridSizeButton_n_clicks,layoutButton_n_clicks,destinationPointButton_n_clicks,algorithmParametersButton_n_clicks,trainAlgorithmButton_n_clicks,resetSessionButton_n_clicks,initialPointButton_n_clicks,obstaclesButton_n_clicks,obstaclesButton_value):
    if ctx.triggered_id == 'obstacles-button' and obstaclesButton_value == 'on':
        return ['Set','off',obstaclesSwitchStyle[0]]
    else:
        return ['Configure','on',obstaclesSwitchStyle[1]]
    

@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'start-simulation-button',
            component_property = 'disabled'
        )
    ],
    [
        Input(
            component_id = 'initial-point-button',
            component_property = 'value'
        ),
        
        Input(
            component_id = 'obstacles-button',
            component_property = 'value'
        ),
    ],
    prevent_initial_call = True
)

def start_simulation_button_disabled_function(initialPointButton_value,obstaclesButton_value):
    if initialPointButton_value == 'on' and obstaclesButton_value == 'on':
        return [False]
    else:
        return [True]


@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'maze-figure',
            component_property = 'figure'
        ),
        Output(
            component_id = 'maze-figure',
            component_property = 'clickData'
        )
    ],
    [
        Input(
            component_id = 'grid-rows',
            component_property = 'value'
        ),
        Input(
            component_id = 'grid-columns',
            component_property = 'value'
        ),
        Input(
            component_id = 'maze-figure',
            component_property = 'clickData'
        ),
        Input(
            component_id = 'grid-size-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'layout-button',
            component_property = 'value'
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
            component_id = 'train-algorithm-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'reset-session-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'initial-point-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'start-simulation-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'obstacles-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'reset-obstacles-button',
            component_property = 'n_clicks'
        )
    ],
    [
        State(
            component_id = 'layout-radio-items',
            component_property = 'value'
        ),
        State(
            component_id = 'discount-factor',
            component_property = 'value'
        ),
        State(
            component_id = 'greedy-policy',
            component_property = 'value'
        ),
        State(
            component_id = 'learning-rate',
            component_property = 'value'
        ),
        State(
            component_id = 'current-session-episodes',
            component_property = 'value'
        )
    ],
    prevent_initial_call = False
)

def maze_figure_figure_clickData_function(gridRows_value,gridColumns_value,mazeFigure_clickData,gridSizeButton_value,layoutButton_value,destinationPointButton_value,algorithmParametersButton_n_clicks,trainAlgorithmButton_n_clicks,resetSessionButton_n_clicks,initialPointButton_value,startSimulationButton_n_clicks,obstaclesButton_value,resetObstaclesButton_n_clicks,layoutRadioItems_value,discountFactor_value,greedyPolicy_value,learningRate_value,currentSessionEpisodes_value):
    if gridSizeButton_value == 'off':
        if gridRows_value != None and gridColumns_value != None:
            global mazeUnderdefined,rewardTableUnderdefined,mazeFullydefined,rewardTableFullydefined,QTable,initialPoint,mazeFullydefinedWithInitialPoint,mazeSimulationWithoutObstacles,shortestPathWithoutObstacles,mazeSimulationWithObstacles,shortestPathWithObstacles,obstacleTable,shortestPathToThePointBeforeObstacle,shortestPathFromThePointBeforeObstacle,rewardTableFullydefinedWithObstacles,shortestPathForDynamicSimulation,staticMazeForDynamicSimulation
            obstacleTable = []
            mazeUnderdefined = go.Figure()
            rewardTableUnderdefined = np.full((gridRows_value,gridColumns_value),aisleReward)
            formMaze(mazeUnderdefined,gridRows_value,gridColumns_value)
            return [mazeUnderdefined,dash.no_update]
        else:
            return [dash.no_update,dash.no_update]
    elif ctx.triggered_id == 'grid-size-button' or ctx.triggered_id == 'layout-button':
        figure_update_layout_hovermode(mazeUnderdefined,'closest')
        return [mazeUnderdefined,dash.no_update]
    elif layoutButton_value == 'off':
        gridPoint = mazeFigure_clickData['points'][0]['curveNumber'] - 1 - gridRows_value*gridColumns_value
        if layoutRadioItems_value == 'Add Walls':
            rewardTableUnderdefined[gridPoint%gridRows_value,gridPoint//gridRows_value] = wallReward
            mazeUnderdefined.update_traces(overwrite = True,fillcolor = 'darkslategrey',selector = dict(name = str(gridPoint//gridRows_value) + ',' + str(gridPoint%gridRows_value)))
            return [mazeUnderdefined,None]
        else:
            rewardTableUnderdefined[gridPoint%gridRows_value,gridPoint//gridRows_value] = aisleReward
            mazeUnderdefined.update_traces(overwrite = True,fillcolor = 'white',selector = dict(name = str(gridPoint//gridRows_value) + ',' + str(gridPoint%gridRows_value)))
            return [mazeUnderdefined,None]
    elif ctx.triggered_id == 'destination-point-button':
        if destinationPointButton_value == 'off':
            figure_update_layout_hovermode(mazeFullydefined,'closest')
        else:
            figure_update_layout_hovermode(mazeFullydefined,False)
        return [mazeFullydefined,dash.no_update]
    elif destinationPointButton_value == 'off':
        mazeFullydefined = go.Figure(mazeUnderdefined)
        rewardTableFullydefined = np.copy(rewardTableUnderdefined)
        gridPoint = mazeFigure_clickData['points'][0]['curveNumber'] - 1 - gridRows_value*gridColumns_value
        mazeFullydefined.update_traces(overwrite = True,fillcolor = 'forestgreen',selector = dict(name = str(gridPoint//gridRows_value) + ',' + str(gridPoint%gridRows_value)))
        rewardTableFullydefined[gridPoint%gridRows_value,gridPoint//gridRows_value] = destinationReward
        return [mazeFullydefined,None]
    elif ctx.triggered_id == 'algorithm-parameters-button' or ctx.triggered_id == 'reset-session-button':
        QTable = np.zeros((gridRows_value,gridColumns_value,4))
        figure_update_layout_hovermode(mazeFullydefined,False)
        return [mazeFullydefined,dash.no_update]
    if ctx.triggered_id == 'train-algorithm-button':
        if aisleReward in rewardTableFullydefined:
            figure_update_layout_hovermode(mazeFullydefined,'closest')
            return [mazeFullydefined,dash.no_update]
        else:
            return [dash.no_update,dash.no_update]
    elif ctx.triggered_id == 'initial-point-button':
        if initialPointButton_value == 'off':
            figure_update_layout_hovermode(mazeSimulationWithoutObstacles,'closest')
        else:
            figure_update_layout_hovermode(mazeSimulationWithoutObstacles,False)
            mazeSimulationWithObstacles = go.Figure(mazeSimulationWithoutObstacles)
            shortestPathWithObstacles = shortestPathWithoutObstacles.copy()
            obstacleTable = []
            shortestPathToThePointBeforeObstacle = [initialPoint]
            shortestPathFromThePointBeforeObstacle = shortestPathWithoutObstacles.copy()
            rewardTableFullydefinedWithObstacles = np.copy(rewardTableFullydefined)
            shortestPathForDynamicSimulation = shortestPathWithoutObstacles.copy()
            staticMazeForDynamicSimulation = go.Figure(mazeSimulationWithoutObstacles)
        return [mazeSimulationWithoutObstacles,dash.no_update]
    elif initialPointButton_value == 'off':
        gridPoint = mazeFigure_clickData['points'][0]['curveNumber'] - 1 - gridRows_value*gridColumns_value
        initialPoint = [gridPoint%gridRows_value,gridPoint//gridRows_value]
        if rewardTableFullydefined[initialPoint[0],initialPoint[1]] == aisleReward:
            mazeFullydefinedWithInitialPoint = go.Figure(mazeFullydefined)
            mazeFullydefinedWithInitialPoint.update_traces(overwrite = True,fillcolor = 'firebrick',selector = dict(name = str(gridPoint//gridRows_value) + ',' + str(gridPoint%gridRows_value)))
            mazeSimulationWithoutObstacles = go.Figure(mazeFullydefinedWithInitialPoint)
            shortestPathWithoutObstacles = formStaticMazeSimulationWithoutObstacles(mazeSimulationWithoutObstacles,gridRows_value,gridColumns_value,initialPoint,rewardTableFullydefined,QTable)
            return [mazeSimulationWithoutObstacles,None]
        else:
            return [mazeFullydefined,None]
    elif ctx.triggered_id == 'start-simulation-button':
        formDynamicMazeSimulation(staticMazeForDynamicSimulation,shortestPathForDynamicSimulation,rewardTableFullydefined,obstacleTable,gridRows_value,gridColumns_value)
        return [staticMazeForDynamicSimulation,dash.no_update]
    elif ctx.triggered_id == 'reset-obstacles-button':
        mazeSimulationWithObstacles = go.Figure(mazeSimulationWithoutObstacles)
        shortestPathWithObstacles = shortestPathWithoutObstacles.copy()
        obstacleTable = []
        shortestPathToThePointBeforeObstacle = [initialPoint]
        shortestPathFromThePointBeforeObstacle = shortestPathWithoutObstacles.copy()
        rewardTableFullydefinedWithObstacles = np.copy(rewardTableFullydefined)
        shortestPathForDynamicSimulation = shortestPathWithoutObstacles.copy()
        staticMazeForDynamicSimulation = go.Figure(mazeSimulationWithObstacles)
        figure_update_layout_hovermode(mazeSimulationWithObstacles,'closest')
        return [mazeSimulationWithObstacles,dash.no_update]
    elif ctx.triggered_id == 'maze-figure':
        gridPoint = mazeFigure_clickData['points'][0]['curveNumber'] - 1 - gridRows_value*gridColumns_value
        obstacle = [gridPoint%gridRows_value,gridPoint//gridRows_value]
        if (rewardTableFullydefinedWithObstacles[obstacle[0],obstacle[1]] == aisleReward) and (obstacle not in shortestPathToThePointBeforeObstacle) and (obstacle in shortestPathFromThePointBeforeObstacle):
            mazeSimulationWithObstacles = go.Figure(mazeFullydefinedWithInitialPoint)
            obstacleTable.append(obstacle)
            for iyx in obstacleTable:
                mazeSimulationWithObstacles.update_traces(overwrite = True,fillcolor = 'turquoise',selector = dict(name = str(iyx[1]) + ',' + str(iyx[0])))
            if shortestPathFromThePointBeforeObstacle[1:shortestPathFromThePointBeforeObstacle.index(obstacle)] != []:
                shortestPathToThePointBeforeObstacle += shortestPathFromThePointBeforeObstacle[1:shortestPathFromThePointBeforeObstacle.index(obstacle)]
            rewardTableFullydefinedWithObstacles[obstacle[0],obstacle[1]] = wallReward
            QTableWithObstacles = np.zeros((gridRows_value,gridColumns_value,4))
            algorithmTraining(currentSessionEpisodes_value,gridRows_value,gridColumns_value,rewardTableFullydefinedWithObstacles,discountFactor_value,greedyPolicy_value,learningRate_value,QTableWithObstacles)
            shortestPathFromThePointBeforeObstacle = formStaticMazeSimulationWithObstacles(mazeSimulationWithObstacles,gridRows_value,gridColumns_value,shortestPathToThePointBeforeObstacle,rewardTableFullydefinedWithObstacles,QTableWithObstacles)
            shortestPathWithObstacles = shortestPathToThePointBeforeObstacle[:-1] + shortestPathFromThePointBeforeObstacle
            return [mazeSimulationWithObstacles,None]
        else:
            return [dash.no_update,None]
    elif obstaclesButton_value == 'off':
        figure_update_layout_hovermode(mazeSimulationWithObstacles,'closest')
        return [mazeSimulationWithObstacles,dash.no_update]
    else:
        figure_update_layout_hovermode(mazeSimulationWithObstacles,False)
        shortestPathForDynamicSimulation = shortestPathWithObstacles
        staticMazeForDynamicSimulation = go.Figure(mazeSimulationWithObstacles)
        return [mazeSimulationWithObstacles,dash.no_update]


@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'current-session-episodes',
            component_property = 'value'
        )
    ],
    [
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
            component_id = 'train-episodes',
            component_property = 'value'
        ),
        State(
            component_id = 'grid-rows',
            component_property = 'value'
        ),
        State(
            component_id = 'grid-columns',
            component_property = 'value'
        ),
        State(
            component_id = 'discount-factor',
            component_property = 'value'
        ),
        State(
            component_id = 'greedy-policy',
            component_property = 'value'
        ),
        State(
            component_id = 'learning-rate',
            component_property = 'value'
        ),
        State(
            component_id = 'current-session-episodes',
            component_property = 'value'
        )
    ],
    prevent_initial_call = True
)

def current_session_episodes_value_function(algorithmParametersButton_value,trainAlgorithmButton_n_clicks,resetSessionButton_n_clicks,trainEpisodes_value,gridRows_value,gridColumns_value,discountFactor_value,greedyPolicy_value,learningRate_value,currentSessionEpisodes_value):
    if ctx.triggered_id == 'train-algorithm-button':
        if aisleReward in rewardTableFullydefined:
            algorithmTraining(trainEpisodes_value,gridRows_value,gridColumns_value,rewardTableFullydefined,discountFactor_value,greedyPolicy_value,learningRate_value,QTable)
            return [currentSessionEpisodes_value + trainEpisodes_value]
        else:
            return [dash.no_update]
    else:
        return [0]
    

@Maze_Follower_App.callback(
    [
        Output(
            component_id = 'reset-obstacles-button',
            component_property = 'disabled'
        )
    ],
    [
        Input(
            component_id = 'initial-point-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'obstacles-button',
            component_property = 'value'
        ),
        Input(
            component_id = 'reset-obstacles-button',
            component_property = 'n_clicks'
        ),
        Input(
            component_id = 'maze-figure',
            component_property = 'clickData'
        )
    ],
    prevent_initial_call = True
)

def reset_obstacles_button_disabled_function(initialPointButton_value,obstaclesButton_value,resetObstaclesButton_n_clicks,mazeFigure_clickData):
    if initialPointButton_value == 'off' or obstaclesButton_value == 'on' or obstacleTable == []:
        return [True]
    else:
        return [False]



def formMaze(figure,rows,columns):
    figure.update_layout(
        font = dict(
            family = 'Bahnschrift'
        ),
        grid = dict(
            columns = 1,
            rows = 1
        ),
        hovermode = False,
        hoverlabel = dict(
            bgcolor = 'white',
            bordercolor = 'black',
            namelength = 0,
            font = dict(
                color = 'white',
                size = 1
            ),
            grouptitlefont = dict(
                color = 'white',
                size = 1
            )
        ),
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
    formFilledSquare(figure,0,0,'white','skip')
    for ix in range(columns):
      for iy in range(rows):
        formFilledSquare(figure,0,0,'white','skip')
    for ix in range(columns):
      for iy in range(rows):
        formFilledSquare(figure,ix,iy,'white','all')
    for ix in range(columns):
      formNumericGuides(figure,ix + 0.5,- 0.5,ix + 1)
      formNumericGuides(figure,ix + 0.5,rows + 0.5,ix + 1)
    for iy in range(rows):
      formNumericGuides(figure,- 0.5,iy + 0.5,iy + 1)
      formNumericGuides(figure,columns + 0.5,iy + 0.5,iy + 1)


def formFilledSquare(figure,ix,iy,squareColour,hoverinformation):
    figure.add_scatter(
        fill = 'toself',
        fillcolor = squareColour,
        hoverinfo = hoverinformation,
        line = dict(
            color = 'black'
        ),
        mode = 'lines',
        name = str(ix) + ',' + str(iy),
        showlegend = False,
        x = [ix,ix + 1,ix + 1,ix,ix],
        y = [iy,iy,iy + 1,iy + 1,iy]
    )


def formNumericGuides(figure,ix,iy,guideNumber):
    figure.add_scatter(
        hoverinfo = 'skip',
        mode = 'text',
        showlegend = False,
        text = guideNumber,
        textposition = 'middle center',
        x = [ix],
        y = [iy]
    )
   

def figure_update_layout_hovermode(figure,status):
    figure.update_layout(
        hovermode = status
    )


def algorithmTraining(trainingEpisodes,rows,columns,currentRewardTable,currentDiscountFactor,currentGreedyPolicy,currentLearningRate,currentQTable):
    for episode in range(trainingEpisodes):
        currentRow,currentColumn = startingLocation(rows,columns,currentRewardTable) #Except for the variables rows and columns, 0th row and column are considered
        while not terminalState(currentRow,currentColumn,currentRewardTable):
            actionIndex = nextAction(currentRow,currentColumn,currentGreedyPolicy,currentQTable) #actionIndex: Action taken next(0: Right,1: Up,2: Left,3: Down)
            nextRow,nextColumn = nextLocation(rows,columns,currentRow,currentColumn,actionIndex)
            updateQTable(currentRewardTable,currentQTable,currentRow,currentColumn,nextRow,nextColumn,actionIndex,currentDiscountFactor,currentLearningRate)
            currentRow,currentColumn = nextRow,nextColumn


def startingLocation(rows,columns,currentRewardTable):
    initialRow = np.random.randint(rows)
    initialColumn = np.random.randint(columns)
    while terminalState(initialRow,initialColumn,currentRewardTable):
        initialRow = np.random.randint(rows)
        initialColumn = np.random.randint(columns)
    return initialRow,initialColumn


def terminalState(currentRow,currentColumn,currentRewardTable):
    if currentRewardTable[currentRow,currentColumn] == aisleReward:
        return False
    else:
        return True
    

def nextAction(currentRow,currentColumn,currentGreedyPolicy,currentQTable):
    if np.random.random() < currentGreedyPolicy:
        return np.argmax(currentQTable[currentRow,currentColumn])
    else:
        return np.random.randint(4)
    

def nextLocation(rows,columns,currentRow,currentColumn,actionIndex):
    if actionIndex == 0 and currentColumn < columns - 1: #actionIndex = 0: Next action - Right
        currentColumn += 1
    elif actionIndex == 1 and currentRow < rows - 1: #actionIndex = 1: Next action - Up
        currentRow += 1
    elif actionIndex == 2 and currentColumn > 0: #actionIndex = 2: Next action - Left
        currentColumn -= 1
    elif actionIndex == 3 and currentRow > 0: #actionIndex = 3: Next action - Down
        currentRow -= 1
    return currentRow,currentColumn


def updateQTable(currentRewardTable,currentQTable,currentRow,currentColumn,nextRow,nextColumn,actionIndex,currentDiscountFactor,currentLearningRate):
    reward = currentRewardTable[nextRow,nextColumn]
    QValueCurrent = currentQTable[currentRow,currentColumn,actionIndex]
    temporalDifference = reward + (currentDiscountFactor*np.max(currentQTable[nextRow,nextColumn])) - QValueCurrent
    QValueUpdate = QValueCurrent + (currentLearningRate*temporalDifference)
    currentQTable[currentRow,currentColumn,actionIndex] = QValueUpdate


def formStaticMazeSimulationWithoutObstacles(figure,rows,columns,currentInitialPoint,currentRewardTable,currentQTable):
    shortestPath = shortestPathCoordinates(rows,columns,currentInitialPoint,currentRewardTable,currentQTable)
    if currentRewardTable[shortestPath[-1][0],shortestPath[-1][1]] == aisleReward:
        figure.update_traces(overwrite = True,fillcolor = 'sienna',selector = dict(name = str(shortestPath[-1][1]) + ',' + str(shortestPath[-1][0])))
    for iyx in shortestPath:
        formFilledSquareForFollower(figure,iyx[1],iyx[0])
    return shortestPath


def formStaticMazeSimulationWithObstacles(figure,rows,columns,currentShortestPathToThePointBeforeObstacle,currentRewardTable,currentQTable):
    shortestPath = shortestPathCoordinates(rows,columns,currentShortestPathToThePointBeforeObstacle[-1],currentRewardTable,currentQTable)
    if currentRewardTable[shortestPath[-1][0],shortestPath[-1][1]] == aisleReward:
        figure.update_traces(overwrite = True,fillcolor = 'sienna',selector = dict(name = str(shortestPath[-1][1]) + ',' + str(shortestPath[-1][0])))
    for iyx in currentShortestPathToThePointBeforeObstacle:
        formFilledSquareForFollower(figure,iyx[1],iyx[0])
    for iyx in shortestPath:
        formFilledSquareForFollower(figure,iyx[1],iyx[0])
    return shortestPath


def formDynamicMazeSimulation(figure,currentShortestPath,currentRewardTable,currentObstacleTable,rows,columns):
    for ix in range(columns):
      for iy in range(rows):
        formDynamicMazeEmptySquareGrid(figure,ix + columns + 1,iy)
    for ix in range(columns):
      formNumericGuides(figure,ix + 0.5 + columns + 1,- 0.5,ix + 1)
      formNumericGuides(figure,ix + 0.5 + columns + 1,rows + 0.5,ix + 1)
    for iy in range(rows):
      formNumericGuides(figure,columns + 0.5 + columns + 1,iy + 0.5,iy + 1)
    dynamicMazeStaticObject = formDynamicMazeStaticObject(currentShortestPath,currentRewardTable,currentObstacleTable,columns)
    figure.frames = tuple(go.Frame(data = dynamicMazeStaticObject + [formFilledSquareForFollowerObject(iyx[1] + columns + 1,iyx[0])]) for iyx in currentShortestPath)
    figure = updateMenus(figure)
    return figure


def shortestPathCoordinates(rows,columns,currentInitialPoint,currentRewardTable,currentQTable):
    currentRow = currentInitialPoint[0]
    currentColumn = currentInitialPoint[1]
    shortestPath = [[currentRow,currentColumn]]
    while not terminalState(currentRow,currentColumn,currentRewardTable):
        actionIndex = nextAction(currentRow,currentColumn,1,currentQTable)
        nextRow,nextColumn = nextLocation(rows,columns,currentRow,currentColumn,actionIndex)
        if [nextRow,nextColumn] in shortestPath:
            return shortestPath
        currentRow,currentColumn = nextRow,nextColumn
        shortestPath.append([currentRow,currentColumn])
    return shortestPath


def formFilledSquareForFollower(figure,ix,iy):
    figure.add_scatter(
        fill = 'toself',
        fillcolor = 'darkorange',
        hoverinfo = 'skip',
        line = dict(
            color = 'black',
            shape = 'spline'
        ),
        mode = 'lines',
        showlegend = False,
        x = [ix + 0.20,ix + 0.80,ix + 0.80,ix + 0.20,ix + 0.20],
        y = [iy + 0.20,iy + 0.20,iy + 0.80,iy + 0.80,iy + 0.20]
    )


def formDynamicMazeEmptySquareGrid(figure,ix,iy):
    figure.add_scatter(
        hoverinfo = 'skip',
        line = dict(
            color = 'black'
        ),
        mode = 'lines',
        name = str(ix) + ',' + str(iy),
        showlegend = False,
        x = [ix,ix + 1,ix + 1,ix,ix],
        y = [iy,iy,iy + 1,iy + 1,iy]
    )


def formDynamicMazeStaticObject(currentShortestPath,currentRewardTable,currentObstacleTable,columns):
    dynamicMazeStaticObject = []
    wallArray = np.argwhere(currentRewardTable == wallReward)
    for iyx in wallArray:
        dynamicMazeStaticObject.append(formFilledSquareForDynamicMazeStaticObject(iyx[1] + columns + 1,iyx[0],'darkslategrey'))
    for iyx in currentObstacleTable:
        dynamicMazeStaticObject.append(formFilledSquareForDynamicMazeStaticObject(iyx[1] + columns + 1,iyx[0],'turquoise'))
    dynamicMazeStaticObject.append(formFilledSquareForDynamicMazeStaticObject(currentShortestPath[0][1] + columns + 1,currentShortestPath[0][0],'firebrick'))
    destinationPoint = np.argwhere(currentRewardTable == destinationReward)[0]
    dynamicMazeStaticObject.append(formFilledSquareForDynamicMazeStaticObject(destinationPoint[1] + columns + 1,destinationPoint[0],'forestgreen'))
    if currentRewardTable[currentShortestPath[-1][0],currentShortestPath[-1][1]] != destinationReward:
        dynamicMazeStaticObject.append(formFilledSquareForDynamicMazeStaticObject(currentShortestPath[-1][1] + columns + 1,currentShortestPath[-1][0],'sienna'))
    return dynamicMazeStaticObject


def formFilledSquareForDynamicMazeStaticObject(ix,iy,squareColour):
    return go.Scatter(
        fill = 'toself',
        fillcolor = squareColour,
        hoverinfo = 'skip',
        line = dict(
            color = 'black'
        ),
        mode = 'lines',
        showlegend = False,
        x = [ix,ix + 1,ix + 1,ix,ix],
        y = [iy,iy,iy + 1,iy + 1,iy]
    ) 


def formFilledSquareForFollowerObject(ix,iy):
    return go.Scatter(
        fill = 'toself',
        fillcolor = 'darkorange',
        hoverinfo = 'skip',
        line = dict(
            color = 'black',
            shape = 'spline'
        ),
        mode = 'lines',
        showlegend = False,
        x = [ix + 0.20,ix + 0.80,ix + 0.80,ix + 0.20,ix + 0.20],
        y = [iy + 0.20,iy + 0.20,iy + 0.80,iy + 0.80,iy + 0.20]
    )


def updateMenus(figure):
    figure.layout.updatemenus = [
        dict(
            bgcolor = 'white',
            bordercolor = 'white',
            borderwidth = 3,
            buttons = [
                dict(
                    args = [
                        None,
                        dict(
                            fromcurrent = True,
                            frame = dict(
                                duration = transitionDuration
                            )
                        )
                    ],
                    label = '<b>Play</b>',
                    method = 'animate'
                ),
                dict(
                    args = [
                        [
                            None
                        ],
                        dict(
                            mode = 'immediate'
                        )
                    ],
                    label = '<b>Pause</b>',
                    method = 'animate'
                ),
                dict(
                    args = [
                        None,
                        dict(
                            fromcurrent = False,
                            frame = dict(
                                duration = transitionDuration,
                                redraw = True
                            )
                        )
                    ],
                    label = '<b>Restart</b>',
                    method = 'animate'
                )
            ],
            direction = 'up',
            font = dict(
                size = 14
            ),
            pad = dict(
                b = 0,
                l = 0,
                r = 1,
                t = 0
            ),
            showactive = True,
            type = 'buttons',
            x = 1,
            xanchor = 'left',
            y = 0.5,
            yanchor = 'middle'
        )
    ]



if __name__ == '__main__':
    Maze_Follower_App.run_server(debug = True)