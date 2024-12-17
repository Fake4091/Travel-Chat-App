from app.views import *

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login", login_view, name="login"),
    path("signup", signup_view, name="signup")
]
