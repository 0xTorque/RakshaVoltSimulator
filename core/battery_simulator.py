# © 2025 Aryan Kumbhare. All Rights Reserved.
# Raksha Volt Simulator v1.0 – Virtual BMS Dashboard
# Unauthorized commercial use prohibited.
# License: AGPL v3 (Open-source for learning/research)
# Commercial use requires separate license.


import numpy as np
import pandas as pd
import os

def generate_battery_data(mode="NORMAL"):
    os.makedirs("data", exist_ok=True)

    time = np.arange(0, 100)

    voltage = 4.2 - 0.005 * time + np.random.normal(0, 0.01, size=len(time))
    current = np.random.uniform(1.5, 3.0, size=len(time))
    temperature = np.random.uniform(25, 35, size=len(time))

    # Scenario modes
    if mode == "HOT":
        temperature += 15
    elif mode == "FAULT":
        voltage += 0.3

    df = pd.DataFrame({
        "Time": time,
        "Voltage": voltage,
        "Current": current,
        "Temperature": temperature
    })

    # Save CSV
    csv_path = "data/battery_data.csv"
    df.to_csv(csv_path, index=False)

    # Return path so main.py can read it
    return csv_path


def generate_fault(voltage, temperature):
    # Over-voltage
    if voltage > 4.2:
        return "OV"  # Over-voltage
    # Under-voltage
    if voltage < 3.0:
        return "UV"  # Under-voltage
    # Over-temp
    if temperature > 60:
        return "OT"  # Over-temp
    return None
