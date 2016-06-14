from flask_jsonpify import jsonify

from app import flask_app
from utils.meetup_utils import MeetupUtils


@flask_app.route("/")
def index():
    """
    Index view to verify the app is running
    """
    return "is working :)"


@flask_app.route("/get_groups")
def get_groups():
    """
    Enpoint that returns groups from meetup api
    """
    try:
        return jsonify({'result': MeetupUtils().get_all_groups()})
    except Exception as e:
        return jsonify({'result': "There was an error" + str(e)})