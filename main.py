# © 2025 Aryan Kumbhare. All Rights Reserved.
# Raksha Volt Simulator v1.0 – Virtual BMS Dashboard
# Unauthorized commercial use prohibited.
# License: AGPL v3 (Open-source for learning/research)
# Commercial use requires separate license.

from core.battery_simulator import generate_battery_data, generate_fault
from core.soc_estimator import estimate_soc
from core.bms_state import get_bms_state
from ui.dashboard import launch_dashboard
import pandas as pd
import os

# 1. Generate battery data
csv_path = generate_battery_data()
print("Raksha Volt Simulator: Battery data generated successfully")

# 2. Read CSV
df = pd.read_csv(csv_path)

# 3. Get latest voltage and temperature
latest_voltage = df["Voltage"].iloc[-1]
latest_temp = df["Temperature"].iloc[-1]

# 4. Estimate SOC
soc = estimate_soc(latest_voltage)
print(f"Latest Voltage: {latest_voltage} V")
print(f"Estimated State of Charge (SOC): {soc} %")

# 5. Determine BMS state
bms_state = get_bms_state(latest_voltage, latest_temp, soc)

# 6. Generate fault (this was missing)
fault = generate_fault(latest_voltage, latest_temp)

# 7. Log events
os.makedirs("data", exist_ok=True)
with open("data/events.log", "a", encoding="utf-8") as f:
    f.write(f"BMS STATE → {bms_state}\n")
    if fault:
        f.write(f"FAULT DETECTED → {fault}\n")

# 8. Launch dashboard
launch_dashboard(csv_path, soc, bms_state)


