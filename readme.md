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