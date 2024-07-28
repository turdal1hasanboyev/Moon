from django.contrib import admin

from moon.models import User, AboutMoon, Products, SpecialOffers, GetInTouch


admin.site.register(AboutMoon)
admin.site.register(SpecialOffers)
admin.site.register(Products)
admin.site.register(GetInTouch)
admin.site.register(User)
