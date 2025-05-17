# 🤖 LinkedIn Auto Apply Bot

This Python automation script uses Selenium to auto-apply to jobs on [LinkedIn](https://www.linkedin.com) using the "Easy Apply" feature. It's designed to simplify the repetitive process of applying to jobs that don't require multi-step forms.

---

## 📌 Features

- Logs into your LinkedIn account automatically
- Navigates to the job listings page
- Detects and clicks the first job listing
- Clicks the "Easy Apply" button
- Fills in your phone number (if required)
- Submits the application if it's a one-step form

---

## ⚙️ Tech Stack

- 🐍 Python 3.x
- 🌐 Selenium WebDriver
- 🧪 WebDriver Manager
- 🔐 dotenv for managing credentials securely

---

## 🔐 Setup Instructions

### 1. Clone this repo

```bash
git clone https://github.com/PTharun007/linkedin-auto-apply.git
cd linkedin-auto-apply
