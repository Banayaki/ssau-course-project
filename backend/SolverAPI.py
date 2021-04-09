import numpy as np
from flask import Blueprint, request
from flask.views import MethodView

from EquationSolver import EquationSolver, ImplicitNumericalEquationSolver, ExplicitNumericalEquationSolver
from utils.Logging import Logging
from utils.ResponseHandler import make_response, response_from_exception

solver_blueprint = Blueprint('solver', __name__)


class SolverAPI(MethodView):

    def __init__(self):
        self.logger = Logging.get_logger(self.__class__.__name__)
        self.analytic_solver = EquationSolver()
        self.implicit_solver = ImplicitNumericalEquationSolver()
        self.explicit_solver = ExplicitNumericalEquationSolver()
        self.max_clip_value = 10e+30
        self.min_clip_value = -10e+30

    def post(self):
        self.logger.info('POST method is called')
        try:
            response_object = {}
            data = request.get_json()
            C, Explicit, Implicit, K, Nt, Nx, R, T, force_stability = self.parse_object(data)

            x, y = self.analytic_solver.solve(K, C, R, T, Nx)
            response_object['analytic'] = {
                'x': x,
                'y': self.clip(y),
            }

            if data.get('Implicit', False):
                impl_y = self.implicit_solver.solve(K, C, R, T, Nx, Nt)
                response_object['implicit'] = {
                    'y': self.clip(impl_y)
                }
            if data.get('Explicit', False):
                expl_y, is_stable = self.explicit_solver.solve(K, C, R, T, Nx, Nt, force_stability)
                response_object['explicit'] = {
                    'y': self.clip(expl_y),
                    'stability': is_stable
                }

            return make_response(response_object)
        except Exception as e:
            self.logger.exception(e)
            return response_from_exception(e)
        pass

    def clip(self, x):
        # return np.clip(np.nan_to_num(x, nan=self.max_clip_value), self.min_clip_value, self.max_clip_value).tolist()
        return np.nan_to_num(x, nan=0).tolist()
        # return x

    def parse_object(self, data: dict):
        sorted_keys = sorted(data.keys())
        return_list = []
        for key in sorted_keys:
            return_list.append(data[key])
        return return_list


solver_view = SolverAPI.as_view('solver_api')

solver_blueprint.add_url_rule('/solve', view_func=solver_view, methods=['POST'])
