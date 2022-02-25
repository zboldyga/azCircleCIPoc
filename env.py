from dotenv import dotenv_values
import json

config = dotenv_values(".env.test")

with open('.env.json', 'w', encoding='utf-8') as f:
    json.dump(config, f, ensure_ascii=False, indent=4)