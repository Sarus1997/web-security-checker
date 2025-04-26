def analyze_stack(headers, body_text=""):
    tech_info = {
        "Server & Hosting": [],
        "Powered By": [],
        "Frontend": [],
        "UI Libraries": [],
        "Backend / API": [],
        "CMS": [],
        "E-Commerce": [],
        "AI / ML": [],
        "Database": [],
        "Payment Gateway": []
    }

    server = headers.get("Server", "")
    x_powered_by = headers.get("X-Powered-By", "")

    # ------------------ Server & Hosting ------------------
    if "apache" in server.lower():
        tech_info["Server & Hosting"].append("🧱 Server: Apache")
    elif "nginx" in server.lower():
        tech_info["Server & Hosting"].append("🧱 Server: Nginx")
    elif "iis" in server.lower():
        tech_info["Server & Hosting"].append("🧱 Server: Microsoft IIS")
    elif "cloudflare" in server.lower():
        tech_info["Server & Hosting"].append("🧱 CDN/Proxy: Cloudflare")
    elif "vercel" in server.lower():
        tech_info["Server & Hosting"].extend(["🧱 Server: Vercel", "☁️ Hosting: Vercel"])
    elif "netlify" in server.lower():
        tech_info["Server & Hosting"].extend(["🧱 Server: Netlify", "☁️ Hosting: Netlify"])
    elif "railway" in server.lower():
        tech_info["Server & Hosting"].append("☁️ Hosting: Railway")
    elif "firebase" in server.lower():
        tech_info["Server & Hosting"].append("☁️ Hosting: Firebase Hosting")
    elif server:
        tech_info["Server & Hosting"].append(f"🧱 Server: {server}")

    # ------------------ Powered By ------------------
    if "express" in x_powered_by.lower():
        tech_info["Powered By"].append("🛠️ Framework: Express (Node.js)")
    elif "php" in x_powered_by.lower():
        tech_info["Powered By"].append("🛠️ Language: PHP")
    elif "asp.net" in x_powered_by.lower():
        tech_info["Powered By"].append("🛠️ Framework: ASP.NET")
    elif "laravel" in x_powered_by.lower():
        tech_info["Powered By"].append("🛠️ Framework: Laravel (PHP)")
    elif "django" in x_powered_by.lower():
        tech_info["Powered By"].append("🛠️ Framework: Django (Python)")
    elif "rails" in x_powered_by.lower():
        tech_info["Powered By"].append("🛠️ Framework: Ruby on Rails")
    elif x_powered_by:
        tech_info["Powered By"].append(f"🛠️ Powered by: {x_powered_by}")

    # ------------------ Frontend ------------------
    if "react" in body_text.lower() or "__REACT_DEVTOOLS_GLOBAL_HOOK__" in body_text:
        tech_info["Frontend"].append("⚛️ Frontend: React")
    if "__next_data__" in body_text.lower():
        tech_info["Frontend"].append("🚀 Framework: Next.js")
    if "vue" in body_text.lower() or "__VUE_DEVTOOLS_GLOBAL_HOOK__" in body_text:
        tech_info["Frontend"].append("🖖 Framework: Vue.js")
    if "nuxt" in body_text.lower():
        tech_info["Frontend"].append("🚀 Framework: Nuxt.js")
    if "ng-version" in body_text.lower():
        tech_info["Frontend"].append("🅰️ Framework: Angular")
    if "svelte" in body_text.lower():
        tech_info["Frontend"].append("🔥 Framework: Svelte")

    # ------------------ UI Libraries ------------------
    if "jquery" in body_text.lower():
        tech_info["UI Libraries"].append("📜 Library: jQuery")
    if "bootstrap" in body_text.lower():
        tech_info["UI Libraries"].append("🎨 UI: Bootstrap")
    if "tailwind" in body_text.lower():
        tech_info["UI Libraries"].append("🎨 UI: Tailwind CSS")
    if "bulma" in body_text.lower():
        tech_info["UI Libraries"].append("🎨 UI: Bulma CSS")
    if "material-ui" in body_text.lower():
        tech_info["UI Libraries"].append("🎨 UI: Material UI")

    # ------------------ Backend / API ------------------
    if "cloudflare" in body_text.lower() and "worker" in body_text.lower():
        tech_info["Backend / API"].append("⚡ Edge Compute: Cloudflare Workers")
    if "graphql" in body_text.lower():
        tech_info["Backend / API"].append("🕸️ API: GraphQL")
    if "socket.io" in body_text.lower():
        tech_info["Backend / API"].append("🔌 Real-time: Socket.IO")
    if "firebase" in body_text.lower():
        tech_info["Backend / API"].append("🔥 BaaS: Firebase")
    if "supabase" in body_text.lower():
        tech_info["Backend / API"].append("🦾 BaaS: Supabase")
    if "strapi" in body_text.lower():
        tech_info["Backend / API"].append("🛠️ Headless CMS: Strapi")

    # ------------------ CMS ------------------
    if "wordpress" in body_text.lower():
        tech_info["CMS"].append("📰 CMS: WordPress")
    if "drupal" in body_text.lower():
        tech_info["CMS"].append("📰 CMS: Drupal")
    if "joomla" in body_text.lower():
        tech_info["CMS"].append("📰 CMS: Joomla")

    # ------------------ E-Commerce ------------------
    if "shopify" in body_text.lower():
        tech_info["E-Commerce"].append("🛒 E-Commerce: Shopify")
    if "magento" in body_text.lower():
        tech_info["E-Commerce"].append("🛒 E-Commerce: Magento")

    # ------------------ AI / ML ------------------
    if "openai" in body_text.lower() or "chatgpt" in body_text.lower():
        tech_info["AI / ML"].append("🤖 AI: Possibly using OpenAI/ChatGPT")
    if "huggingface" in body_text.lower():
        tech_info["AI / ML"].append("🤗 AI: Hugging Face")
    if "tensorflow" in body_text.lower():
        tech_info["AI / ML"].append("🧠 ML: TensorFlow")
    if "torch" in body_text.lower() or "pytorch" in body_text.lower():
        tech_info["AI / ML"].append("🔥 ML: PyTorch")

    # ------------------ Database ------------------
    if "mongodb" in body_text.lower():
        tech_info["Database"].append("🗃️ Database: MongoDB")
    if "mysql" in body_text.lower():
        tech_info["Database"].append("🗃️ Database: MySQL")
    if "postgresql" in body_text.lower() or "postgres" in body_text.lower():
        tech_info["Database"].append("🗃️ Database: PostgreSQL")
    if "sqlite" in body_text.lower():
        tech_info["Database"].append("🗃️ Database: SQLite")
    if "redis" in body_text.lower():
        tech_info["Database"].append("⚡ Cache/DB: Redis")

    # ------------------ Payment Gateway ------------------
    if "stripe" in body_text.lower():
        tech_info["Payment Gateway"].append("💳 Payment: Stripe")
    if "paypal" in body_text.lower():
        tech_info["Payment Gateway"].append("💳 Payment: PayPal")
    if "square" in body_text.lower():
        tech_info["Payment Gateway"].append("💳 Payment: Square")
    if "omise" in body_text.lower():
        tech_info["Payment Gateway"].append("💳 Payment: Omise")

    # ----------- Return as flat formatted lines -----------
    final_list = []
    for category, items in tech_info.items():
        if items:
            final_list.append(f"\n📦 {category}:")
            final_list.extend([f"   {item}" for item in items])

    return final_list
