# 🛡️ Web Security Checker

A Python tool to analyze HTTP security headers and detect exposed server technologies.

## 📁 Structure

web-security-checker/ 
├── main.py # Entry point 
├── checker/ # Core logic 
│ ├── headers.py # Security header checking 
│ ├── tech_stack.py # Detect tech stack from headers 
│ ├── fallback.py # Curl fallback for failed requests 
│ └── init.py 
├── requirements.txt # Python dependencies 
└── README.md # Project documentation


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
🔍 Checking security headers for: https://example.com/

🧠 Detected Technology Stack:
   🧱 Server: Nginx
   🛠️ Powered by: PHP/7.4

🛡️ Security Header Check:
   ✅ X-Frame-Options: Found
   ❌ Content-Security-Policy: Not Found
   ⚠️  Server: Found → Consider removing or obfuscating this

🍪 Cookie Security Check:
   ✅ Secure
   ✅ HttpOnly
   ❌ SameSite

```