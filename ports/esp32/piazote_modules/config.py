# Config module to load a json file into an object.

import json


class config:
    """Class to retrieve the config data"""

    def __init__(self) -> None:
        self._loadConfigJson()

    def _loadConfigJson(self):
        """Extract data from JSON file"""
        with open("config.json") as config_f:
            print("Loading JSON object")
            config_data = json.load(config_f)
            self.wifi_ssid = config_data["WIFI_SSID"]
            self.wifi_password = config_data["WIFI_PASS"]
            print("Configuration object loaded")