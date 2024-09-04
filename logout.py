import logging
from sanic import Blueprint, Sanic, HTTPResponse, redirect, text, html
from db import db
from auth import protected
from login import setJWT

logger = logging.getLogger()
logger.setLevel("INFO")

bp = Blueprint("logout", url_prefix="/logout")


@bp.route("/", methods=["GET"])
@protected
def logout(request):
    app_instance = Sanic.get_app("C2")
    token = app_instance.ctx.jwt
    token.killJWT()

    return html("<html><head></head><body>bagged</body></html>", 302, headers = {"Location": "https://www.google.com"})
    # 1. clear client-side localStorage for the page
    