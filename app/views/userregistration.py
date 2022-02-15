import json
from app.app import login_manager
from app.models.usermodel import User
from app.models.orderdetailmodel import OrderDetails
from flask_restful import Resource
from app.views.orderitem import orderitem
from flask import jsonify,request,flash,render_template,redirect, url_for
from flask_login import current_user,LoginManager,login_required,login_user,logout_user

def userlogin():
	#user login
	if request.method == 'POST':
		print(request.form,request.form["username"])
		if (request.form["username"]=="admin@001" and request.form["password"]=="admin098765"):
		 	return redirect(url_for('admincheck'))
		else:
			user = User.objects.get(username=request.form["username"])
			if (user.userpassword==request.form["password"]):
				login_user(user)
				flash('You were successfully logged in.')
				if user.userrole=="deliveryuser":
					orderitems=OrderDetails.objects.all()
					return render_template("delorderdetails.html",orderitems=orderitems)
				return redirect(url_for('orderitem'))
			else:
				render_template('login.html')
	return render_template('login.html')


def userregister():
	#user registration
	if request.method == 'POST':
		username = request.form["username"]
		userpassword = request.form["userpassword"]
		usermailid = request.form["usermailid"]
		userrole = request.form["userrole"]
		deliveryaddress = request.form["deliveryaddress"]
		deliveryaddresslist = []
		deliveryaddresslist.append(deliveryaddress)
		userphoneno = request.form["userphoneno"]
		print(request.form)
		User.objects.create(username=username,userpassword=userpassword,
			usermailid=usermailid,userrole=userrole,
			deliveryaddress=deliveryaddresslist,userphoneno=userphoneno)
		return redirect(url_for('userlogin'))
	else:
		return render_template('register.html')


def logout():
	logout_user()
	return redirect(url_for('userlogin'))
