# 🚀 Universal Telegram Multi-Bot Requester (Async Engine)

## 📌 Overview
An efficient, asynchronous Python-based automation tool designed to interact with multiple Telegram bots simultaneously. This engine allows users to broadcast search queries via a simple command directly from their "Saved Messages" and receive aggregated results in one place.

## 🛠 Technical Stack
* **Language:** Python 3.10+
* **Framework:** Pyrogram (Asynchronous MTProto API)
* **Core Logic:** Asyncio event loops with custom delay management.

## ✨ Key Features
* **Full Asynchrony**: Built on `asyncio` for high performance.
* **Anti-Flood Protection**: Integrated 15-second delay between requests.
* **Simplified UX**: Trigger searches using the `.find [query]` command.

## 🚀 Installation
1. Install dependencies: `pip install pyrogram tgcrypto`.
2. Configure your `API_ID` and `API_HASH` in `main.py`.
3. Run the script and start searching!
