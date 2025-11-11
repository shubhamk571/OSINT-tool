import dns.resolver

def get_dns_info(domain):
    records = {}
    try:
        for record_type in ["A", "MX", "NS", "TXT", "CNAME"]:
            try:
                answers = dns.resolver.resolve(domain, record_type)
                records[record_type] = [r.to_text() for r in answers]
            except Exception:
                records[record_type] = []
    except Exception as e:
        records["error"] = str(e)
    return records
