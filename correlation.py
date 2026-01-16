def calculate_risk(ctx):
    score = 0
    score += len(ctx.get("admin", [])) * 3
    if ctx.get("cors", {}).get("risk") == "HIGH":
        score += 3
    if ctx.get("waf") == "None":
        score += 2
    if score >= 7: return "HIGH"
    if score >= 4: return "MEDIUM"
    return "LOW"
