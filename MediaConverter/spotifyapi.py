""" from dotenv import main
import os

main.load_dotenv()

client_id = os.getenv("CLIENT_ID")
print(client_id) """