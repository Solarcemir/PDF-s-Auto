# 📚 PDF Downloader for Educational Platforms (Selenium + Python)

This is a Python-based automation script that allows students to easily download PDF documents from online learning platforms powered by D2L (Desire2Learn) or similar systems.

✅ It **requires manual login** and does **not bypass any authentication**.  
✅ It is **intended for personal, educational use only**.  
✅ It helps you save time at the end of the semester by automatically grabbing course materials.

---

## 🚀 Features

- Automatic navigation to course content
- Download all PDF documents from the Table of Contents
- Avoids re-downloading files already saved
- Custom folder name support
- Works on any D2L-based platform (like Brightspace, CourseLink, etc.)

---

## 🛠 Requirements

- Python 3.7+
- Google Chrome browser
- Chrome WebDriver (must match your Chrome version)

---

## 📦 Installation

1. **Clone this repository** or download the script:
```
git clone https://github.com/yourusername/pdf-downloader.git
cd pdf-downloader
```

2. **Install the required Python packages:**
```
pip install selenium
```

3. **Download ChromeDriver**  
Make sure the [ChromeDriver](https://sites.google.com/chromium.org/driver/) version matches your Chrome browser.  
Place it in your project folder or make sure it's in your system PATH.

---

## ▶️ How to Use

1. **Run the script:**
```
python pdf_downloader.py
```

2. **Follow the prompts:**
   - Enter the name of the folder where you want PDFs to be saved.
   - Paste the link to your learning platform homepage (e.g. `https://youruniversity.brightspace.com/d2l/home`)
   - Manually login and navigate to the course.
   - Press Enter when you're on the desired course page.

3. **The script will:**
   - Click into the "Content" section
   - Access the Table of Contents
   - Find all PDF document links
   - Begin downloading each file to the specified folder

---

## 📎 Notes

- This script is **read-only automation**: it simulates manual clicks, and respects the platform's authentication and copyright.
- It does **not scrape** or store any content for redistribution.
- Make sure you are complying with your institution’s **terms of use** when using this tool.

---

## ⚖️ License

This project is licensed under the MIT License.

---



