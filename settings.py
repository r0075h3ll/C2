# from sanic import Sanic
# import os
# from dotenv import load_dotenv

# load_dotenv()
# JWT_SECRET = os.getenv("JWT_SECRET")
# DB_USER = os.getenv("DB_USER")
# DB_PASSWORD = os.getenv("DB_PASSWORD")
# DB_NAME = os.getenv("DB_NAME")

# configs = {
#     "JWT_SECRET": JWT_SECRET,
#     "DB_USER": DB_USER,
#     "DB_PASSWORD": DB_PASSWORD,
#     "DB_NAME": DB_NAME
# }

# get_app_instance = Sanic.get_app("C2")
# get_app_instance.config.secrets = configs