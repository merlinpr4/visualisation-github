from dotenv import load_dotenv
load_dotenv()
import os

os.environ["USER"] = "yo there"

USER = os.getenv("API_USER")
print (USER)

print (os.getenv("USER"))