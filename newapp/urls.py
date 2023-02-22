from django.urls import path
from .views import *
urlpatterns=[
    path('first/',first),
    path("second/",second),
    path("third/",third),
    path("four/",four),
    path("five/",five),
    path("registrationpage/",registration),
    path("loginpage/",loginup),
    path("employein/",employeinn),
    path("employesearch/",employesearch),
    path('display/',display),
    path('dispfreak/',dispfreak),
    path("imageupload/",imageupload),
    path("audioupload/",audioupload),
    path("videoupload/",videoupload),
    path("imagedisplay/",imagedisplay),
    path("Videodisplay/",videodisplay),
    path("audiodisplay/",audiodisplay),
    path("resumeupload/",resumeupload),
    path("resumedisplay/",resumedisplay),
    path("shopregister/",shopregister),
    path("shoplogin/",shoplogin),


    path("productload/",productupload),
    path('productdisplay/',productdisplay),
    path("profilehtml/",profile),
    path("productdelete/<int:id>",productdelete),
    path("productedit/<int:id>",productedit),
    path("index/",index),
    path("userregister/",userreg),
    path("success/",success),
    path("verify/<auth_token>",verify),
    path("userlogin/", logins),
    path("userview/",userview),
    path("contact/",contact),
    path("grandsale/",grandsale),
    path("newarrivals/",newarrival),
    path("newseason/",season),
    path("addcart/<int:id>",cartitem),
    path("wishlisttocart/<int:id>",wishlisttocart),
    path("wishlist/<int:id>",wishlistitem),
    path("cartdisplay/",cartdisplay),
    path("wishlistdisplay/",wishlistdisplay),
    path("removecart/<int:id>",remove),
    path("removewishlist/<int:id>",removewishlist),
    path("cartbuy/<int:id>/",cartbuys),
    path("placeorder/",placeorder),
    path("payment/",paymentdone),
    path("snotification/",shopnotification),
    path("usernotification/",usernotification)























]
#  path('url'name',function_name)