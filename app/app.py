#application is defined here 
from flask import Flask
from flask_mongoengine import MongoEngine
from flask_login import LoginManager
from flask_restful import  Api
from flask_login import current_user
from flask_login import LoginManager

login_manager = LoginManager()
app = Flask(__name__,template_folder='../templates')

app.config["MONGODB_SETTINGS"] = {
	"db":"deliveryapp",
	"host":"localhost",
	"port":27017
}

app.secret_key = b'_5#y2L"Fjnmb\n\xec]/'
db =  MongoEngine(app)
api = Api(app)
