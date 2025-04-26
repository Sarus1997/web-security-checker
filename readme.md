# 🛡️ Web Security Checker

A Python tool to analyze HTTP security headers and detect exposed server technologies.

## 📁 Structure
```bash
web-security-checker/ 
├── main.py # Entry point 
├── checker/ 
│ ├── fallback.py # Curl fallback for failed requests 
│ ├── headers.py # Detect tech stack from headers 
│ ├── tech_stack.py # Security header checking 
│ └── __init__.py 
├── requirements.txt # Python dependencies 
└── README.md # Project documentation
```


## 🚀 Usage

1. Install dependencies:

```bash
pip install -r requirements.txt

```

2. Run the script:

```bash
python main.py

```

3. Result will show:

```bash
- Technology stack
- Security headers
- Cookie flags
- Recommendations

```
✅ Example Output
```bash
============================================================
🔍 Checking Security Headers for: https://sarus.vercel.app/
============================================================

🧠 Detected Technology Stack:
------------------------------------------------------------

📦 Server & Hosting:
   🧱 Server: Vercel
   ☁️ Hosting: Vercel

📦 Frontend:
   ⚛️ Frontend: React
   🖖 Framework: Vue.js
   🚀 Framework: Nuxt.js

📦 Backend / API:
   🔥 BaaS: Firebase
------------------------------------------------------------

🛡️ Security Header Check:
------------------------------------------------------------
❌ X-Frame-Options: Not Found
❌ X-XSS-Protection: Not Found
❌ Content-Security-Policy: Not Found
❌ X-Content-Type-Options: Not Found
✅ Strict-Transport-Security: Found
❌ Referrer-Policy: Not Found
❌ Permissions-Policy: Not Found
❌ Cross-Origin-Resource-Policy: Not Found
❌ Cross-Origin-Opener-Policy: Not Found
❌ Cross-Origin-Embedder-Policy: Not Found
✅ Access-Control-Allow-Origin: Found
✅ Cache-Control: Found
❌ Pragma: Not Found
❌ Expires: Not Found
✅ Content-Disposition: Found
⚠️  Server: Found → Vercel → Consider removing or obfuscating this
✅ X-Powered-By: Not Found → Good (Information not exposed)
------------------------------------------------------------

🍪 Cookie Security Check:
------------------------------------------------------------
   ❌ Set-Cookie: Not Found
------------------------------------------------------------

🚨 Potential Security Risks:
------------------------------------------------------------
   🔴 Missing CSP → Risk of XSS attacks
   🔴 Server info exposed → Could allow targeted attacks
============================================================

```