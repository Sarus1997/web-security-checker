def analyze_stack(headers):
    tech_info = []

    server = headers.get("Server", "")
    x_powered_by = headers.get("X-Powered-By", "")

    if "apache" in server.lower():
        tech_info.append("🧱 Server: Apache")
    elif "nginx" in server.lower():
        tech_info.append("🧱 Server: Nginx")
    elif "iis" in server.lower():
        tech_info.append("🧱 Server: Microsoft IIS")
    elif "cloudflare" in server.lower():
        tech_info.append("🧱 CDN/Proxy: Cloudflare")
    elif server:
        tech_info.append(f"🧱 Server: {server}")

    if "express" in x_powered_by.lower():
        tech_info.append("🛠️ Framework: Express (Node.js)")
    elif "php" in x_powered_by.lower():
        tech_info.append("🛠️ Language: PHP")
    elif "asp.net" in x_powered_by.lower():
        tech_info.append("🛠️ Framework: ASP.NET")
    elif x_powered_by:
        tech_info.append(f"🛠️ Powered by: {x_powered_by}")

    return tech_info
