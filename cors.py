import requests
def run(target):
    try:
        r = requests.get(f"https://{target}", headers={"Origin": "https://evil.com"}, timeout=5)
        if r.headers.get("Access-Control-Allow-Origin") == "*":
            return {"risk": "HIGH"}
        return {"risk": "LOW"}
    except:
        return {"risk": "UNKNOWN"}
