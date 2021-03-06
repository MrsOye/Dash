from dash import dcc, html
import dash_bootstrap_components as dbc
import dash_trich_components as dtc
from Stylee import cardbody_style, card_icon, cardimg_style, card_style



def output_card(card_id: str = None, card_label: str =None,
                style={"backgroundColor": 'yellow'}, 
                icon: str ='bi bi-cash-coin', card_size: int = 4):
    return dbc.Col(lg=card_size,
                    children=dbc.CardGroup(
                        children=[
                            dbc.Card(
                                    children=[
                                        html.H3(id=card_id),
                                        html.P(card_label)
                                    ]
                                ),
                            dbc.Card(
                                    children=[
                                        html.Div(
                                            className=icon,
                                            style=card_icon
                                        )
                                    ],
                                    style=style
                            )
                        ]
                    )
                )
