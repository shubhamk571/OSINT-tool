import re
import socket

def check_email(email):
    info = {"email": email, "valid_syntax": False, "mx_record": None}
    try:
        # Simple regex validation
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        info["valid_syntax"] = bool(re.match(pattern, email))

        domain = email.split("@")[1]
        mx_records = socket.getaddrinfo(domain, None)
        info["mx_record"] = [r[4][0] for r in mx_records if r[4]]
    except Exception as e:
        info["error"] = str(e)
    return info
