import os

API_ID = API_ID = 29683927

API_HASH = os.environ.get("API_HASH", "b2eb32ac1030edd8bc36c7b554ef6fc3")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7903348261:AAFgADxgmNQUiW9UhF_0srnTFCKWT6RLW90")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 5583858510))

LOG = -2311732949

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6971380203").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
