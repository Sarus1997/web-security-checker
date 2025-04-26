import subprocess

def fallback_curl_request(url, required_headers):
    try:
        print(f"\n🌐 Using curl fallback for: {url}\n")
        result = subprocess.run(
            ['curl', '-I', '--insecure', url],
            capture_output=True,
            text=True
        )
        headers = result.stdout
        for header in required_headers:
            if any(header.lower() in line.lower() for line in headers.splitlines()):
                print(f"✅ {header}: Found")
            else:
                print(f"❌ {header}: Not Found")
    except Exception as e:
        print(f"\n❗ Curl error: {e}")