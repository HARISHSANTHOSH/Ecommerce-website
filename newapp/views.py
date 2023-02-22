from django.core.mail import send_mail
from django.shortcuts import render,redirect
import os
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.models import User
import uuid
from django.contrib import messages
from django.contrib.auth import authenticate
import time
import datetime
from datetime import timedelta



from newproject.settings import EMAIL_HOST_USER
from django.contrib.auth import get_user_model

from django.conf.urls.static import static
# Create your views here.

def first(request):
    return HttpResponse("hello welcome")

def second(request):
    return HttpResponse("Second page")


# passing html tags to httpresponse

def third(request):
    return HttpResponse("<h1>Python django</h1>"
                        "<p>this is a django page</p>")


#render() : render is a function that combines a template with a view and returns html page

#request= first.htmlfiles
def four(request):
    return render(request,"first.html")




# templates : it is a directory that is used to collect html files


#create a django page with
# pythondjango // font color size , underline , center

# sunheading // about django

#paragraph

def five(request):
    return render(request,"second.html")



# create a registration page with name,emailid,phnnumber,password,confirm password

#login page

# name
# password


def registration(request):
    if request.method=='POST':
        a=regform(request.POST)
        if a.is_valid():
            us=a.cleaned_data["username"]
            em=a.cleaned_data["email"]
            ph=a.cleaned_data["phonenumber"]
            ps=a.cleaned_data["password"]
            cp=a.cleaned_data["confirmpassword"]
            if ps==cp:
                b=regmodel(username=us,email=em,phonenumber=ph,password=ps)
                b.save()
                return HttpResponse("registration success")
            else:
                return HttpResponse("incorrect password")
        else:
             return HttpResponse("registration failed")


    return render(request,"registration.html")








def loginup(request):
    if request.method=='POST':
        a=logform(request.POST)
        if a.is_valid():
            us=a.cleaned_data["username"]
            ps=a.cleaned_data["password"]
            b=regmodel.objects.all()
            for i in b:
                if us==i.username and ps==i.password:
                    return HttpResponse("loginsuccess")
            else:
                return HttpResponse("login failed")
    return render(request,"login.html")



def employeinn(request):
    if request.method=='POST':
        a=employeform(request.POST)
        if a.is_valid():
            emn=a.cleaned_data["employename"]
            emid=a.cleaned_data["employeid"]
            cmpn=a.cleaned_data["companyname"]
            em=a.cleaned_data["email"]
            dep=a.cleaned_data["department"]
            b=employemodel(employename=emn,employeid=emid,companyname=cmpn,email=em,department=dep)
            b.save()
            return HttpResponse("new employe added")
    return render(request,"employein.html")



def employesearch(request):
    if request.method=='POST':
        a=employesearchform(request.POST)
        if a.is_valid():
            em=a.cleaned_data["employename"]
            emid=a.cleaned_data["employeid"]
            b=employemodel.objects.all()
            for i in b:
                if em==i.employename and emid==i.employeid:
                    return HttpResponse("employe founded")
            else:
                return HttpResponse("not found")
    return render(request,"employesearch.html")

# display
# frontend --> bcakend--> database : post
#database--> backend --> frontend : get



def display(request):                                        #html                      # video : video name video file
                                                              #audio name
    a=regmodel.objects.all()                                  # audio image
                                                              # audio file # file field

    return render(request,"display.html",{"a":a})

def dispfreak(request):
    a=employemodel.objects.all()

    return render(request,"dispfreak.html",{"a":a})


def imageupload(request):
    if request.method=='POST':
        a=imgform(request.POST,request.FILES)


        if a.is_valid():
            imgn=a.cleaned_data["imgname"]
            imgf=a.cleaned_data["imgfile"]
            b=imgmodel(imgname=imgn,imgfile=imgf)
            b.save()
            return HttpResponse("uploaded")
        else:
            return HttpResponse("not uploaded")

    return render(request,"imageupload.html")

def imagedisplay(request):
    a=imgmodel.objects.all()
    image=[]
    name=[]

    for i in a:
        im=i.imgfile
        image.append(str(im).split('/')[-1])
        nm=i.imgname
        name.append(nm)
    mylist=zip(image,name)

    return render(request,"imagedisplay.html",{"mylist":mylist})








