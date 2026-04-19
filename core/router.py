import time

def route_task(task_description, complexity):
    """
    Simulates the routing logic between Nemotron 3 Nano and Super.
    """
    time.sleep(0.5)
    if complexity == "low":
        return {
            "model": "Nemotron 3 Nano",
            "rationale": "Fast pattern match, low complexity",
            "confidence": "97%"
        }
    else:
        return {
            "model": "Nemotron 3 Super",
            "rationale": "Multi-hop reasoning required",
            "confidence": "91%"
        }
