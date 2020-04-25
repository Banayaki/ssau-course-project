from flask import Blueprint, request
from flask.views import MethodView

from backend.EquationSolver import EquationSolver
from backend.utils.Logging import Logging
from backend.utils.ResponseHandler import make_response, response_from_exception

solver_blueprint = Blueprint('solver', __name__)


class SolverAPI(MethodView):

    def __init__(self):
        self.logger = Logging.get_logger(self.__class__.__name__)
        self.equation_solver = EquationSolver()

    def post(self):
        self.logger.info('POST method is called')
        try:
            data = request.get_json()
            K, C, R, T, lb, rb, max_error = self.parse_object(data)
            x, y = self.equation_solver.solve(K, C, R, T, lb, rb, max_error)
            response_object = {
                'x': x,
                'y': y
            }
            return make_response(response_object)
        except Exception as e:
            self.logger.exception(e)
            return response_from_exception(e)
        pass

    def parse_object(self, data):
        return data.values()


solver_view = SolverAPI.as_view('solver_api')

solver_blueprint.add_url_rule('/solve', view_func=solver_view, methods=['POST'])