def audioupload(request):
    if request.method=='POST':
        a=audioform(request.POST,request.FILES)
        if a.is_valid():
            audnm=a.cleaned_data["audioname"]
            audimg=a.cleaned_data["audioimage"]
            audfl=a.cleaned_data["audiofile"]
            b=audiomodell(audioname=audnm,audioimage=audimg,audiofile=audfl)
            b.save()
            return HttpResponse("audio uploaded")
        else:
            return HttpResponse("failed")




    return render(request,"audioupload.html")

def audiodisplay(request):
    a=audiomodell.objects.all()
    audioname=[]
    audioimage=[]
    audiofile=[]
    for i in a:
        audn=i.audioname
        audimg=i.audioimage
        audf=i.audiofile
        audioname.append(audn)
        audioimage.append(str(audimg).split('/')[-1])
        audiofile.append(str(audf).split('/')[-1])
    mylist=zip(audioname,audioimage,audiofile)
    return render(request,"audiodisplay.html",{"mylist":mylist})


def videoupload(request):
    if request.method=='POST':
        a=videoform(request.POST,request.FILES)
        if a.is_valid():
            vidn=a.cleaned_data["videoname"]
            vidf=a.cleaned_data["videofile"]
            b=videomodel(videoname=vidn,videofile=vidf)
            b.save()
            return  HttpResponse("video uploaded")
        else:
            return HttpResponse("failed")
    return render(request,"video.html")


def videodisplay(request):
    a=videomodel.objects.all()
    videoname=[]
    videofile=[]

    for i in a:
        vdf=i.videofile

        videofile.append(str(vdf).split('/')[-1])
        vdn=i.videoname
        videoname.append(vdn)
    mylist=zip(videoname,videofile)
    return render(request,"videodisplay.html",{"mylist":mylist})



def resumeupload(request):
    if request.method=='POST':
        a=resumeform(request.POST,request.FILES)
        if a.is_valid():
            empn=a.cleaned_data["employename"]
            resf=a.cleaned_data["resume"]
            b=resumemodel(employename=empn,resume=resf)
            b.save()
            return HttpResponse("resume submitted successfully")
        else:
            return HttpResponse("failed")
    return render(request,"resumeupload.html")

def resumedisplay(request):
    a=resumemodel.objects.all()
    employename=[]
    resumefile=[]
    for i in a:
        empn=i.employename
        rsf=i.resume
        employename.append(empn)
        resumefile.append(rsf)
    mylist=zip(employename,resumefile)

    return render(request,"resumedisplay.html",{"mylist":mylist})


def shopregister(request):
    if request.method=='POST':
        a=shopform(request.POST)
        if a.is_valid():
            shpn=a.cleaned_data["shopname"]
            loc=a.cleaned_data["location"]
            add=a.cleaned_data["address"]
            shpid=a.cleaned_data["shopid"]
            em=a.cleaned_data["email"]
            ph=a.cleaned_data["phonenumber"]
            ps=a.cleaned_data["password"]
            cp=a.cleaned_data["confirmpassword"]
            if ps==cp:
                b=shopmodel(shopname=shpn,location=loc,address=add,shopid=shpid,email=em,phonenumber=ph,password=ps)
                b.save()
                return HttpResponse("registrationsucess")
            else:
                return HttpResponse("registration failed")
    return render(request,"shopregister.html")


def shoplogin(request):
    if request.method=='POST':
        a=shoploginform(request.POST)
        if a.is_valid():
            shpn=a.cleaned_data["shopname"]
            pss=a.cleaned_data["password"]
            b=shopmodel.objects.all()
            request.session['shopname']=shpn            # to make a variable global
            for i in b:
                if i.shopname==shpn and i.password==pss:
                    request.session['id']=i.id
                    return redirect(profile)
    return render(request,"shoplogin.html")


def profile(request):
    shopname=request.session['shopname']
    return render(request,"profile.html",{"shopname":shopname})

def productupload(request):
    if request.method=='POST':
        a=productform(request.POST,request.FILES)
        id=request.session['id']


        if a.is_valid():
            prdn=a.cleaned_data["productname"]
            prc=a.cleaned_data["price"]
            desc=a.cleaned_data["description"]
            prdimg=a.cleaned_data["productimage"]
            b=productmodel(shopid=id,productname=prdn,price=prc,description=desc,productimage=prdimg)
            b.save()
            return redirect(productdisplay)
    return render(request,"productupload.html")


