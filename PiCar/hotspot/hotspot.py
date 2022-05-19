from getmac import get_mac_address
import os 

# Stop hostapd 
os.system("systemctl stop hostapd")

# Set wifi country to CA
os.system("raspi-config nonint do_wifi_country CA")

# Get the mac address of the Raspberry Pi
mac = get_mac_address()
print("Mac address: " + mac)

# remove the : from the mac address
mac = mac.replace(":", "")

# Get the last 6 digits of the mac address
mac = mac[-6:]

hostapdconf = """
interface=wlan0
hw_mode=g
country_code=CA
driver=nl80211
channel=6
macaddr_acl=0
auth_algs=1
ignore_broadcast_ssid=0
wpa=2
wpa_key_mgmt=WPA-PSK
wpa_pairwise=CCMP
wpa_passphrase=raspberry
ieee80211n=1
wmm_enabled=1
wpa_group_rekey=86400
ssid=PiCarV_""" + mac.upper() 

# Write the hostapd configuration file to /etc/hostapd/hostapd.conf
try:
    with open("/etc/hostapd/hostapd.conf", "w") as f:
        f.write(hostapdconf)
except:
    print("Error writing hostapd.conf")


# Start hostapd
os.system("systemctl start hostapd")

# Disable the hotspot service 
#os.system("systemctl disable hotspot")

