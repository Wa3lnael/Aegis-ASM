import requests
def run(target):
    try:
        r = requests.get(f"https://{target}", timeout=5)
        if "cloudflare" in r.headers.get("Server","").lower():
            return "Cloudflare"
        return "None"
    except:
        return "Unknown"
