import requests
def run(target):
    try:
        r = requests.get(f"https://{target}", timeout=5)
        return dict(r.headers)
    except:
        return {}
