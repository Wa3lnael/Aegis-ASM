import requests
COMMON = ["/admin", "/login", "/dashboard"]
def run(target):
    found = []
    for p in COMMON:
        try:
            r = requests.get(f"https://{target}{p}", timeout=5)
            if r.status_code == 200:
                found.append(p)
        except:
            pass
    return found
