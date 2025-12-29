# © 2025 Aryan Kumbhare. All Rights Reserved.
# Raksha Volt Simulator v1.0 – Virtual BMS Dashboard
# Unauthorized commercial use prohibited.
# License: AGPL v3 (Open-source for learning/research)
# Commercial use requires separate license.


def check_safety(voltage, temperature):
    if voltage > 4.25 or temperature > 55:
        return "CRITICAL"
    elif voltage > 4.1 or temperature > 45:
        return "WARNING"
    else:
        return "NORMAL"
