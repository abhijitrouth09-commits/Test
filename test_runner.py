from test import run
import time
import traceback
import subprocess

print("🚀 Starting Render test...")

# 🔥 FORCE INSTALL BROWSER AT RUNTIME
try:
    print("🔧 Installing Chromium (runtime)...")
    subprocess.run(["python", "-m", "playwright", "install", "chromium"], check=True)
    print("✅ Chromium installed")
except Exception as e:
    print("❌ Install failed:", e)

# 🔥 RUN SCRIPT
try:
    run()
except Exception as e:
    print("❌ ERROR OCCURRED:")
    traceback.print_exc()

print("⏳ Keeping service alive...")

# keep alive (important for Render)
while True:
    time.sleep(60)
