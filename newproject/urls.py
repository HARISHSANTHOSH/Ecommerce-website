"""newproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static




# add app path
urlpatterns = [
    path('admin/', admin.site.urls),

    path('newapp/',include('newapp.urls'))
    ]+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)




#  path('url name', include ('appname.urls'))

    # include : which is a function that is used to redirect into app's urls file one url file to another url file







