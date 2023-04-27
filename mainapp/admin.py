from django.contrib import admin
from .models import *
admin.site.register(User)
admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(Cities)
admin.site.register(Region)
admin.site.register(ModerationAd)
