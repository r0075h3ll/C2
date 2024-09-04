from functools import wraps

import jwt
from sanic import text, Sanic

def check_token(request):
    app_inst = Sanic.get_app("C2")

    jw_secret = app_inst.config.secrets['JWT_SECRET']
    token = request.cookies.get("token", False)
    if not token:
        return False, "Token Required"

    if app_inst.ctx.jwt is None:
        return False, "Invalid Session"

    try:
        jwt.decode(
            token, jw_secret, algorithms=["HS256"]
        )
    except jwt.exceptions.InvalidTokenError:
        return False, "Invalid Token"
    else:
        return True, ""

def protected(wrapped):
    def decorator(f):
        @wraps(f)
        async def decorated_function(request, *args, **kwargs):
            is_authenticated,_ = check_token(request)

            if is_authenticated:
                response = f(request, *args, **kwargs) # call the handler for authenticated endpoint
                return response
            else:
                return text(_, 404) # or redirect to index page

        return decorated_function

    return decorator(wrapped)

# if __name__ == "__main__":
    # jw_secret = Sanic.get_app("C2").config.secrets['JWT_SECRET'] # what if this variable gets leaked?