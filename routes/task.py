# How agent will communicate with the infra

from sanic import Blueprint, response, text
from db import db
from auth import protected
import logging, json
import random

logger = logging.getLogger()
logger.setLevel('INFO')

bp = Blueprint("task")

# class Model(db.Base):
#     __tablename__ = "tasks"
#     uuid = db.Column(db.String, primary_key=True)
#     task = db.Column(db.String)


@bp.route('/task', methods=['GET'])
@protected
def hi(request):
    return text("Tasks")


@bp.route('/create_task', methods=['GET', 'POST'])
@protected
def create_task(request):
    ag_uuid = request.args.get('uuid')
    ag_task = request.args.get('task')

    create_tsk = db.TaskModel(
        # id = random.randint(0,1000),
        uuid = ag_uuid,
        task = ag_task
    )
    db.session.add(create_tsk)
    db.session.commit()

    return text("Task created for agent - %s" % (ag_uuid))


@bp.route('/get_tasks/<uuid>', methods=['GET'])
@protected
def get_tasks(request, uuid):
    # jwt = request.cookie.jwt # get the jwt from cookie

    # verify the jwt

    # make db query
    agent_uuid = uuid
    responses = []

    task_info = {}

    get_all_uuid_with_tasks = db.session.query(db.TaskModel).filter(db.TaskModel.agent_uuid).scalar_subquery()
    instance = db.session.query(db.AgentModel).filter(db.AgentModel.uuid == agent_uuid and agent_uuid.in_(get_all_uuid_with_tasks)).all()

    # get_all_uuid_with_tasks = db.select(db.TaskModel.agent_uuid).scalar_subquery() # generates a list of uuid
    # instance = db.select(db.AgentModel).where(db.AgentModel.uuid == agent_uuid and agent_uuid.in_(get_all_uuid_with_tasks)) # checks if uuid exists in agents and has task(s) assigned

    try:
        # with db.engine.connect() as conn:
        #     for row in conn.execute(instance):
        #         responses.append(row)

        # if len(instance) == 0:
        #     return response.json(json.dumps("No tasks found"))
        
        for i in instance:
            print(i)

        # task_query = db.select(TaskModel.task).where(TaskModel.agent_uuid == agent_uuid)
        # tasks.update()
    except Exception as e:
        logger.info(e, exc_info = True)
        return response.json(json.dumps("No tasks found"))

    # tasks = db.session.query(Model).all()
    # for task in tasks:
    #     task_info[task.uuid] = task.task
    #     logger.info(task.uuid, task.task)

    # return response.json(json.dumps(instance)) 


    # return text(instance)

    # serialize the tasks

    # return the tasks in a format

    """

        {
            "commands": [
                "ls",
                "mkdir something",
                "do something with bash"
            ]
        }

    """