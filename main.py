from ota import OTAUpdater
from WIFI_CONFIG import SSID, PASSWORD

# firmware_url = "https://github.com/kevinmcaleer/ota_test/main/"
firmware_url = "https://github.com/macraj/uPyOTA/blob/master/"

ota_updater = OTAUpdater(SSID, PASSWORD, firmware_url, "main.py")

ota_updater.download_and_install_update_if_available()