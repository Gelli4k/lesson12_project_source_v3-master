import logging

from flask import Flask, request, render_template, send_from_directory
# from functions import ...
from main.views import main_blueprint
from loader.views import loader_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)


@app.errrorhandler(400)
def bad_request_error(error):
    logging.INFO(error)
    return render_template("error 400.html", error=error)


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)

if __name__ == "__main__":
    app.run()

