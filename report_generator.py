import json
from datetime import datetime

def generate_report(results, filename):
    report = {
        "timestamp": str(datetime.utcnow()),
        "intelligence_data": results
    }
    with open(filename, "w") as f:
        json.dump(report, f, indent=4)
