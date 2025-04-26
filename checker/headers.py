import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning  # type: ignore
from .tech_stack import analyze_stack
from .fallback import fallback_curl_request

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def check_security_web(url):
    required_headers = [
        "X-Frame-Options", "X-XSS-Protection", "Content-Security-Policy",
        "X-Content-Type-Options", "Strict-Transport-Security", "Referrer-Policy",
        "Permissions-Policy", "Cross-Origin-Resource-Policy",
        "Cross-Origin-Opener-Policy", "Cross-Origin-Embedder-Policy",
        "Access-Control-Allow-Origin", "Cache-Control", "Pragma", "Expires",
        "Content-Disposition", "Server", "X-Powered-By"
    ]

    try:
        print("\n" + "="*60)
        print(f"🔍 Checking Security Headers for: {url}")
        print("="*60 + "\n")

        response = requests.get(url, verify=False, timeout=30)
        headers = response.headers

        # 🧠 Technology Stack
        tech_info = analyze_stack(headers, response.text)
        if tech_info:
            print("🧠 Detected Technology Stack:")
            print("-"*60)
            for tech in tech_info:
                print(f"{tech}")
            print("-"*60 + "\n")

        # 🛡️ Security Header Check
        print("🛡️ Security Header Check:")
        print("-"*60)
        for header in required_headers:
            if header in headers:
                if header in ["Server", "X-Powered-By"]:
                    tech = headers[header]
                    print(f"⚠️  {header}: Found → {tech} → Consider removing or obfuscating this")
                else:
                    print(f"✅ {header}: Found")
            else:
                if header in ["Server", "X-Powered-By"]:
                    print(f"✅ {header}: Not Found → Good (Information not exposed)")
                else:
                    print(f"❌ {header}: Not Found")
        print("-"*60 + "\n")

        # 🍪 Cookie Check
        print("🍪 Cookie Security Check:")
        print("-"*60)
        cookies = response.headers.get("Set-Cookie")
        if cookies:
            print(f"   {'✅' if 'Secure' in cookies else '❌'} Secure")
            print(f"   {'✅' if 'HttpOnly' in cookies else '❌'} HttpOnly")
            print(f"   {'✅' if 'SameSite' in cookies else '❌'} SameSite")
        else:
            print("   ❌ Set-Cookie: Not Found")
        print("-"*60 + "\n")

        # 🚨 Risk Section
        print("🚨 Potential Security Risks:")
        print("-"*60)
        if "Content-Security-Policy" not in headers:
            print("   🔴 Missing CSP → Risk of XSS attacks")
        if "Strict-Transport-Security" not in headers:
            print("   🔴 Missing HSTS → Risk of HTTPS downgrade")
        if "Server" in headers:
            print("   🔴 Server info exposed → Could allow targeted attacks")
        if "X-Powered-By" in headers:
            print("   🔴 X-Powered-By exposed → Technology fingerprinting risk")
        print("="*60 + "\n")

    except (requests.exceptions.SSLError, requests.exceptions.ReadTimeout) as err:
        print(f"\n⚠ Connection issue with {url}: {err}")
        fallback_curl_request(url, required_headers)

    except Exception as e:
        print(f"\n❗ Error checking {url}: {e}")
