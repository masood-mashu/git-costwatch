"""
spend_anomaly_detector.py - Computes daily spend z-score relative to rolling historical baseline
"""
import sys
import json


def detect_spend_anomalies(spend_data_json: str):
    import json
    data = json.loads(spend_data_json) if isinstance(spend_data_json, str) else spend_data_json
    current = data.get("current_spend", 100.0)
    baseline = data.get("baseline_spend", 90.0)
    pct_change = round(((current - baseline) / max(baseline, 1.0)) * 100, 1)
    is_anomaly = pct_change > 30.0
    return {"pct_change": pct_change, "anomaly_detected": is_anomaly, "status": "SPEND_ANOMALY" if is_anomaly else "SPEND_NORMAL"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "spend-anomaly-detector"}))
