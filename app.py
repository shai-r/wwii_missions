from flask import Flask

from controllers.target_controller import all_targets, targets_blueprint
from repository.database import create_tables


app = Flask(__name__)

if __name__ == '__main__':
    create_tables()
    app.register_blueprint(targets_blueprint, url_prefix="/api/mission")
    app.run(debug=True)