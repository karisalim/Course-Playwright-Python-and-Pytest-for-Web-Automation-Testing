import asyncio
import json
import subprocess
import time
import aiohttp
import requests
from pydoll.browser.chromium import Chrome
from pydoll.browser.options import ChromiumOptions

CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROFILE_DIR = r"C:\Temp\pydoll_profile"
DEBUG_PORT = 9222


def start_chrome():
    """بيشغّل Chrome في الخلفية لو مش شغّال."""
    import socket

    # تحقق لو Chrome شغّال بالفعل
    try:
        s = socket.create_connection(("localhost", DEBUG_PORT), timeout=1)
        s.close()
        print(f"[+] Chrome شغّال بالفعل على port {DEBUG_PORT}")
        return
    except (ConnectionRefusedError, OSError):
        pass

    # شغّل Chrome في الخلفية
    print("[*] بيشغّل Chrome أوتوماتيك...")
    subprocess.Popen([
        CHROME_PATH,
        f"--remote-debugging-port={DEBUG_PORT}",
        f"--user-data-dir={PROFILE_DIR}",
        "--disable-blink-features=AutomationControlled",
        "--no-first-run",
        "--no-default-browser-check",
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # انتظر Chrome يشتغل
    print("[*] بينتظر Chrome يشتغل...")
    for i in range(10):
        time.sleep(1)
        try:
            s = socket.create_connection(("localhost", DEBUG_PORT), timeout=1)
            s.close()
            print(f"[+] Chrome اشتغل بعد {i + 1} ثانية ✅")
            return
        except (ConnectionRefusedError, OSError):
            print(f"    انتظار... ({i + 1}/10)")

    raise RuntimeError("Chrome مش اشتغل! تحقق من المسار.")


async def get_ws_url():
    """بيجيب الـ WebSocket URL من Chrome."""
    async with aiohttp.ClientSession() as session:
        async with session.get(f"http://localhost:{DEBUG_PORT}/json/version") as resp:
            data = await resp.json(content_type=None)
            ws_url = data["webSocketDebuggerUrl"]
            user_agent = data["User-Agent"]
            print(f"[+] WS URL: {ws_url}")
            return ws_url, user_agent


async def get_cloudflare_cookies(target_url: str):
    options = ChromiumOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-notifications")
    options.add_argument("--no-sandbox")
    options.add_argument(f"--user-data-dir={PROFILE_DIR}")
    options.add_argument(f"--remote-debugging-port={DEBUG_PORT}")
    options.binary_location = CHROME_PATH

    ws_url, user_agent = await get_ws_url()

    browser = Chrome(options=options)
    await browser.connect(ws_url)

    print(f"[*] بيفتح: {target_url}")
    tab = await browser.new_tab(url=target_url)
    await tab.enable_auto_solve_cloudflare_captcha()

    print("[*] بينتظر تحميل الصفحة وحل Cloudflare (8 ثواني)...")
    await asyncio.sleep(8)

    cookies_raw = await tab.get_cookies()
    print(f"[+] عدد الـ Cookies: {len(cookies_raw)}")

    cookies_dict = {}
    for cookie in cookies_raw:
        cookies_dict[cookie["name"]] = cookie["value"]
        print(f"    - {cookie['name']}: {cookie['value'][:50]}")

    return cookies_dict, user_agent


def scrape_with_cookies(url: str, cookies: dict, user_agent: str, num_requests: int = 3):
    headers = {
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "none",
        "Sec-Fetch-User": "?1",
    }

    session = requests.Session()
    session.cookies.update(cookies)
    session.headers.update(headers)

    print(f"\n[*] بيعمل {num_requests} requests بالـ cookies...")

    for i in range(1, num_requests + 1):
        try:
            response = session.get(url, timeout=10)
            status = response.status_code
            if status == 200:
                print(f"    [{i}] ✅ Status: {status} | Size: {len(response.text)} chars")
            elif status == 403:
                print(f"    [{i}] ❌ Status: 403 - Cloudflare لسه بيبلوك")
            else:
                print(f"    [{i}] ⚠️  Status: {status}")
        except Exception as e:
            print(f"    [{i}] ❌ Error: {e}")


async def main():
    TARGET_URL = "https://www.scrapingcourse.com/cloudflare-challenge"

    print("=" * 60)
    print("pydoll Demo - Cloudflare Bypass Training")
    print("=" * 60)

    # ✅ بيشغّل Chrome أوتوماتيك لو مش شغّال
    start_chrome()

    cookies, user_agent = await get_cloudflare_cookies(TARGET_URL)

    with open("cookies.json", "w") as f:
        json.dump({"cookies": cookies, "user_agent": user_agent}, f, indent=2)
    print(f"\n[+] Cookies محفوظة في cookies.json")

    scrape_with_cookies(TARGET_URL, cookies, user_agent, num_requests=3)

    print("\n" + "=" * 60)
    print("✅ خلص!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())