from datetime import datetime, date

import dash_mantine_components as dmc
from dash import Input, Output, html
from dash.exceptions import PreventUpdate

component = html.Div(
    [
        dmc.DatePicker(
            id="date-picker",
            label="Start Date",
            description="You can also provide a description",
            minDate=date(2020, 8, 5),
            maxDate=date(2022, 9, 19),
            date=datetime.now().date(),
        ),
        dmc.Space(h=10),  # no-prism
        dmc.Text(id="selected-date"),
    ]
)


@app.callback(Output("selected-date", "children"), Input("date-picker", "date"))
def update_output(d):
    prefix = "You have selected: "
    if d:
        return prefix + d
    else:
        raise PreventUpdate
