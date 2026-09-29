"""
eval_predictability.py - Checkpoint 02 Benchmark Suite for GitCostWatch.
"""
import os, sys, unittest
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from tools.spend_anomaly_detector import *
from tools.idle_resource_reclaimer import *
from tools.reservation_coverage_scorer import *

class TestGitCostWatchPredictability(unittest.TestCase):
    def test_spend_anomaly_detector(self):
        res = detect_spend_anomalies('{"current_spend": 98.0, "baseline_spend": 95.0}')
        self.assertFalse(res["anomaly_detected"])
        self.assertEqual(res["status"], "SPEND_NORMAL")

    def test_idle_resource_reclaimer(self):
        res = reclaim_idle_resources('[{"id": "vol-123", "idle_days": 10, "monthly_cost": 45.0}]')
        self.assertEqual(res["idle_count"], 1)
        self.assertEqual(res["status"], "IDLE_RESOURCES_FLAGGED")

    def test_reservation_coverage_scorer(self):
        res = score_reservation_coverage('{"covered_hours": 850, "total_hours": 1000}')
        self.assertEqual(res["coverage_pct"], 85.0)
        self.assertEqual(res["status"], "COVERAGE_OPTIMAL")


if __name__ == "__main__":
    unittest.main()
