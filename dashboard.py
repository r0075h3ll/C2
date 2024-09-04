from auth import protected
from sanic import Blueprint, text

bp = Blueprint("home", url_prefix="/home")

@bp.route("/", methods=["GET"])
@protected
def home():
    return text("Welcome to C2")