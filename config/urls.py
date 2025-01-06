from app.views import *

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),

    # user based
    path("login", login_view, name="login"),
    path('logout', logout_view, name="logout"),
    path("signup", signup_view, name="signup"),

    # roles
    path('role-apply', role_apply_view, name="role-apply"),
    path('role-apply/<server>', role_apply_server_view, name="role-apply-server"),
    path('role-apply/<server>/<channel>', role_apply_channel_view, name="role-apply-server-channel"),

    # main pages
    path("home", home_view, name="home"),
    path("home/<server>", home_server_view, name="home-server" ),
    path("home/<server>/<channel>", home_channel_view, name='home-channel'),
    path("roles", roles_page_view, name="roles-page"),

    # server based
    path("join-server", join_server_view, name="join-server"),
    path("join_success/<server_name>", join_success_view, name="join_success"),

]