def productdisplay(request):
    shpid=request.session['id']


    a=productmodel.objects.all()
    productname=[]
    price=[]
    description=[]
    productimage=[]
    id=[]
    shopid=[]


    for i in a:
        sid=i.shopid
        shopid.append(sid)

        id1=i.id
        id.append(id1)



        prdn=i.productname

        prc=i.price
        desc=i.description
        prdimg=i.productimage
        productname.append(prdn)
        price.append(prc)
        description.append(desc)
        productimage.append(str(prdimg).split('/')[-1])
    mylist=zip(productname,price,description,productimage,id,shopid)
    return render(request,"productdisplay.html",{"mylist":mylist,"shpid":shpid})





#models.objects.all() //fetchall
#models.objects.get(id=id)

def productdelete(request,id):
    a=productmodel.objects.get(id=id)
    a.delete()

    return redirect(productdisplay)


def productedit(request,id):

    a=productmodel.objects.get(id=id)
    im=str(a.productimage).split('/')[-1]

    if request.method=='POST':
        if len(request.FILES):  # checking new file
            if len(a.productimage)>0: # old file
                os.remove(a.productimage.path)
            a.productimage=request.FILES["image"] #edit input image name
        a.productname=request.POST.get('productname')
        a.price=request.POST.get('price')
        a.description=request.POST.get('description')
        a.save()
        return redirect(productdisplay)



    return render(request,"editproduct.html",{"a":a,'im':im})


def userreg(request):
    if request.method =='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        password=request.POST.get('password')
        if User.objects.filter(username=username).first(): #user checjin exist
            messages.success(request,'username already exists')
            return redirect(userreg)
        if User.objects.filter(email=email).first():
            messages.success(request,'email already taken')
            return redirect(userreg)
        user_obj=User(username=username,email=email,first_name=firstname,last_name=lastname)
        user_obj.set_password(password)
        user_obj.save()
        auth_token=str(uuid.uuid4())   #rhtugjit
        profile_obj=profileload.objects.create(user=user_obj,auth_token=auth_token)
        profile_obj.save()
        send_mail_regis(email,auth_token)
        return render(request,'success.html')
    return render(request,'userregister.html')



def success(request):
    return render(request,'success.html')

def send_mail_regis(email,auth_token):
    subject="your account has been verified"
    #f is a string literal which contains expressions inside curley brackets,the expressions are replaced by values
    message=f'click the link to verify the account http://127.0.0.1:8000/newapp/verify/{auth_token}'
    email_from=EMAIL_HOST_USER
    recipient=[email]
    #inbuilt fn sendmail
    send_mail(subject,message,email_from,recipient)





def index(request):
    username=request.session['username']
    return render(request,"index.html",{"username":username})


def regiscom(request):
    return render(request,"registrationcomplete.html")


def verify(request,auth_token):
    profile_obj=profileload.objects.filter(auth_token=auth_token).first()
    if profile_obj: #true
        if profile_obj.is_verified:  # if profile object s false
            messages.success(request,"your account is already verified")
            return redirect(logins)
        profile_obj.is_verified=True
        profile_obj.save()
        messages.success(request,"your account has been verified")
        return redirect(logins) #logi function (login)
    else:
        messages.success(request,"user not found")
        return redirect(logins)


def logins(request):
    if request.method=='POST':
        username=request.POST.get("username") #hari
        password=request.POST.get("password") #123
        request.session['username']=username
        user_obj=User.objects.filter(username=username).first()


        if user_obj is None: # if user doesnt exist
            messages.success(request,"user not found")
            return redirect(logins)
        profile_obj=profileload.objects.filter(user=user_obj).first()

        if not profile_obj.is_verified: # if no profile is verified


            messages.success(request,"profile is not verifid check your email")
            return redirect(logins)
        user=authenticate(username=username,password=password)
        # user valid
        # if the given credentials are valid,return a userobject

        if user is None:
            messages.success(request,"wrong password ot username")
            return redirect(logins)
        return redirect(userview)
    return render(request,"userlogin.html")


def userview(request):
    username=request.session['username']
    a=productmodel.objects.all()
    productname=[]
    price=[]
    description=[]
    productimage=[]
    id=[]

    for i in a:
        id1=i.id
        id.append(id1)

        prdn=i.productname
        prc=i.price
        desc=i.description
        prdimg=i.productimage
        productname.append(prdn)
        price.append(prc)
        description.append(desc)
        productimage.append(str(prdimg).split('/')[-1])
    mylist=zip(productname,price,description,productimage,id)

    return render(request,"userview.html",{"mylist":mylist,"username":username})


def contact(request):
    username = request.session['username']
    return render(request,"contact.html",{"username":username})


def grandsale(request):
    return render(request,"grandsale.html")

def newarrival(request):
    return render(request,"newarrivals.html")

