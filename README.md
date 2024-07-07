# Apple_Music_Downloader
This script allows you to download songs from Apple Music in MP3 format. The script uses Selenium for browser automation and Requests for file downloading.

## Disclaimer

This project is intended for sharing and educational purposes only. It should not be used for any commercial or profit-making activities. 

## How It Works

The script leverages the [Apple Music Downloader](https://apple-music-downloader.com) website to perform the conversion and download of Apple Music tracks. Here’s how the functionality is implemented:

1. **Selenium for Browser Automation**:
    - The script uses Selenium to automate the process of interacting with the [Apple Music Downloader](https://apple-music-downloader.com) website.
    - It opens the website, enters the Apple Music URL, and clicks the necessary buttons to start the conversion process.

2. **Extracting Download Links**:
    - After initiating the conversion, the script waits for the download link to be generated.
    - It then extracts the download link from the page once it's available.

3. **Downloading the MP3 File**:
    - Using the Requests library, the script downloads the MP3 file from the extracted link.
    - The file is saved locally with a name formatted as `SongName-ArtistName.mp3`.

This approach ensures that the download process is automated, reliable, and fast, utilizing the robust capabilities of the [Apple Music Downloader](https://apple-music-downloader.com) platform.


## Prerequisites

- Python 3.9
- Selenium library
- Requests library

## Setup Instructions

### Step 1: Clone and Set Up the Environment
```
git clone https://github.com/Joezhou1211/Apple_Music_Downloader.git

pip install -r requirements.txt
```

### Step 2: Browser Configuration

#### For macOS (Safari)

1. **Enable Remote Automation in Safari**:
   - Open Safari.
   - Go to `Preferences > Advanced`.
   - Check the box for `Show Develop menu in menu bar`.
   - In the menu bar, go to `Develop > Allow Remote Automation`.

#### For Windows (Chrome)

1. **Download ChromeDriver**:
   - Download the ChromeDriver that matches your Chrome version from [https://sites.google.com/a/chromium.org/chromedriver/downloads].
   - Add the ChromeDriver executable to your system PATH.

2. **Modify the Script**:
   - Replace the `driver = webdriver.Safari()` line with:
     ```python
     from selenium.webdriver.chrome.service import Service
     from webdriver_manager.chrome import ChromeDriverManager

     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
     ```

### Step 3: Get Apple Music Links

To get the Apple Music song links:

1. Open [Apple Music](https://music.apple.com).
2. Search any song and click 'share' then copy its link.

![image](https://github.com/Joezhou1211/Apple_Music_Downloader/assets/121386280/876444d1-a556-4d58-90d7-448fc2659ae8)


### Step 4: Edit the Script

Edit the `downloader.py` script to include your Apple Music links:

```python
links = [
    "https://music.apple.com/au/album/%E8%81%96%E8%AA%95%E7%B5%90/542922079?i=542922100",
    "https://music.apple.com/link2",
    # Add more links as needed
]
```

![image](https://github.com/Joezhou1211/Apple_Music_Downloader/assets/121386280/476598d3-7510-404c-acc0-db48a25ae0a2)

### Step 5: Run the code
```bash
python downloader.py



