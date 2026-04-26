from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import re

URL = "https://www.zee5.com/tv-shows/details/tumm-se-tumm-tak/0-6-4z5727104"

def run():
    with sync_playwright() as p:
        print("🚀 Launching browser...")

        browser = p.chromium.launch(
            headless=True,
            args=["--no-sandbox", "--disable-dev-shm-usage"]
        )

        page = browser.new_page()

        print("🌐 Opening ZEE5 page...")
        page.goto(URL, timeout=60000)

        page.wait_for_timeout(8000)

        html = page.content()
        print(f"📄 HTML size: {len(html)}")

        soup = BeautifulSoup(html, "html.parser")

        episodes = []

        for img in soup.find_all("img"):
            title = img.get("title") or img.get("alt")

            if title and "Episode" in title:
                match = re.search(r"Episode\s*(\d+)", title)

                if match:
                    ep_num = int(match.group(1))
                    src = img.get("src", "")

                    id_match = re.search(r"/resources/([^/]+)/", src)
                    ep_id = id_match.group(1) if id_match else None

                    if ep_id:
                        episodes.append({
                            "num": ep_num,
                            "id": ep_id,
                            "title": title
                        })

        if not episodes:
            print("❌ No episodes found")
        else:
            latest = max(episodes, key=lambda x: x["num"])

            print("\n🎬 ===== LATEST EPISODE =====")
            print(f"Episode Number : {latest['num']}")
            print(f"Episode ID     : {latest['id']}")
            print(f"Title          : {latest['title']}")

            ep_url = f"https://www.zee5.com/tv-shows/details/tumm-se-tumm-tak/{latest['id']}"
            print(f"Watch URL      : {ep_url}")

        browser.close()