def season(request):
    return render(request,"newseason.html")


def cartitem(request,id):
    a=productmodel.objects.get(id=id)
    username=request.session["username"]
    if cart.objects.filter(productname=a.productname).first():
        return HttpResponse("already in cart")

    b=cart(usernme=username,productname=a.productname,price=a.price,description=a.description,productimage=a.productimage)
    b.save()
    return HttpResponse("item added successfully")

def wishlistitem(request,id):
    a=productmodel.objects.get(id=id)
    username = request.session["username"]
    if wishlist.objects.filter(productname=a.productname).first():
        return HttpResponse("already exist")

    b=wishlist(usernme=username,productname=a.productname,price=a.price,description=a.description,productimage=a.productimage)
    b.save()
    return HttpResponse("added")

def wishlisttocart(request,id):
    a=wishlist.objects.get(id=id)
    username=request.session["username"]
    if cart.objects.filter(productname=a.productname).first():
        return HttpResponse("already exist")
    b=cart(usernme=username,productname=a.productname,price=a.price,description=a.description,productimage=a.productimage)
    b.save()
    return HttpResponse("added")


def cartdisplay(request):
    username=request.session['username']
    a = cart.objects.all()
    productname = []
    price = []
    description = []
    productimage = []
    id = []
    usernm=[]

    for i in a:
        id1 = i.id
        id.append(id1)
        us=i.usernme
        usernm.append(us)

        prdn = i.productname
        prc = i.price
        desc = i.description
        prdimg = i.productimage
        productname.append(prdn)
        price.append(prc)
        description.append(desc)
        productimage.append(str(prdimg).split('/')[-1])
    mylist = zip(productname, price, description, productimage, id,usernm)
    return render(request, "cartdisplay.html", {"mylist": mylist,"username":username})

def wishlistdisplay(request):
    username=request.session['username']
    a = wishlist.objects.all()
    productname = []
    price = []
    description = []
    productimage = []
    id = []
    usname=[]

    for i in a:
        id1 = i.id
        id.append(id1)
        us=i.usernme
        usname.append(us)

        prdn = i.productname
        prc = i.price
        desc = i.description
        prdimg = i.productimage
        productname.append(prdn)
        price.append(prc)
        description.append(desc)
        productimage.append(str(prdimg).split('/')[-1])
    mylist = zip(productname, price, description, productimage, id,usname)
    return render(request, "wishlistdisplay.html", {"mylist": mylist,"username":username})


def remove(request,id):
    a=cart.objects.get(id=id)
    a.delete()
    return redirect(cartdisplay)


def removewishlist(request,id):
    a=wishlist.objects.get(id=id)
    a.delete()
    return redirect(wishlistdisplay)


def cartbuys(request,id):
    a=cart.objects.get(id=id)
    im=str(a.productimage).split('/')[-1]
    if request.method=='POST':

        name=request.POST.get('productname')
        price=request.POST.get('price')
        description=request.POST.get('description')
        quantity=request.POST.get('quantity')
        b=cartbuyss(productname=name,price=price,description=description,quantity=quantity)
        b.save()
        total=int(price)*int(quantity)
        return render(request,"finalbill.html",{"total":total,"name":name,"price":price,"quantity":quantity,"im":im})
    return render(request,"cartbuy.html",{"a":a,"im":im})


def placeorder(request):
    if request.method=="POST":
        crdnm=request.POST.get("cardholdername")
        crdno=request.POST.get("cardnumber")
        exprd=request.POST.get("expiredate")
        sucr=request.POST.get("securitycode")
        b=cusdetailsmodel(cardholdername=crdnm,cardnumber=crdno,expiredate=exprd,securitycode=sucr)
        b.save()
        return redirect(paymentdone)







    return render(request,"placeorder.html")




def paymentdone(request):
    a=datetime.datetime.now()
    a+=timedelta(days=5)






    return render(request,"payementdone.html",{"a":a})




def shopnotification(request):
    a=snotification.objects.all()
    content=[]
    sdate=[]
    for i in a:
        cnt=i.content
        dt=i.shopnot
        content.append(cnt)
        sdate.append(dt)
    mylist=zip(content,sdate)

    return render(request,"snotification.html",{"mylist":mylist})


def usernotification(request):
    a=usnotification.objects.all()
    content=[]
    sdate=[]
    for i in a:
        cnt=i.content
        dt=i.shopnot
        content.append(cnt)
        sdate.append(dt)
    mylist=zip(content,sdate)

    return render(request,"usernotification.html",{"mylist":mylist})