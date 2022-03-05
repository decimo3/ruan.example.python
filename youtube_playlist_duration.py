import requests
import dotenv

dotenv.load_dotenv()
key = dotenv.get_key("./.env","KEY")

params = {'part':'snippet','maxResults':25,'q':'surfing','key':key}
response = requests.get("https://www.googleapis.com/youtube/v3/search", params=params)

print(response.json())
