from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import re

def clean_filename(name):
    """Replaces invalid filename characters with underscores."""
    return re.sub(r'[\\/*?:"<>|]', "_", name)

# === Ask user for folder name ===
folder_name = input("📁 Enter the name of the folder where PDFs will be saved: ").strip()
folder_path = os.path.join(os.getcwd(), folder_name)
os.makedirs(folder_path, exist_ok=True)

# === Ask user for learning platform URL ===
start_url = input("🌐 Paste the URL of your learning platform's homepage (e.g., https://yourplatform.com/d2l/home): ").strip()

# === Setting up Chrome options ===
options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": folder_path,
    "plugins.always_open_pdf_externally": True  # Skip preview, force download
})
options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=options)

# === Open platform ===
print("🧭 Opening platform, please login and navigate to your course manually.")
driver.get(start_url)
input("📌 Press Enter when you're inside the course page you want to download from...")

# === Click "Content" tab ===
try:
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.LINK_TEXT, "Content"))).click()
    print("✅ Entering Content section...")
    time.sleep(2)
except Exception as e:
    print("⚠️ Could not click on Content. Try clicking it manually, then press Enter.")
    input("Press Enter to continue once Content is open.")

# === Click on "Table of Contents" ===
try:
    WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "TreeItemTOC"))).click()
    print("✅ Entering Table of Contents...")
    time.sleep(2)
except:
    print("⚠️ Could not find Table of Contents button, continuing anyway...")

# === Get course ID from current URL ===
current_url = driver.current_url
match = re.search(r'/d2l/le/content/(\d+)/', current_url)
course_id = match.group(1) if match else None
if not course_id:
    print("❌ Course ID could not be detected. Exiting.")
    driver.quit()
    exit()

# === Build platform-safe ToC URL ===
base_domain = re.match(r'https?://[^/]+', start_url).group(0)
toc_url = f"{base_domain}/d2l/le/content/{course_id}/Home"

# === Track already downloaded files ===
downloaded_files = set(os.listdir(folder_path))

# === Main download loop ===
while True:
    try:
        # Go back to ToC in case we navigated away
        driver.get(toc_url)
        WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.ID, "TreeItemTOC"))).click()
        time.sleep(2)

        # Find all visible PDF links
        pdf_links = driver.find_elements(By.XPATH, '//a[contains(@title, "PDF document")]')
        print(f"🔍 PDFs detected: {len(pdf_links)}")

        descargado_algo = False

        for i, pdf in enumerate(pdf_links):
            title = pdf.text.strip() or f"Document_{i+1}"
            title = clean_filename(title)
            filename = f"{title}.pdf"

            if filename in downloaded_files:
                print(f"🟡 Already exists: {filename}, skipping.")
                continue

            print(f"➡️ Attempting to download: {title}")

            try:
                driver.execute_script("arguments[0].scrollIntoView(true);", pdf)
                time.sleep(0.5)
                pdf.click()
                time.sleep(2)

                download_button = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, '//button[@id and contains(.,"Download")]'))
                )
                download_button.click()

                print(f"✅ Download started for: {filename}")
                downloaded_files.add(filename)
                descargado_algo = True
                time.sleep(2)

            except Exception as e:
                print(f"❌ Error downloading {title}: {e}")

            break  # Only download one per loop to avoid stale elements

        if not descargado_algo:
            print("✅ All detected PDFs have been downloaded.")
            break

    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")
        break

# Optional: Close browser
# driver.quit()
