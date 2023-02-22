from django import forms

#forms--> module
#Form --> parent class


class regform(forms.Form):
    username=forms.CharField(max_length=30)
    email=forms.EmailField()
    phonenumber=forms.IntegerField()
    password=forms.CharField(max_length=20)
    confirmpassword=forms.CharField(max_length=20)



class logform(forms.Form):
    username=forms.CharField(max_length=30)
    password=forms.CharField(max_length=20)

class employeform(forms.Form):
    employename=forms.CharField(max_length=30)
    employeid=forms.IntegerField()
    companyname=forms.CharField(max_length=30)
    email=forms.EmailField()
    department=forms.CharField(max_length=30)

class employesearchform(forms.Form):
    employename=forms.CharField(max_length=30)
    employeid=forms.IntegerField()

class imgform(forms.Form):
    imgname=forms.CharField(max_length=30)
    imgfile=forms.ImageField()

class audioform(forms.Form):
    audioname=forms.CharField(max_length=30)
    audioimage=forms.ImageField()
    audiofile=forms.FileField()

class videoform(forms.Form):
    videoname=forms.CharField(max_length=30)
    videofile=forms.FileField()

class resumeform(forms.Form):
    employename=forms.CharField(max_length=30)
    resume=forms.FileField()

class shopform(forms.Form):
    shopname=forms.CharField(max_length=30)
    location=forms.CharField(max_length=30)
    address=forms.CharField(max_length=30)
    shopid=forms.IntegerField()
    email=forms.EmailField()
    phonenumber=forms.IntegerField()
    password=forms.CharField(max_length=20)
    confirmpassword=forms.CharField(max_length=20)
class shoploginform(forms.Form):
    shopname=forms.CharField(max_length=30)
    password=forms.CharField(max_length=20)


class productform(forms.Form):
    productname=forms.CharField(max_length=30)
    price=forms.IntegerField()
    description=forms.CharField(max_length=30)
    productimage=forms.ImageField()

class cusdetailsform(forms.Form):
    cardholdername=forms.CharField(max_length=30)
    cardnumber=forms.CharField(max_length=30)
    expiredate=forms.CharField(max_length=30)
    securitycode=forms.CharField(max_length=30)