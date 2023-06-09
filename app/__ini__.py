from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


from app.views import upload_csv

# Endpoints
app.add_url_rule("/upload", view_func=upload_csv)
