# 🎬 YouTube Video Downloader

Hello! Welcome to my project. This is a simple Python tool I created to easily download high-quality YouTube videos directly to your computer.

## ✨ What does it do?
* Downloads the best quality video and audio from YouTube.
* Automatically combines them into a single `.mp4` file.

---

## 🛠️ Step-by-Step Installation Guide (For Beginners)

If you are new to Python or getting errors like `No such file or directory` or `ModuleNotFoundError`, follow these exact steps to set it up correctly:

### Step 1: Install Python
1. Download and install Python from the official website (make sure to check the box that says **"Add Python to PATH"** during installation).

### Step 2: Open the Project in VS Code
1. Open **Visual Studio Code**.
2. Go to `File` > `Open Folder` and select the folder where your `ytdown.py` file is saved (e.g., *Automated VideoSocial Media Downloader*).
> 💡 **Why?** This prevents the `Errno 2: No such file or directory` error by making sure your terminal opens in the correct location.

### Step 3: Install Required Dependencies
Open the Terminal inside VS Code (`Terminal` > `New Terminal`) and run the following command to install the required library:

```bash
pip install yt-dlp
