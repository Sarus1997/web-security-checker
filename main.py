from checker.headers import check_security_web


if __name__ == "__main__":
    url = "https://sarus.vercel.app/"  # You can change this to test other URLs
    check_security_web(url)