# 📧 AI Email Automation System

Auto-reads, classifies, and replies to emails automatically. Connects to Gmail, reads every incoming email, classifies intent, drafts a reply, and sends — saving businesses 2-3 hours per day of manual email handling.

## 🚀 How It Works

Incoming Email → Gmail → n8n/Python → Classify Intent → Generate Reply → Send Reply

## ✨ Features

- Auto-Read — Monitors Gmail inbox for unread emails
- Smart Classification — Identifies Support, Sales, Complaint, or Inquiry
- Auto-Reply — Sends contextual replies instantly
- 24/7 Operation — n8n workflow runs continuously on cloud
- Dual Version — Python (customizable) + n8n (production-ready)
- 100% Free — No API keys or credits needed

## 🛠️ Tech Stack

Python | n8n | Gmail API | JavaScript | Flask

## 📂 Project Structure


email-automation/
email_bot.py Gmail API connection
classifier.py Email classification + reply generation
main.py Main automation script
requirements.txt Python dependencies
credentials.json Gmail API credentials (not in repo)



## ⚡ Quick Start — Python Version

1. Clone the repo: `git clone https://github.com/Abdulgeni/email-automation.git`
2. Install: `pip install -r requirements.txt`
3. Set up Gmail API in Google Cloud Console
4. Download credentials as `credentials.json`
5. Run: `python main.py`

## ⚡ Quick Start — n8n Version

1. Import workflow into n8n
2. Connect Gmail account
3. Activate — runs 24/7 automatically

## 📊 Email Categories

SUPPORT — help, error, broken, bug, issue → Troubleshooting steps
SALES — price, cost, demo, trial → Pricing + schedule call
COMPLAINT — refund, complaint, bad, unhappy → Apology + resolution
INQUIRY — how, what, when, where → Information + contact details

## 📈 ROI for Businesses

Time on emails: 2-3 hours/day → 15 minutes/day
Response time: 4-8 hours → Under 1 minute
Missed emails: 5-10% → 0%

## 👤 Author

Abdulgeni — github.com/Abdulgeni

Built with Python, n8n, and Gmail API.
