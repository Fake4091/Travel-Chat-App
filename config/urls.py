from app.views import *

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),

    # user based
    path("login", login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path("signup", signup_view, name="signup"),

    # main pages
    path("home", home_view, name="home"),

    # server based
    path("join", join_view, name="join"),
    path("join_success/<server_name>", join_success_view, name="join_success")

]
