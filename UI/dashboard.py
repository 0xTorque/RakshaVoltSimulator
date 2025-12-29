# © 2025 Aryan Kumbhare. All Rights Reserved.
# Raksha Volt Simulator v1.0 – Virtual BMS Dashboard
# Unauthorized commercial use prohibited.
# License: AGPL v3 (Open-source for learning/research)
# Commercial use requires separate license.


import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots


def launch_dashboard(csv_path, soc, bms_state,fault=None):
    df = pd.read_csv(csv_path)

    fig = make_subplots(
        rows=2,
        cols=2,
        subplot_titles=(
            "Pack Voltage Behavior",
            "Thermal Profile",
            "Battery State of Charge",
            "System Safety Status"
        ), 
        specs=[[{}, {}], [{"type": "indicator"}, {"type": "indicator"}]],
    vertical_spacing=0.12,
    horizontal_spacing=0.08
    ) 

    # Voltage plot
    fig.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["Voltage"],
            name="Voltage (V)"
        ),
        row=1,
        col=1
    )

    # Temperature plot
    fig.add_trace(
        go.Scatter(
            x=df["Time"],
            y=df["Temperature"],
            name="Temperature (°C)"
        ),
        row=1,
        col=2
    )

    # SOC Gauge
    fig.add_trace(
    go.Indicator(
        mode="gauge+number",
        value=soc,
        title={"text": "SOC (%)"},
        gauge={"axis": {"range": [0, 100]}}
    ),
    row=2,
    col=1
)

    # BMS State Indicator
    color = (
        "green"
        if bms_state == "NORMAL_OPERATION"
        else "orange"
        if bms_state == "LIMITED_POWER"
        else "red"
    )

    fig.add_trace(
        go.Indicator(
            mode="number",
            value=1,
            title={"text": "BMS STATE"},
            number={
                "prefix": f"{bms_state} ",
                "font": {"color": color, "size": 40}
            }
        ),
        row=2,
        col=2
    )
# Add Fault Indicator if any
    if fault:
        fig.add_trace(
        go.Indicator(
            mode="number",
            value=1,
            title={"text": f"FAULT: {fault}"},
            number={"font": {"color": "red", "size": 30}}
        ),
        row=2,
        col=2  # Or add a new row/col for clarity
    )

    # Product banner
    fig.add_annotation(
        text=f"<b>Raksha Volt Sim™ | Virtual BMS Simulator | STATUS: {bms_state}</b>",
        x=0.5,
        y=1.15,
        xref="paper",
        yref="paper",
        showarrow=False,
        font=dict(size=18, color="white")
    )

    # Dark automotive theme
    fig.update_layout(
        template="plotly_dark",
        font=dict(family="Segoe UI", size=14),
        paper_bgcolor="#0b1220",
        plot_bgcolor="#0b1220",
        height=720,
        showlegend=False,
        title_text="Raksha Volt Sim™ – Virtual BMS Dashboard"
    ) 

    fig.update_layout(
    margin=dict(
        l=60,
        r=60,
        t=90,
        b=60
    ),
    legend=dict(
        orientation="h",
        x=0.5,
        y=-0.25,
        xanchor="center"
    )
) # spacing + legend fix

    fig.show()
