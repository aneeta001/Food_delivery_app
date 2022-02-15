import uuid
from flask import jsonify,request,render_template,redirect, url_for
from flask_login import current_user
from app.models.usermodel import User
from app.models.orderdetailmodel import OrderDetails
from app.views.admin import hotelItem

def orderitem():
	#function for ordering item
	if request.method == 'POST':
		itemname = request.form["itemname"]
		# pickupaddress = request.form["pickupaddress"]
		newaddress = request.form["newaddress"]
		deliveryaddress = request.form.get("deliveryaddress")
		print(deliveryaddress)
		if  newaddress:
			user =  User.objects.get(id=current_user.id)
			deliveryaddresslist = user.deliveryaddress
			deliveryaddresslist.append(newaddress)
			user.deliveryaddress = deliveryaddresslist
			user.save()
			deliveryaddress = newaddress
		else:
			deliveryaddress=deliveryaddress
		uniqueuid = uuid.uuid4().hex
		OrderDetails.objects.create(itemname=itemname,deliveryaddress=deliveryaddress,
			ordereduser = current_user.id,orderid=uniqueuid)
		user =  User.objects.get(id=current_user.id)
		orderitems = OrderDetails.objects(ordereduser=current_user.id)
		return render_template("orderplaced.html",user=user,orderitems=orderitems)
	else:
		user =  User.objects.get(id=current_user.id)
		orderitems = OrderDetails.objects(ordereduser=current_user.id)
		return render_template("order.html",user=user,orderitems=orderitems, hotelItem=hotelItem)
	

def orderupdate():
	#function for order update by delivery user 
	if request.method=='POST':
		if (current_user.userrole=="deliveryuser"):		
			orderid = request.form["orderid"]
			statusoforder = request.form["statusoforder"]
			deliveryusername = request.form["deliveryusername"]
			locationofagent = request.form["locationofagent"]
			deliveryuserphoneno = request.form["deliveryuserphoneno"]
			order = OrderDetails.objects.get(orderid=orderid)
			order.statusoforder = statusoforder
			order.deliveryusername = deliveryusername
			order.locationofagent = locationofagent
			order.deliveryuserphoneno = deliveryuserphoneno
			order.save()
			orderitems=OrderDetails.objects.all()
			return render_template("delorderdetails.html", orderitems=orderitems)
		else:
			return render_template("login.html")
	else:
		if (current_user.userrole=="deliveryuser"):	
			return render_template("deliveryupdate.html")
		else:
			return render_template("login.html")

def hotelitems():
	#function to pass items based on the hotel chosen
	if request.method == 'POST':
		hotelname = request.form["hotel"]
		menuitems=hotelItem[hotelname]
		user =  User.objects.get(id=current_user.id)
		return render_template("order.html", user=user, menuitems=menuitems, hotelItem=hotelItem) 
