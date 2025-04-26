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
    elif "railway" in server.lower():
        tech_info.append("☁️ Hosting: Railway")
    elif "firebase" in server.lower():
        tech_info.append("☁️ Hosting: Firebase Hosting")
    elif server:
        tech_info.append(f"🧱 Server: {server}")

    # X-Powered-By
    if "express" in x_powered_by.lower():
        tech_info.append("🛠️ Framework: Express (Node.js)")
    elif "php" in x_powered_by.lower():
        tech_info.append("🛠️ Language: PHP")
    elif "asp.net" in x_powered_by.lower():
        tech_info.append("🛠️ Framework: ASP.NET")
    elif "laravel" in x_powered_by.lower():
        tech_info.append("🛠️ Framework: Laravel (PHP)")
    elif "django" in x_powered_by.lower():
        tech_info.append("🛠️ Framework: Django (Python)")
    elif "rails" in x_powered_by.lower():
        tech_info.append("🛠️ Framework: Ruby on Rails")
    elif x_powered_by:
        tech_info.append(f"🛠️ Powered by: {x_powered_by}")

    # HTML/JS Signature Detection (Simple)
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
    if "svelte" in body_text.lower():
        tech_info.append("🔥 Framework: Svelte")
    if "jquery" in body_text.lower():
        tech_info.append("📜 Library: jQuery")
    if "bootstrap" in body_text.lower():
        tech_info.append("🎨 UI: Bootstrap")
    if "tailwind" in body_text.lower():
        tech_info.append("🎨 UI: Tailwind CSS")
    if "bulma" in body_text.lower():
        tech_info.append("🎨 UI: Bulma CSS")
    if "material-ui" in body_text.lower():
        tech_info.append("🎨 UI: Material UI")

    # Hosting/Backend/Other
    if "cloudflare" in body_text.lower() and "worker" in body_text.lower():
        tech_info.append("⚡ Edge Compute: Cloudflare Workers")
    if "graphql" in body_text.lower():
        tech_info.append("🕸️ API: GraphQL")
    if "socket.io" in body_text.lower():
        tech_info.append("🔌 Real-time: Socket.IO")
    if "firebase" in body_text.lower():
        tech_info.append("🔥 BaaS: Firebase")
    if "supabase" in body_text.lower():
        tech_info.append("🦾 BaaS: Supabase")
    if "strapi" in body_text.lower():
        tech_info.append("🛠️ Headless CMS: Strapi")

    # CMS
    if "wordpress" in body_text.lower():
        tech_info.append("📰 CMS: WordPress")
    if "drupal" in body_text.lower():
        tech_info.append("📰 CMS: Drupal")
    if "joomla" in body_text.lower():
        tech_info.append("📰 CMS: Joomla")
    if "shopify" in body_text.lower():
        tech_info.append("🛒 E-Commerce: Shopify")
    if "magento" in body_text.lower():
        tech_info.append("🛒 E-Commerce: Magento")

    # AI/ML
    if "openai" in body_text.lower() or "chatgpt" in body_text.lower():
        tech_info.append("🤖 AI: Possibly using OpenAI/ChatGPT")
    if "huggingface" in body_text.lower():
        tech_info.append("🤗 AI: Hugging Face")
    if "tensorflow" in body_text.lower():
        tech_info.append("🧠 ML: TensorFlow")
    if "torch" in body_text.lower() or "pytorch" in body_text.lower():
        tech_info.append("🔥 ML: PyTorch")

    return tech_info