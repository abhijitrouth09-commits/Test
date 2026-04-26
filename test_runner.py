from test import run
import time
import traceback

print("🚀 Starting Render test...")

try:
    run()
except Exception as e:
    print("❌ ERROR OCCURRED:")
    traceback.print_exc()

print("⏳ Keeping service alive...")

# 🔥 keep alive so Render doesn't stop
while True:
    time.sleep(60)
