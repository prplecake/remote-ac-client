from flask import Flask

from . import ir_blaster


app = Flask(__name__)
app.register_blueprint(ir_blaster.bp)
