def explain(ctx):
    reasons = []
    if ctx.get("admin"):
        reasons.append("Public admin interfaces detected")
    if ctx.get("cors", {}).get("risk") == "HIGH":
        reasons.append("Insecure CORS configuration")
    if ctx.get("waf") == "None":
        reasons.append("No WAF detected")
    return reasons
