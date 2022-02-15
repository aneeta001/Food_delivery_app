#routers
from app.app import api, app, login_manager
from app.models.usermodel import User
from app.views.userregistration import userregister,userlogin,logout
from app.views.orderitem import orderitem,orderupdate, hotelitems
from app.views.admin import view_order_details, addhotel, removehotel, admincheck, finishedit, additems

login_manager.init_app(app)
@login_manager.user_loader

def load_user(user):
    """current user details"""
    return User.objects.get(id=user)

#for login
app.add_url_rule("/", view_func=userlogin, methods=["GET","POST"])

#for admin login
app.add_url_rule("/admin",view_func=admincheck, methods=["GET","POST"])

#for user register
app.add_url_rule("/register",view_func=userregister,methods=["GET","POST"])

#for ordering item
app.add_url_rule("/orderitem",view_func=orderitem,methods=["GET","POST"])

#for order update and is available only for delivery user
app.add_url_rule("/orderupdate",view_func=orderupdate,methods=["GET","POST"])

#to view the user orders(admin privilege)
app.add_url_rule("/vieworders",view_func=view_order_details,methods=["GET","POST"])

#to add a restaurant(admin privilege)
app.add_url_rule("/addhotel",view_func=addhotel,methods=["GET","POST"])

#to add items for the newly added restaurant(admin privilege)
app.add_url_rule("/additems",view_func=additems,methods=["GET","POST"])

#to mark the end of restaurant adding process
app.add_url_rule("/finishedit",view_func=finishedit,methods=["GET","POST"])

#to remove a restaurant(admin privilege)
app.add_url_rule("/removehotel",view_func=removehotel,methods=["GET","POST"])

#to pass menu items based on hotel chosen
app.add_url_rule("/hotelitems",view_func=hotelitems,methods=["GET","POST"])

#for logout
app.add_url_rule("/logout",view_func=logout,methods=["GET","POST"])

