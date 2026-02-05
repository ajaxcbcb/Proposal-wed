import sys
import threading
import http.server
import socketserver
import time
from playwright.sync_api import sync_playwright

PORT = 8082

def start_server():
    class QuietHandler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, format, *args):
            pass

    try:
        with socketserver.TCPServer(("", PORT), QuietHandler) as httpd:
            print(f"Serving at port {PORT}")
            httpd.serve_forever()
    except OSError as e:
        print(f"Could not start server: {e}")

def verify():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(f"http://localhost:{PORT}/index.html")

        # Scroll to stress test
        page.locator("#stress").scroll_into_view_if_needed()

        # Click plus button a few times to change numbers
        plus_btn = page.locator("#btnPlus")
        plus_btn.click()
        plus_btn.click()
        plus_btn.click()

        # Wait for update
        page.wait_for_timeout(500)

        # Take screenshot of the stress section
        stress_section = page.locator("#stress")
        stress_section.screenshot(path="verification/stress_test.png")

        browser.close()
        print("Screenshot taken.")

if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    time.sleep(2)

    try:
        verify()
    except Exception as e:
        print(f"Verification failed: {e}")
        sys.exit(1)
