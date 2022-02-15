#order details model
from app.app import db
from app.models.usermodel import User

class OrderDetails(db.Document):
	itemname = db.StringField(required=True)
	pickupaddress = db.StringField()
	ordereduser = db.ReferenceField(User)
	statusoforder = db.StringField(default="Pending Pickup")
	deliveryusername = db.StringField()
	locationofagent =  db.StringField()
	deliveryuserphoneno = db.StringField()
	orderid = db.StringField(required=True)
	deliveryaddress = db.StringField(required=True)
