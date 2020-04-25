import json


def make_response(response_object):
    return json.dumps(response_object), 200


def response_from_exception(exception):
    response_object = {
        'status': 'fail',
        'message': str(exception)
    }
    return json.dumps(response_object), 400
