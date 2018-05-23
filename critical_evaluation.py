# api keys in config file



# --- api request file ---
parser = ConfigParser()
parser.read('config/config.ini')
api_key = parser.get('api','google_vision_api_key')