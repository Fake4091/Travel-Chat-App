from django.contrib import admin
from app.models import *

# Registering all models to admin page. 

admin.site.register(Server)
admin.site.register(Channel)
admin.site.register(Role)
admin.site.register(Profile)
admin.site.register(Message)
admin.site.register(Business)
