from flask import Blueprint
from app.core.event import Event
hello_blueprint = Blueprint('hello', __name__)


@hello_blueprint.route('/hello')
def hello():
    Event.send('new_queue', 'world')
    return "world"
