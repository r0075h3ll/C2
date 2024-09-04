import logging
from sanic import Sanic
from sanic.response import text
from routes import task, content
from sanic_ext import Extend
import login, logout
import os
from sanic.worker.loader import AppLoader
from dotenv import load_dotenv

logger = logging.getLogger()
logger.setLevel("INFO")

app = Sanic("C2")

load_dotenv()
JWT_SECRET = os.getenv("JWT_SECRET")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")

configs = {
    "JWT_SECRET": JWT_SECRET,
    "DB_USER": DB_USER,
    "DB_PASSWORD": DB_PASSWORD,
    "DB_NAME": DB_NAME
}

app.config.secrets = configs

app.ctx.jwt = None
logger.info(app.ctx.jwt)
# content.ctx = app.ctx
# login.bp.ctx = app.ctx
# logout.bp.ctx = app.ctx

# app.blueprint(task.bp)
# app.blueprint(agent.bp)

app.blueprint(content)
app.blueprint(login.bp)
app.blueprint(logout.bp)

Extend(app)

# logger.info(app.ctx.jwt)

@app.get("/")
async def hello_world(request):
    logger.info(app.ctx.jwt)
    logger.info(dir(request))
    logger.info(request.cookies.get("token"))
    return text("Hello, world.")

@app.get("/c2")
async def c2_init(request):
    return text("C2")


# if __name__ == "__main__":
#     loader = AppLoader(factory=partial(create_app))
#     app = loader.load()
#     app.prepare(host="0.0.0.0", port=8000, dev=True)
#     Sanic.serve(primary=app, app_loader=loader)