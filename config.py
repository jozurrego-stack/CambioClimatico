import os
from dotenv import load_dotenv
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "").strip()
CDS_URL = os.getenv("CDS_URL", "").strip()
CDS_KEY = os.getenv("CDS_KEY", "").strip()
