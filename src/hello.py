from flask import Flask, jsonify
from database.db import db

app = Flask(__name__)
print (db)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://default:TuMdKmZRkO87@ep-icy-resonance-a4kcukot-pooler.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"
# initialize the app with the extension
db.init_app(app)

@app.route("/taxis")
def hello_world():
    return jsonify("Hello, World!!!")

