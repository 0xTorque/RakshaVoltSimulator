# © 2025 Aryan Kumbhare. All Rights Reserved.
# Raksha Volt Simulator v1.0 – Virtual BMS Dashboard
# Unauthorized commercial use prohibited.
# License: AGPL v3 (Open-source for learning/research)
# Commercial use requires separate license.


def estimate_soc(voltage):
    """
    Simple SOC estimation based on voltage
    Assumption: 
    4.2V = 100%
    3.0V = 0%
    """

    min_v = 3.0
    max_v = 4.2

    soc = (voltage - min_v) / (max_v - min_v) * 100
    soc = max(0, min(100, soc))  # clamp between 0–100

    return round(soc, 2)
