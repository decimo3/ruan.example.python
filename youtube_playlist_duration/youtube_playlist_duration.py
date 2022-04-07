# Não foi possível continuar o projeto devido a limitações de acesso a API do Youtube

import requests
import dotenv

dotenv.load_dotenv()
key = dotenv.get_key("./.env","KEY")

params = {'part':'snippet','maxResults':25,'q':'surfing','key':key}
response = requests.get("https://www.googleapis.com/youtube/v3/search", params=params)

print(response.json())
