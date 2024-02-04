
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import http.client, urllib

import os
import time
import logging

# removes last line of artist link (This link will open...)
def remove_last_line_from_string(s):
    return s[:s.rfind('\n')]

# load website
url = 'https://www.iheartradio.ca/virginradio/toronto/1.1748215?mode=history'
delay_time = 60

# enable headless mode in Selenium
options = Options()
options.add_argument('--headless=new')

driver = webdriver.Chrome(
    options=options,
    # other properties...
)

# instantiate driver
driver = webdriver.Chrome(service=ChromeService(
    ChromeDriverManager().install()), options=options)


def main():
    log = logging.getLogger(__name__)
    logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"), format='%(asctime)s %(message)s')
    log.info("Running Website Monitor")
    artist_name = ""
    while True:
        # get the entire website content
        previous_name = artist_name
        driver.get(url)

        try:
            # select elements by class name
            elements = driver.find_elements(By.CLASS_NAME, "artistLink")
            for title in elements:
                artist_name = title.text
                artist_name = remove_last_line_from_string(artist_name)
                return artist_name
        except:
            print("Error checking website")
        finally:
            if previous_name != artist_name:
                log.info("NEW LOG")
                print(artist_name)
                if artist_name == "Taylor Swift":
                    conn = http.client.HTTPSConnection("api.pushover.net:443")
                    conn.request("POST", "/1/messages.json",
                                 urllib.parse.urlencode({
                                     "token": "aqv51a55c4axu3rpysnxvqpxp9bri8",
                                     "user": "ursx4wqb3ttgxp7jch8batv8nfpwxo",
                                     "message": "TS is playing!",
                                 }), {"Content-type": "application/x-www-form-urlencoded"})
                    conn.getresponse()

            time.sleep(delay_time)
            continue
if __name__ == "__main__":
    main() 