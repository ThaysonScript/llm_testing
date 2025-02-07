from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

print(f"API_KEY: {api_key}")
print(f"DB_USER: {db_user}")
print(f"DB_PASSWORD: {db_password}")
