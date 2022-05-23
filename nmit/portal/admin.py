from django.contrib import admin

# Register your models here.
from .models import Activity, Ngo, User

admin.site.register(Ngo)
admin.site.register(Activity)
admin.site.register(User)
