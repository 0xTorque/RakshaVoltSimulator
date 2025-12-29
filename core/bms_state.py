# © 2025 Aryan Kumbhare. All Rights Reserved.
# Raksha Volt Simulator v1.0 – Virtual BMS Dashboard
# Unauthorized commercial use prohibited.
# License: AGPL v3 (Open-source for learning/research)
# Commercial use requires separate license.


from core.safety_logic import check_safety

def get_bms_state(voltage, temperature, soc):
    safety = check_safety(voltage, temperature)

    if safety == "CRITICAL":
        return "SHUTDOWN"
    elif safety == "WARNING":
        return "LIMITED_POWER"
    else:
        return "NORMAL_OPERATION"
