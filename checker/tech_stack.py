def analyze_stack(headers, body_text=""):
    tech_info = []

    server = headers.get("Server", "")
    x_powered_by = headers.get("X-Powered-By", "")

    # Server
    if "apache" in server.lower():
        tech_info.append("🧱 Server: Apache")
    elif "nginx" in server.lower():
        tech_info.append("🧱 Server: Nginx")
    elif "iis" in server.lower():
        tech_info.append("🧱 Server: Microsoft IIS")
    elif "cloudflare" in server.lower():
        tech_info.append("🧱 CDN/Proxy: Cloudflare")
    elif "vercel" in server.lower():
        tech_info.append("🧱 Server: Vercel")
        tech_info.append("☁️ Hosting: Vercel")
    elif "netlify" in server.lower():
        tech_info.append("🧱 Server: Netlify")
        tech_info.append("☁️ Hosting: Netlify")
    elif server:
        tech_info.append(f"🧱 Server: {server}")

    # X-Powered-By
    if "express" in x_powered_by.lower():
        tech_info.append("🛠️ Framework: Express (Node.js)")
    elif "php" in x_powered_by.lower():
        tech_info.append("🛠️ Language: PHP")
    elif "asp.net" in x_powered_by.lower():
        tech_info.append("🛠️ Framework: ASP.NET")
    elif x_powered_by:
        tech_info.append(f"🛠️ Powered by: {x_powered_by}")

    # HTML Signature Detection (Simple)
    if "React" in body_text or "__REACT_DEVTOOLS_GLOBAL_HOOK__" in body_text:
        tech_info.append("⚛️ Frontend: React")
    if "__NEXT_DATA__" in body_text:
        tech_info.append("🚀 Framework: Next.js")
    if "Vue" in body_text or "__VUE_DEVTOOLS_GLOBAL_HOOK__" in body_text:
        tech_info.append("🖖 Framework: Vue.js")
    if "nuxt" in body_text.lower():
        tech_info.append("🚀 Framework: Nuxt.js")
    if "ng-version" in body_text.lower():
        tech_info.append("🅰️ Framework: Angular")
    if "openai" in body_text.lower():
        tech_info.append("🤖 AI: Possibly using OpenAI/ChatGPT")

    return tech_info