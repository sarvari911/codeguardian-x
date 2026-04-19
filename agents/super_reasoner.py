import time
from core.router import route_task

def reason_cross_file(nano_findings):
    """
    Simulates Nemotron 3 Super taking findings and performing cross-file reasoning.
    """
    time.sleep(2.5)
    
    routing_decision = route_task("Cross-module attack chain", "high")
    
    # We simulate that the Super Reasoner connects the auth string to the query builder
    attack_chains = [
        {
            "id": 1,
            "path": "auth.py -> query_builder.py -> admin_panel.py",
            "type": "SQL Injection -> Privilege Escalation",
            "severity": "CRITICAL",
            "cvss": 9.8
        }
    ]
    
    return attack_chains, routing_decision
