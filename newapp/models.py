from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# models=module
#Model=parent class


class regmodel(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    password = models.CharField(max_length=20)


class employemodel(models.Model):
    employename = models.CharField(max_length=30)
    employeid = models.IntegerField()
    companyname = models.CharField(max_length=30)
    email = models.EmailField()
    department = models.CharField(max_length=30)


class imgmodel(models.Model):
    imgname=models.CharField(max_length=30)
    imgfile=models.ImageField(upload_to='newapp/static')

class audiomodell(models.Model):
    audioname=models.CharField(max_length=30)
    audioimage=models.ImageField(upload_to="newapp/static")
    audiofile=models.FileField(upload_to="newapp/static")

class videomodel(models.Model):
    videoname=models.CharField(max_length=30)
    videofile=models.FileField(upload_to="newapp/static")


class resumemodel(models.Model):
    employename=models.CharField(max_length=30)
    resume=models.FileField(upload_to="newapp/static")


class shopmodel(models.Model):
    shopname=models.CharField(max_length=30)
    location=models.CharField(max_length=30)
    address=models.CharField(max_length=30)
    shopid=models.IntegerField()
    email=models.EmailField()
    phonenumber=models.IntegerField()
    password=models.CharField(max_length=30)
    def __str__(self):
        return self.shopname

class productmodel(models.Model):
    shopid=models.IntegerField()
    productname=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.CharField(max_length=30)
    productimage=models.ImageField(upload_to="newapp/static")

    def __str__(self):
        return self.productname


class profileload(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    auth_token=models.CharField(max_length=100)
    is_verified=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user


class cart(models.Model):
    usernme=models.CharField(max_length=30,default='SOME STRING')
    productname=models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=30)
    productimage = models.ImageField()

    def __str__(self):
        return self.productname


class wishlist(models.Model):
    usernme=models.CharField(max_length=30,default='SOME STRING')
    productname = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=30)
    productimage = models.ImageField()

    def __str__(self):
        return self.productname


class cartbuyss(models.Model):
    productname=models.CharField(max_length=30)
    price=models.IntegerField()
    description=models.CharField(max_length=30)
    productimage=models.ImageField()
    quantity=models.IntegerField()

    def __str__(self):
        return self.productname


class cusdetailsmodel(models.Model):
    cardholdername=models.CharField(max_length=30)
    cardnumber=models.CharField(max_length=30)
    expiredate=models.CharField(max_length=30)
    securitycode=models.CharField(max_length=30)

    def __str__(self):
        return self.cardholdername


class snotification(models.Model):
    content=models.CharField(max_length=200)
    shopnot=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content

class usnotification(models.Model):
    content=models.CharField(max_length=200)
    shopnot=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.content
