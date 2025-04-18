import matplotlib.pyplot as plt
import base64
from io import BytesIO

def run_analysis(data):
    cities = data.get("cities", [])
    base = {
        "Dallas": {"roi": 1.89, "net_profit": 2416.0, "esg": 4, "risk": 3, "market": 5},
        "Los Angeles": {"roi": 1.28, "net_profit": 2245.8, "esg": 5, "risk": 2, "market": 4},
        "Phoenix": {"roi": 1.63, "net_profit": 2357.7, "esg": 3, "risk": 2.5, "market": 3}
    }

    weights = data["weights"]
    results = []
    roi_vals = []
    for city in cities:
        b = base[city]
        score = b["roi"] * (weights["roi"]/100) + b["esg"] * (weights["esg"]/100) - b["risk"] * (weights["risk"]/100) + b["market"] * (weights["market"]/100)
        results.append({"city": city, "roi": round(b["roi"], 2), "net_profit": round(b["net_profit"], 1), "score": round(score, 2)})
        roi_vals.append(b["roi"])

    fig, ax = plt.subplots(figsize=(6,4))
    ax.bar(cities, roi_vals, color='steelblue')
    ax.set_title("ROI 对比")
    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    roi_chart = base64.b64encode(buf.read()).decode("utf-8")
    plt.close()

    results.sort(key=lambda x: x["score"], reverse=True)
    return {"results": results, "roi_chart": roi_chart}
