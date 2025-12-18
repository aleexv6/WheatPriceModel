from dotenv import load_dotenv
import os

load_dotenv()  # Charge les variables depuis .env

# Database
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")

#Api keys
USDA_NASS_API_KEY = os.getenv("USDA_NASS_API_KEY")