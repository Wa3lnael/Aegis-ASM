import requests
def run(target):
    try:
        r = requests.get(f"https://{target}", timeout=5)
        return {"status": r.status_code}
    except:
        return None
