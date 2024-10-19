import sota
import machine
import network
import time

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
GITHUB_URL = "https://raw.githubusercontent.com/macraj/upyota/master"
OTA = sota.Senko(None, None, url=GITHUB_URL, files=["boot.py", "main.py"])

# Connect to Wi-Fi network.
def sta_connect():
    if not wlan.isconnected():
        # connecting to network...
        wlan.connect("ray-S", "D75AB729AS7")

        ctime = time.time()
        while not wlan.isconnected():
            if time.time() - ctime > 30:
                # print('WLAN timeout!')
                return False
            time.sleep(0.5)
            stat_led.value(not stat_led.value())
        return True
    print('network config:', wlan.ifconfig())

sta_connect()

if OTA.update():
    print("Updated to the latest version! Rebooting...")
    machine.reset()
# if OTA.fetch():
#     print("A newer version is available!")
# else:
#     print("Up to date!")
OTA = None