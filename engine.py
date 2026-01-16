from core.recon import dns, http, ssl, headers, cors, waf
from core.exposure import admin_panels, buckets, apis
from core.scoring.correlation import calculate_risk
from core.scoring.explain import explain

def scan(target: str) -> dict:
    ctx = {"target": target}
    ctx["dns"] = dns.run(target)
    ctx["http"] = http.run(target)
    ctx["ssl"] = ssl.run(target)
    ctx["headers"] = headers.run(target)
    ctx["cors"] = cors.run(target)
    ctx["waf"] = waf.run(target)
    ctx["admin"] = admin_panels.run(target)
    ctx["buckets"] = buckets.run(target)
    ctx["apis"] = apis.run(target)
    ctx["risk"] = calculate_risk(ctx)
    ctx["explain"] = explain(ctx)
    return ctx
