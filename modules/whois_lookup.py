import whois

def get_whois_info(domain):
    try:
        data = whois.whois(domain)
        return {
            "domain_name": data.domain_name,
            "registrar": data.registrar,
            "creation_date": str(data.creation_date),
            "expiration_date": str(data.expiration_date),
            "emails": data.emails,
            "country": data.country,
        }
    except Exception as e:
        return {"error": str(e)}
