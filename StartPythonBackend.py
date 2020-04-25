from flask import Flask

from backend.SolverAPI import solver_blueprint

app = Flask(__name__)

app.register_blueprint(solver_blueprint)

if __name__ == '__main__':
    app.run(host='localhost', port=51115, debug=False)
