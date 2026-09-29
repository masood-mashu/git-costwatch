"""
idle_resource_reclaimer.py - Audits compute and storage for zero-utilization thresholds across multi-cloud accounts
"""
import sys
import json


def reclaim_idle_resources(resource_inventory_json: str):
    import json
    resources = json.loads(resource_inventory_json) if isinstance(resource_inventory_json, str) else resource_inventory_json
    idle = [r for r in resources if r.get("idle_days", 0) >= 7]
    savings = sum(r.get("monthly_cost", 20.0) for r in idle)
    return {"idle_count": len(idle), "potential_savings_usd": round(savings, 2), "status": "IDLE_RESOURCES_FLAGGED" if len(idle) > 0 else "NO_IDLE_RESOURCES"}


if __name__ == "__main__":
    print(json.dumps({"status": "READY", "tool": "idle-resource-reclaimer"}))
