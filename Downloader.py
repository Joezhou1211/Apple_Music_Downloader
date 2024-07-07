from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

# Initialize Safari browser
driver = webdriver.Safari()

# List of Apple Music links to download
links = [  # Add any links here
    "https://music.apple.com/au/album/%E8%81%96%E8%AA%95%E7%B5%90/542922079?i=542922100"
]

for link in links:
    try:
        # Open the downloader website
        driver.get('https://apple-music-downloader.com')

        # Locate the input box and enter the link
        input_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "search-input"))
        )
        input_box.clear()
        input_box.send_keys(link)

        # Locate and click the "Start" button
        start_button = driver.find_element(By.ID, "search-submit")
        start_button.click()

        # Wait for the "Get Download" button to appear and click it
        download_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#info > div > div:nth-child(3) > input.get-download-submit"))
        )
        driver.execute_script("arguments[0].click();", download_button)

        # Add extra wait time to ensure the page loads completely
        time.sleep(10)

        # Retrieve the song name and artist name
        song_name_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#info > h3"))
        )
        artist_name_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#info > p"))
        )
        song_name = song_name_element.text
        artist_name = artist_name_element.text

        # Locate the download link
        download_link_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#download_mp3 > a.download-btn"))
        )
        download_url = download_link_element.get_attribute('href')
        print(f"Download URL: {download_url}")

        if download_url:
            # Download the file and rename it
            response = requests.get(download_url)
            file_name = f"{song_name}-{artist_name}.mp3"
            with open(file_name, 'wb') as file:
                file.write(response.content)
            print(f"File downloaded and saved as: {file_name} for link: {link}")
        else:
            print(f"Download URL not found for link: {link}")

    except Exception as e:
        print(f"Error processing link {link}: {e}")

# Close the browser
driver.quit()
