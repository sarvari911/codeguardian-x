import time
from core.router import route_task

def run_fast_scan():
    """
    Simulates Nemotron 3 Nano scanning files for syntax and simple patterns.
    """
    time.sleep(1.5)
    
    routing_decision = route_task("File-level syntax scan", "low")
    
    findings = [
        {"file": "api/routes/auth.py", "line": 47, "issue": "Unsanitized string input detected", "severity": "Medium"},
        {"file": "db/query_builder.py", "line": 112, "issue": "No parameterization in SQL query", "severity": "High"},
        {"file": "utils/logger.py", "line": 22, "issue": "Hardcoded debug token", "severity": "Low"}
    ]
    
    return findings, routing_decision
