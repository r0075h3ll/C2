import logging
import jwt
from sanic import Blueprint, text, redirect, HTTPResponse, Sanic
from db import db
import random
# from settings import JWT_SECRET
from urllib.parse import parse_qs
from sanic import Sanic

logger = logging.getLogger()
logger.setLevel("INFO")

bp = Blueprint("login", url_prefix="/login")

class setJWT():
    def __init__(self, username=None): 
        self.user = username
        self.jw_token = None
        self.app_instance = Sanic.get_app("C2")
        JWT_SECRET = self.app_instance.config.secrets['JWT_SECRET']

        jw_token = jwt.encode(
            {
                "uuid": self.user
            }, JWT_SECRET, algorithm = 'HS256'          
        )

        self.jw_token = jw_token

    def getJWT(self):
        return self.jw_token
    
    def checkJWT(self):
        try:
            decode = jwt.decode(self.jw_token, key=JWT_SECRET, algorithms=['HS256', ])

        except Exception as e:
            logger.info("JWT verification failed")
            return False
        
        return True

    def killJWT(self):
        self.jw_token = None
        self.app_instance.ctx.jwt = None


@bp.route("/signup", methods=["POST"]) #redirect to home if session is not expired
def signup(request):
    # username = request.args.get("uname").lower()
    # password = request.args.get("passwd").lower()

    username = request.form.get("uname")
    password = request.form.get("passwd")

    logger.info(username)

    getAllUsers = db.session.query(db.UserModel).all()

    logger.info(getAllUsers)

    # for user in getAllUsers:
    #     print(user.username, user.password)

    for user in getAllUsers:
        if user.username == username:
            logger.info("user already exists")
            return redirect("/login") # redirect to login page 


    CreateUser = db.UserModel(id = random.randint(0,1337), username = username, password = password) # make ID parameter auto increment
    db.session.add(CreateUser)
    db.session.commit()
    logger.info("User account created")
    return text("User account created")


@bp.route("/", methods=["POST"])
def login(request): # if the user is not loggedin, redirect here
    # logger.info(bp.ctx.jwt)
    form = request.get_form()

    logger.info(form)
    
    # args = parse_qs(request.body)
    # logger.info(args)
    username = form.get("uname")
    password = form.get("passwd")

    getAllUsers = db.session.query(db.UserModel).all()
    get_app_context = Sanic.get_app("C2")

    logger.info(getAllUsers)

    for record in getAllUsers:
        # logger.info(record.username, username)
        if record.username == username and record.password == password:
            
            logger.info("User found in database")
            logger.info(username + " logged in")

            jw_token = setJWT(username)
            get_app_context.ctx.jwt = jw_token # set jwt in app context
            # app.ctx.jwt = jw_token

            return HTTPResponse(headers = {"Set-Cookie": jw_token.getJWT()}) #set safe cookie attributes

    return HTTPResponse(status=404, body="user not found")
    # return text("user not found") # send a proper 404 status code