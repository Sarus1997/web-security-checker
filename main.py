from checker.headers import check_security_web


if __name__ == "__main__":
    url = "https://sarus.vercel.app/"  # เปลี่ยน URL ที่ต้องการตรวจสอบ
    check_security_web(url)