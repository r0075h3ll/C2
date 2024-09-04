# api/content/__init__.py
from sanic import Blueprint
import routes.agent
import routes.task

# print(dir(routes.task))

content = Blueprint.group(agent.bp, task.bp, url_prefix="/agent")