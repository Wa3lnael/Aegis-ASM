def format_report(r):
    msg = f"Target: {r['target']}\nRisk: {r['risk']}\n"
    for x in r['explain']:
        msg += f"- {x}\n"
    return msg
