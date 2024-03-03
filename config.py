import os

from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('TOKEN')
STRIPE_TOKEN = os.getenv('STRIPE_TOKEN')

