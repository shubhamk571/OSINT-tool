import requests

def check_profiles(username):
    social_sites = {
        "GitHub": f"https://github.com/{username}",
        "Twitter": f"https://x.com/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
    }

    results = {}
    headers = {"User-Agent": "Mozilla/5.0"}

    for site, url in social_sites.items():
        try:
            resp = requests.get(url, headers=headers, timeout=5)
            results[site] = "Found" if resp.status_code == 200 else "Not Found"
        except Exception as e:
            results[site] = f"Error: {e}"
    return results
