"""
reservation_coverage_scorer.py - Calculates percentage of eligible compute instances covered by RIs or Savings Plans
"""
import sys
import json


def score_reservation_coverage(coverage_metrics_json: str):
    import json
    data = json.loads(coverage_metrics_json) if isinstance(coverage_metrics_json, str) else coverage_metrics_json
    covered = data.get("covered_hours", 800)
    total = data.get("total_hours", 1000)
    pct = round((covered / max(total, 1)) * 100, 1)
    is_optimal = pct >= 75.0
    return {"coverage_pct": pct, "status": "COVERAGE_OPTIMAL" if is_optimal else "COVERAGE_DEFICIT"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "reservation-coverage-scorer"}))
