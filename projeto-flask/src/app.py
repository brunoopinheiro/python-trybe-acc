from os import environ
from waitress import serve
from flask import Flask
from controllers.jokes_controller import jokes_controller
from controllers.home_controller import home_controller

app = Flask(__name__)
app.static_folder = "views/static"
app.template_folder = "views/templates"
app.register_blueprint(home_controller, url_prefix="/")
app.register_blueprint(jokes_controller, url_prefix="/jokes")


def start_server(host: str = "0.0.0.0", port: int = 8000):
    if environ.get("FLASK_ENV") == "dev":
        return app.run(debug=True, host=host, port=port)
    else:
        serve(app, host=host, port=port)


if __name__ == "__main__":
    start_server()
