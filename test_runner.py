from test import run
import time
import traceback
import subprocess
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Test running..."

def start_test():
    print("🚀 Starting Render test...")

    try:
        print("🔧 Installing Chromium...")
        subprocess.run(["python", "-m", "playwright", "install", "chromium"], check=True)
        print("✅ Chromium installed")
    except Exception as e:
        print("❌ Install failed:", e)

    try:
        run()
    except Exception:
        print("❌ ERROR:")
        traceback.print_exc()

# 🔥 RUN TEST IN BACKGROUND
import threading
threading.Thread(target=start_test).start()

# 🔥 KEEP SERVER ALIVE (VERY IMPORTANT)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
