from SolverAPI import solver_blueprint
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(solver_blueprint)

if __name__ == '__main__':
    app.run(host='localhost', port=51115, debug=False)
