from app.views import *

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),

    # user-based
    path("login", login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path("signup", signup_view, name="signup"),

    # main pages
    path("home", home_view, name="home"),
]
