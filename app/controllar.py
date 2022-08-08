from flask_restful import Resource, request
from werkzeug.exceptions import BadRequest
from service import *

class Rates(Resource):
    # GET Method
    def get(self):
        """
        param : client request params

        return : process rates between port/region
        """
        origin = request.args.get("origin")
        destination = request.args.get("destination")
        date_from = request.args.get("date_from")
        date_to = request.args.get("date_to")
        flag, message = check_request_params(origin,destination,date_from,date_to)
        if flag:
            return get_rates(origin, destination, date_from, date_to)
        raise BadRequest({"Error" : "Invalid location arguments : " + message })