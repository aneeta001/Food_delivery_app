import uuid
from flask import jsonify,request,render_template,redirect, url_for
from flask_login import current_user
from app.models.usermodel import User
from app.models.orderdetailmodel import OrderDetails


hotelItem = {
				"barbeque nation":["chicken biriyani","grilled chicken","dessert platter","pani puri","malai kulfi","grilled prawns"],
				"rahmath hotel":["beef biriyani","chicken biriyani"],
				"the grillax":["peri peri chicken","grilled fish","shahi paneer tikka"],
				"restaurant 51":["beef lasagna","chicken sheek","lamb skewers"],
				"grand pavilion":["beef fry","pepper steak"],
				"cafe mojo":["sizzling brownie","hawaiian chicken","chicken momos"],
				"the yellow chilli":["dum biriyani","non-veg platter","lal mirch tikka"],
				"madison street":["american breakfast","beef brisket"],
				"the outhouse bistro":["chicken wings","chicken 65","alfredo pasta","veggie pizza"],
				"theos restaurant":["egg bhurji","pothy porotta","beef coconut fry"],
				"thali restaurant":["chicken dosa","karimeen fry","hyderabadi biriyani"],
				"paragon restaurant":["mutton biriyani","ghee rice","prawns biriyani"],
				"fusion table":["american chopsuey","fish and chips","tawa dajaj chicken"],
				"supreme allspice":["chicken burger","chicken lasagna","steak platter","tuna salad"],
				"chef's stop":["fish wrap","neymeen biriyani","kizhi porotta"], 
				"sulaimani":["veg noodles","chicken noodles","porotta"],
				"cafe qd":["sizzlers","zinger burger","chicken wrap"],
				"hungry rollers":["whole meat shawarma","arabic rice","lebanese shawarma"],
				"roastown":["korean fried chicken","lahmacan turkish pizza","seafood bisque","turkish pilaf","brownie mille-feuille"],
				"c'sons repeat":["falooda","banana split","dragon chicken"],
				"ming palace":["triple rice","pork in plum","bangkok beef","chicken lollipop"],
				"vintage cafe":["chilli chicken","chicken biriyani","egg wrap"],
				"green garden":["beef roast","veg noodles","chicken tikka","veg biriyani"],
				"1980's":["beef kizhi","chicken roast","prawns fry"],
				"chifonets":["dragon chicken","chicken momos","chicken lollipop","white sauce pasta","chinese chopsuey"],
				"cool land":["butter chicken","tandoori chicken","chicken biriyani","porotta"],
				"pepperpot":["french fries","chicken wings","dragon puttu"],
				"albaith":["falafel","broasted chicken","blossom mango","triple sundaes"],
				"muzvalla grill":["grilled platter","chicken al fahm","honey chilli al fahm"],
				"delicia":["kunafa","thai chicken"]}

items=[]


def admincheck():
	return render_template("admin.html")

def view_order_details():
	#function to view the user orders(admin privilege)
	orderitems = OrderDetails.objects.all()
	return render_template("orderplaced.html",orderitems=orderitems)


def addhotel():
	#function to add a hotel(admin privilege)
	if request.method == 'POST':
		global hotelname
		hotelname=request.form["hotelname"]
		return render_template("addhotel.html")
	else:
		return render_template("addhotel.html")


def additems():
	#function to add items for the newly added restaurant
	if request.method == 'POST':
		global itemname
		itemname = request.form["itemname"]
		print(itemname)
		items.append(itemname)
		print(items)
		return render_template("addhotel.html")

def finishedit():
	#to mark the end of restaurant adding process
	if request.method== "POST":
		hotelItem[hotelname]=items 
		return render_template("addhotel.html")

def removehotel():
	#function to remove a hotel(admin privilege)
	if request.method == 'POST':
		hotelname=request.form["hotelname"]
		del hotelItem[hotelname]
		return render_template("removehotel.html")
	else:
		return render_template("removehotel.html")
